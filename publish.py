#!/usr/bin/env python3
"""
Xcarus茶思屋 - 一键发布工具
Usage: python publish.py

Put your .md files in _drafts/ → run this → DONE online in 2 min.
把写好的 .md 丢进 _drafts/ → 运行本脚本 → 搞定，2 分钟后上线。
"""

import os, re, sys, subprocess
from datetime import datetime
from pathlib import Path

# ====== Config ======
PROJECT_ROOT = Path(__file__).parent.resolve()
DRAFTS_DIR = PROJECT_ROOT / "_drafts"
POSTS_DIR = PROJECT_ROOT / "content" / "posts"
DEFAULT_CATEGORY = "成长碎碎念"

CATEGORIES = [
    "成长碎碎念", "物理与科学", "电脑与软件",
    "阅读与思考", "游戏与娱乐", "高考备考与学习",
    "AI与思想", "人物与社会"
]

# ====== Helpers ======

def run(cmd, cwd=None):
    """Run a shell command, print output"""
    result = subprocess.run(cmd, shell=True, cwd=cwd or PROJECT_ROOT,
                           capture_output=True, text=True)
    if result.returncode != 0 and result.stderr:
        print(f"   ⚠️  {result.stderr.strip()[:200]}")
    return result.returncode == 0

def extract_title(content):
    for line in content.split("\n"):
        if line.strip().startswith("# ") and not line.strip().startswith("## "):
            return line.strip()[2:]
    return "未命名"

def extract_description(content):
    lines = content.split("\n")
    started, parts = False, []
    for line in lines:
        s = line.strip()
        if not s:
            if started: break
            continue
        if s.startswith("#"): started = True; continue
        if started: parts.append(s)
    desc = " ".join(parts)[:150]
    return desc or "暂无简介"

def guess_category(text):
    text = text.lower()
    for kw, cat in [("物理","物理与科学"),("科学","物理与科学"),
                    ("数学","高考备考与学习"),("高考","高考备考与学习"),
                    ("备考","高考备考与学习"),("ai","AI与思想"),
                    ("思考","AI与思想"),("人工智能","AI与思想"),
                    ("编程","电脑与软件"),("电脑","电脑与软件"),
                    ("游戏","游戏与娱乐"),("阅读","阅读与思考"),
                    ("人物","人物与社会"),("成长","成长碎碎念")]:
        if kw in text: return cat
    return DEFAULT_CATEGORY

def slugify(text):
    return re.sub(r'[^\w\s-]', '', text.strip().lower())\
             .replace(' ', '-').replace('--','-')[:50]

# ====== Core ======

def publish():
    drafts = list(DRAFTS_DIR.glob("*.md"))
    if not drafts:
        print("⚠️  _drafts/ 为空，没东西发布。把 .md 放进去再试。")
        return False

    titles = []
    for draft in drafts:
        raw = draft.read_text(encoding="utf-8")
        title = extract_title(raw)
        slug = slugify(title) or draft.stem
        desc = extract_description(raw)
        cat = guess_category(title + "\n" + raw[:500])
        date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")

        fm = f"""---
title: "{title}"
date: {date}
draft: false
categories:
  - {cat}
tags:
  - 未分类
description: "{desc}"
---

"""
        bundle = POSTS_DIR / slug
        bundle.mkdir(parents=True, exist_ok=True)
        (bundle / "index.md").write_text(fm + raw, encoding="utf-8")
        titles.append(title)
        print(f"   ✅ {title} → posts/{slug}/")

    # Build
    print("\n🔨 构建检查...")
    if not run("hugo --minify"):
        print("❌ 构建失败，请检查错误。")
        return False

    # Git
    commit_msg = "发布: " + " | ".join(titles)
    print(f"\n📤 提交: {commit_msg}")
    run("git add content/posts/")
    run(f'git commit -m "{commit_msg}"')
    run("git push origin main")

    print(f"\n🎉 搞定！{len(titles)} 篇文章已发布，2 分钟后刷新 https://alexerrorx.github.io/")
    return True

# ====== Main ======

if __name__ == "__main__":
    print("=" * 44)
    print("  Xcarus茶思屋 · 一键发布")
    print("=" * 44)
    publish()
