import io, os, sys

before_root = sys.argv[1]
after_root = sys.argv[2]

def norm(s):
    # 去掉全部空白，再看去掉 ** 后的正文是否一致（证明只动了位置/空格，未增删文字）
    s = ''.join(s.split())
    return s.replace('**', '')

bad, checked = [], 0
for dp, dn, fn in os.walk(after_root):
    if 'vendor' in dp or '_probe' in dp or '.git' in dp:
        continue
    for f in sorted(fn):
        if not f.endswith('.md'):
            continue
        pa = os.path.join(dp, f)
        rel = os.path.relpath(pa, after_root)
        pb = os.path.join(before_root, rel)
        if not os.path.exists(pb):
            bad.append(('新增文件（无备份对照）', rel))
            continue
        a = norm(io.open(pa, encoding='utf-8').read())
        b = norm(io.open(pb, encoding='utf-8').read())
        checked += 1
        if a != b:
            bad.append(('内容有变', rel))

print('比对文件：%d ｜ 正文不一致：%d' % (checked, len(bad)))
for kind, rel in bad:
    print('  %s  %s' % (kind, rel))

# 再报告有变化的文件清单
changed = []
for dp, dn, fn in os.walk(after_root):
    if 'vendor' in dp or '_probe' in dp or '.git' in dp:
        continue
    for f in sorted(fn):
        if not f.endswith('.md'):
            continue
        pa = os.path.join(dp, f)
        rel = os.path.relpath(pa, after_root)
        pb = os.path.join(before_root, rel)
        if os.path.exists(pb) and io.open(pa, encoding='utf-8').read() != io.open(pb, encoding='utf-8').read():
            changed.append(rel)
print('\n实际被改动的文件（%d 个）：' % len(changed))
for c in changed:
    print('  ' + c)
