#!/usr/bin/env python3
"""
Xcarus茶思屋 - 一键发布工具
用法: python publish.py
将 _drafts/ 目录下的 .md 文件自动转换为 Hugo 文章并发布
"""

import os
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# ========== 配置区 ==========
PROJECT_ROOT = Path(__file__).parent.resolve()
DRAFTS_DIR = PROJECT_ROOT / "_drafts"
POSTS_DIR = PROJECT_ROOT / "content" / "posts"

# 默认设置
DEFAULT_CATEGORY = "成长碎碎念"
DEFAULT_DESCRIPTION_LENGTH = 150

# 可用分类
CATEGORIES = [
    "成长碎碎念", "物理与科学", "电脑与软件",
    "阅读与思考", "游戏与娱乐", "高考备考与学习",
    "AI与思想", "人物与社会"
]

# ========== 工具函数 ==========

def slugify(text):
    """中文转拼音简写或保留英文"""
    # 简单处理：去除非字母数字汉字字符，保留英文和数字
    text = text.strip().lower()
    # 中英文混合时用拼音或保留
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:50]


def extract_title(content):
    """从 Markdown 内容中提取标题（第一个 # 标题）"""
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return "未命名文章"


def extract_description(content, max_len=150):
    """提取文章摘要（第一段非标题文字）"""
    lines = content.split("\n")
    text_lines = []
    started = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if started:
                break
            continue
        if stripped.startswith("#"):
            started = True
            continue
        if started and stripped:
            text_lines.append(stripped)
            if len("".join(text_lines)) > max_len:
                break
    desc = " ".join(text_lines).strip()
    if len(desc) > max_len:
        desc = desc[:max_len-3] + "..."
    return desc or "暂无简介"


def extract_tags(content):
    """简单提取可能的标签（从内容中的关键词）"""
    tags = set()
    content_lower = content.lower()
    keywords = {
        "物理": "物理", "数学": "数学", "化学": "化学",
        "ai": "AI", "人工智能": "AI", "机器学习": "AI",
        "高考": "高考", "备考": "高考备考", "学习": "学习方法",
        "python": "Python", "编程": "编程", "算法": "算法",
        "阅读": "阅读", "思考": "深度思考",
        "游戏": "游戏", "科幻": "科幻",
    }
    for key, tag in keywords.items():
        if key.lower() in content_lower:
            tags.add(tag)
    return list(tags)


def guess_category(content, filename=""):
    """根据内容和文件名猜测分类"""
    text = (filename + " " + content[:500]).lower()
    guess_map = {
        "物理": "物理与科学", "科学": "物理与科学",
        "数学": "高考备考与学习", "高考": "高考备考与学习",
        "备考": "高考备考与学习", "学习": "高考备考与学习",
        "ai": "AI与思想", "人工智能": "AI与思想", "思考": "AI与思想",
        "电脑": "电脑与软件", "软件": "电脑与软件", "编程": "电脑与软件",
        "游戏": "游戏与娱乐", "娱乐": "游戏与娱乐",
        "阅读": "阅读与思考", "读书": "阅读与思考",
        "人物": "人物与社会", "社会": "人物与社会",
        "成长": "成长碎碎念", "生活": "成长碎碎念",
    }
    for key, cat in guess_map.items():
        if key in text:
            return cat
    return DEFAULT_CATEGORY


def add_frontmatter(title, content, category=None, tags=None, description=None, date=None):
    """为 Markdown 内容添加 Hugo Front Matter"""
    if category is None:
        category = guess_category(content, title)
    if tags is None:
        tags = extract_tags(content)
    if description is None:
        description = extract_description(content)
    if date is None:
        date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")

    tags_yaml = "\n".join([f"  - {t}" for t in tags]) if tags else "  - 未分类"

    frontmatter = f"""---
title: "{title}"
date: {date}
draft: false
categories:
  - {category}
tags:
{tags_yaml}
description: "{description}"
---

"""
    return frontmatter + content


def publish_one(filepath):
    """发布单个 .md 文件"""
    filename = filepath.name
    if not filename.endswith(".md"):
        return False, "不是 .md 文件"

    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    # 跳过已有 front matter 的文件
    if raw.strip().startswith("---"):
        title = extract_title(raw)
    else:
        title = extract_title(raw)

    slug = slugify(title) or filename.replace(".md", "")
    content = add_frontmatter(title, raw)

    # 创建 Hugo Page Bundle
    bundle_dir = POSTS_DIR / slug
    bundle_dir.mkdir(parents=True, exist_ok=True)

    index_path = bundle_dir / "index.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

    return True, f"✅ {title} → content/posts/{slug}/index.md"


def build_site():
    """构建站点"""
    print("\n🔨 构建中...")
    result = subprocess.run(
        ["hugo", "--minify"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("✅ 构建成功")
        return True
    else:
        print(f"❌ 构建失败:\n{result.stderr}")
        return False


def main():
    print("=" * 50)
    print("  Xcarus茶思屋 - 文章发布工具")
    print("=" * 50)

    # 确保 _drafts 目录存在
    DRAFTS_DIR.mkdir(exist_ok=True)
    print(f"\n📂 草稿目录: {DRAFTS_DIR}")
    print(f"📂 文章目录: {POSTS_DIR}")
    print(f"\n📝 支持格式: .md 文件（无需手写头文件）")
    print(f"📝 可用分类: {', '.join(CATEGORIES)}")
    print(f"\n用法: 把写好的 .md 文件放进 _drafts/ 目录，然后运行本脚本")

    # 扫描草稿
    drafts = list(DRAFTS_DIR.glob("*.md"))
    if not drafts:
        print("\n⚠️  _drafts/ 目录为空，没有文章需要发布。")
        print("   把 .md 文件放进 _drafts/ 目录后再运行。")
        return

    print(f"\n📋 发现 {len(drafts)} 篇草稿:")
    for d in drafts:
        print(f"   - {d.name}")

    print("\n" + "-" * 50)

    # 逐篇发布
    success = 0
    for draft in drafts:
        ok, msg = publish_one(draft)
        print(f"   {msg}")
        if ok:
            success += 1

    if success == 0:
        print("\n⚠️  没有文章被发布。")
        return

    print(f"\n✅ 成功发布 {success}/{len(drafts)} 篇")

    # 询问是否构建
    print("\n" + "=" * 50)
    print("下一步操作:")
    print("  1. 本地预览:  hugo server -D")
    print("  2. 推送上线:  git add . && git commit -m '发布新文章' && git push")
    print("=" * 50)


if __name__ == "__main__":
    main()
