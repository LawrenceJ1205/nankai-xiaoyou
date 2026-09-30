"""修复「加粗收尾紧贴中文标点、其后又是非标点非空白」导致整对 ** 失效的问题。

判据与 marked（CommonMark）一致：delimiter run 是否 right-flanking。
- 若 `**` 前是标点、后既不是空白也不是标点 → 该 run 不是 right-flanking → 加粗失效。
- 处置：句读类标点（。，、；：！？…·）移出加粗（更合中文排版）；成对符号则补一个空格。

标点定义 = ASCII 标点 ∪ Unicode P（标点）/ S（符号）类别 —— 与 marked 的 \\p{P}\\p{S} 对齐，
因此 `——`（Pd）、`-` 等**不会**被误判，避免无谓补空格。
"""
import io
import re
import sys
import unicodedata

ASCII_PUNCT = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
PUNC_MOVE = set('。，、；：！？…·')


def is_punct(ch):
    if not ch:
        return False
    if ch in ASCII_PUNCT:
        return True
    return unicodedata.category(ch)[0] in ('P', 'S')


def fix_line(line):
    changed = 0
    while True:
        pos = [m.start() for m in re.finditer(r'\*\*', line)]
        if len(pos) % 2:
            break
        target = None
        for k in range(len(pos) - 1, 0, -2):
            i = pos[k]
            prev = line[i - 1] if i > 0 else ''
            nxt = line[i + 2] if i + 2 < len(line) else ''
            if prev and is_punct(prev) and nxt and nxt.strip() and not is_punct(nxt):
                target = i
                break
        if target is None:
            break
        i = target
        j = i - 1
        while j >= 0 and is_punct(line[j]):
            j -= 1
        tail = line[j + 1:i]
        if tail and all(c in PUNC_MOVE for c in tail):
            line = line[:j + 1] + '**' + tail + line[i + 2:]
        else:
            line = line[:i + 2] + ' ' + line[i + 2:]
        changed += 1
    return line, changed


def run(path):
    s = io.open(path, encoding='utf-8').read()
    lines = s.split('\n')
    total = 0
    for idx, l in enumerate(lines):
        nl, c = fix_line(l)
        if c:
            lines[idx] = nl
            total += c
    io.open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    return total


if __name__ == '__main__':
    for p in sys.argv[1:]:
        n = run(p)
        print('%s  → 修复 %d 处' % (p.split('/')[-1], n))
