# -*- coding: utf-8 -*-
"""骄人板块「企业卡片」字段字数上限校验（体例见 06_jiaoren/README.md §收录字段）。

用法：  python check_card_length.py
退出码：0 = 全部合规；1 = 有超限/空值字段（列出明细）

体例（2026-09-24 起）：
  11 字段固定，各有字数上限；空值统一写 ——（未公开）/ ——（待核实）；
  时间敏感内容（管线进展 / 订单 / 最新获奖）不入卡片。
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CARD = os.path.join(ROOT, 'docs', '06_jiaoren', '企业卡片.md')

CAP = {
    '主营赛道': 40,
    '成立时间 · 总部': 45,
    '当前阶段': 70,
    '业务亮点': 60,
    '创始人 / 核心校友': 190,      # 单人 ≤120；多人合计 ≤190
    '核心产品 · 技术平台': 160,
    '业绩与资本': 150,
    '行业殊荣': 120,
    '关联学院': 30,
    '公开背书': 60,
    '数据来源': 80,
}
FIELD_RE = re.compile(r'^-\s+\*\*([^*]+?)\s*[：:]\s*\*\*\s*(.*)$')
HEAD_RE = re.compile(r'^###\s+\d+\.')


def visible(t):
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)   # 链接只计显示文字
    return len(re.sub(r'[*`>\s]', '', t))


def main():
    if not os.path.exists(CARD):
        print('未找到', CARD); return 1
    lines = io.open(CARD, encoding='utf-8').read().split('\n')
    heads = [i for i, l in enumerate(lines) if HEAD_RE.match(l)]
    # 每张卡的结束边界：下一张卡 / 下一个 `## ` 二级标题 / `---` 分隔线，取最近者
    bounds = []
    for k, i in enumerate(heads):
        stop = len(lines)
        for y in range(i + 1, len(lines)):
            if (HEAD_RE.match(lines[y]) or lines[y].startswith('## ')
                    or lines[y].startswith('> ') or lines[y].strip() == '---'):
                stop = y
                break
        bounds.append(stop)
    problems = []

    for k, i in enumerate(heads):
        j = bounds[k]
        name = re.sub(r'^###\s+\d+\.\s*', '', lines[i])
        seen = []
        for x in range(i + 1, j):
            m = FIELD_RE.match(lines[x])
            if not m:
                continue
            f = m.group(1).strip()
            seen.append(f)
            body = [m.group(2)]
            y = x + 1
            while y < j and not FIELD_RE.match(lines[y]) and not lines[y].startswith('#'):
                body.append(lines[y]); y += 1
            n = visible('\n'.join(body).strip())
            if f not in CAP:
                problems.append((name, f, n, '未知字段名'))
            elif n == 0:
                problems.append((name, f, n, '空值未按规范填写'))
            elif n > CAP[f]:
                problems.append((name, f, n, f'超上限 {CAP[f]}'))
        missing = [f for f in CAP if f not in seen]
        if missing:
            problems.append((name, '—', 0, '缺字段：' + ' / '.join(missing)))

    print('=' * 62)
    print('骄人企业卡片 · 字段上限校验  ·  %s' % os.path.basename(CARD))
    print('=' * 62)
    print('卡片数 : %d  ｜ 字段块 : %d（应 %d）' %
          (len(heads), sum(len(re.findall(FIELD_RE, l)) for l in lines), len(heads) * 11))
    if not problems:
        print('[PASS] 全部字段在字数上限内，无缺失字段。')
        return 0
    print('[FAIL] %d 处问题：\n' % len(problems))
    for name, f, n, why in problems:
        print('  ! %-22s %-18s %4d 字  %s' % (name[:22], f, n, why))
    return 1


if __name__ == '__main__':
    sys.exit(main())
