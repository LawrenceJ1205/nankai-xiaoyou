import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fix_bold_tail import fix_line

root = sys.argv[1] if len(sys.argv) > 1 else 'docs'
rows = []
for dp, dn, fn in os.walk(root):
    if 'vendor' in dp or '_probe' in dp or '.git' in dp:
        continue
    for f in sorted(fn):
        if not f.endswith('.md'):
            continue
        p = os.path.join(dp, f)
        s = io.open(p, encoding='utf-8').read()
        n = 0
        for l in s.split('\n'):
            _, c = fix_line(l)
            n += c
        if n:
            rows.append((n, p))

rows.sort(reverse=True)
print('共有问题的 md：%d 个，合计 %d 处' % (len(rows), sum(r[0] for r in rows)))
for n, p in rows:
    print('  %4d  %s' % (n, p.replace('\\', '/')))
