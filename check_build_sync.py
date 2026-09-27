# -*- coding: utf-8 -*-
"""
双入口 BUILD 同步闸门 —— 「发布前必跑」。

背景：站点有两个入口，共用同一套 md：
    docs/index.html   —— 主入口（内部版，显示「工作流驾驶舱」）
    docs/alumni.html  —— 校友版（隐去驾驶舱）
两者各自内联了一份 `var BUILD`，用于给 XHR 取 .md 时破缓存。**只要有一个没跟着升，
该入口就会命中托管层的旧缓存、继续显示上一版内容**（2026-09-27 新增本闸门）。

用法：
    python check_build_sync.py      # 0 = 两入口一致；1 = 不一致，先改再发
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
ENTRIES = ["index.html", "alumni.html"]
PAT = re.compile(r"var BUILD = '([^']*)'")


def read(p):
    return io.open(p, encoding="utf-8", errors="ignore").read()


def main():
    print("=" * 66)
    print("双入口 BUILD 同步闸门  ·  index.html / alumni.html")
    print("=" * 66)

    found = {}
    for name in ENTRIES:
        p = os.path.join(DOCS, name)
        if not os.path.exists(p):
            print("[!!] 缺少入口文件：docs/%s" % name)
            return 1
        hits = PAT.findall(read(p))
        if len(hits) != 1:
            print("[!!] docs/%s 中 `var BUILD` 命中 %d 处（应为 1 处）" % (name, len(hits)))
            return 1
        found[name] = hits[0]
        print("  %-14s BUILD = %s" % (name, hits[0]))

    vals = set(found.values())
    if len(vals) != 1:
        print("\n[!!] 两入口 BUILD 不一致，禁止发布：%s" % found)
        print("处理：把 docs/index.html 与 docs/alumni.html 的 var BUILD 改成同一个新值，再重跑本脚本。")
        return 1

    print("\n[PASS] 双入口 BUILD 一致（%s）。" % found["index.html"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
