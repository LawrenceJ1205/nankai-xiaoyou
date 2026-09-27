# -*- coding: utf-8 -*-
"""校友版显隐核验：解析无头渲染的 DOM，按 display:none 剪枝后取「可见文本」。

用法（先无头渲染，再核验；配合六步发布的第 ⑤ 步线上实测）：
    msedge --headless --dump-dom "https://<站点>/alumni.html?v=<BUILD>" > _probe/dom.html
    python check_alumni_dom.py _probe/dom.html [额外禁止词...]
输出：可见正文 / 可见侧边栏 的长度与关键词命中情况；命中即退出码 1。
说明：按 display:none 剪枝后取「可见文本」，专门用于核验校友版（alumni.html）
      是否还残留内部内容（工作流驾驶舱 / 00_cockpit 等）。
"""
import io
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Visible(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = []          # 每层：True=可见
        self.text = []           # 可见文本
        self.hidden_tags = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        attrs = dict(attrs)
        style = (attrs.get("style") or "").replace(" ", "")
        hidden = "display:none" in style or "visibility:hidden" in style
        parent_ok = self.stack[-1] if self.stack else True
        self.stack.append(parent_ok and not hidden)
        if hidden:
            self.hidden_tags.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if all(self.stack):
            t = data.strip()
            if t:
                self.text.append(t)


def visible_text(html):
    p = Visible()
    p.feed(html)
    return " ".join(p.text), p.hidden_tags


def section(dom, attr, value):
    """按 class 属性取出第一个区块的原始 HTML（粗略但够用：找配对标签）。"""
    m = re.search(r'<%s[^>]*%s="[^"]*\b%s\b[^"]*"[^>]*>' % (attr[0], attr[1], value), dom)
    if not m:
        return ""
    tag = attr[0]
    i = m.end()
    depth = 1
    pat = re.compile(r"</?%s\b[^>]*>" % tag)
    for mm in pat.finditer(dom, i):
        if mm.group(0).startswith("</"):
            depth -= 1
            if depth == 0:
                return dom[i:mm.start()]
        else:
            depth += 1
    return dom[i:]


def main():
    path = sys.argv[1]
    extra = sys.argv[2:]
    dom = io.open(path, encoding="utf-8", errors="ignore").read()

    art = section(dom, ("article", "class"), "markdown-section")
    side = section(dom, ("aside", "class"), "sidebar")

    at, ah = visible_text(art)
    st, sh = visible_text(side)

    print("=" * 62)
    print("校友版显隐核验 ·", path.split("/")[-1])
    print("=" * 62)
    print("可见正文长度 :", len(at))
    print("可见侧边栏长度:", len(st))
    print("被剪枝隐藏的元素:", len(ah))

    bad = []
    for kw in ["00_cockpit", "工作流驾驶舱", "见 ）", "见）", "（）"] + extra:
        n = at.count(kw) + st.count(kw)
        print("  关键词 %-14s 可见命中 %d" % (kw, n))
        if n:
            bad.append(kw)

    if bad:
        print("\n[!!] 仍有可见残留：", bad)
        for kw in bad:
            i = at.find(kw)
            if i > -1:
                print("    正文上下文:", at[max(0, i - 40):i + 40])
            i = st.find(kw)
            if i > -1:
                print("    侧栏上下文:", st[max(0, i - 40):i + 40])
        return 1

    print("\n[PASS] 可见区域无内部内容残留。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
