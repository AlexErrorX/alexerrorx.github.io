# 🏠 Xcarus Tea House · Xcarus茶思屋

<p align="center">
  <img src="https://img.shields.io/badge/Hugo-0.146+-FF4088?style=flat&logo=hugo&logoColor=white" alt="Hugo">
  <img src="https://img.shields.io/badge/Theme-Stellar%20Dreamland-blueviolet?style=flat" alt="Theme">
  <img src="https://img.shields.io/badge/Deploy-GitHub%20Pages-222?style=flat&logo=github" alt="GitHub Pages">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License">
</p>

<p align="center">
  <b>Make time for civilization, for civilization won't make time.</b><br>
  <i>给岁月以文明，而不是给文明以岁月。</i>
</p>

---

## 📖 About

**Xcarus Tea House** is the personal blog of **ErrorX** — a high school student passionate about physics, programming, AI, and deep thinking. The name is a blend of **星辰 (stars)** and **茶思 (tea & contemplation)** — a quiet space to think clearly amid a universe of ideas.

> 🀄 高中生 ErrorX 的个人博客。名字融合「星辰」与「茶思」，在浩瀚星空中静心思考。

---

## 🎨 Design — Stellar Dreamland · 星穹梦境

A custom dark sci-fi theme built on Hugo PaperMod.

| Feature | Description · 说明 |
|---------|------|
| 🌌 Aurora Background | Floating gradient blobs with 25s animation · 极光浮动背景 |
| 🖼️ Wallpaper Slideshow | Auto-rotates every 20 minutes from `static/hero-wallpapers/` · 壁纸自动轮播 |
| ⌨️ Typewriter Effect | Quotes from *The Three-Body Problem* · 三体名言打字机效果 |
| 📱 iPhone-style Scroll | Parallax unlock effect · iPhone 解锁式滚动视差 |
| 🪟 Glassmorphism | Single-layer frosted glass for performance · 单层毛玻璃 |
| 🎵 Music Player | APlayer + NetEase playlist · 网易云音乐播放器 |
| 🌙 Dark Mode | Default dark, toggle available · 默认深色模式 |

**Color Palette · 色板：**

| Name | Hex | Usage · 用途 |
|------|-----|-------|
| Starry Blue · 星空蓝 | `#165DFF` | Primary accent · 主强调色 |
| Nebula Purple · 星云紫 | `#7B61FF` | Secondary accent · 次强调色 |
| Deep Space · 深空黑 | `#0F172A` | Background · 背景 |
| Aurora Cyan · 极光青 | `#00D4FF` | Highlights · 高亮 |
| Starlight · 星光白 | `#F1F5F9` | Text · 文字 |

---

## 📂 Project Structure · 项目结构

```
xcarus-blog/
├── _drafts/                  📝 Drop .md drafts here · 草稿放这里
├── content/
│   ├── posts/                📄 Blog posts (Hugo Page Bundles) · 文章
│   ├── about.md              👤 About page · 关于页面
│   ├── message.md            💬 Guestbook · 留言墙
│   └── thinking-journey.md   🧠 Thinking archive · 思维成长档案
├── assets/
│   ├── css/extended/dream.css    🎨 Core styles (1400+ lines) · 核心样式
│   └── js/stars.js               ✨ Canvas starfield · Canvas 星空
├── layouts/                  🧩 Custom templates · 自定义模板
├── static/hero-wallpapers/   🖼️ Homepage backgrounds · 首页壁纸
├── themes/PaperMod/          📦 Hugo PaperMod theme (submodule)
├── publish.py                🚀 One-click publish tool · 一键发布
├── hugo.yaml                 ⚙️ Site config · 站点配置
└── README.md                 📖 You are here · 你在这里
```

---

## 🚀 Quick Start · 快速开始

### Prerequisites · 前置条件

- [Hugo](https://gohugo.io/installation/) v0.146+ Extended
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/) 3.7+ (for `publish.py` · 发布工具需要)

### Local Dev · 本地开发

```bash
# Clone with submodules · 克隆仓库（含子模块）
git clone --recursive https://github.com/AlexErrorX/alexerrorx.github.io.git
cd alexerrorx.github.io

# Start dev server on port 1313 · 启动开发服务器
hugo server -D -p 1313

# Or use npm · 或使用 npm
npm run dev
```

Open `http://localhost:1313` · 浏览器打开即可预览。

### Pushing to Production · 推送到线上

```bash
git add .
git commit -m "Update"     # 提交
git push origin main        # 推送到 GitHub（自动部署）
```

---

## ✍️ Publishing Workflow · 发布流程

### The Easy Way · 推荐方式

Write your article as a `.md` file — **no front matter needed** · 无需手写头文件。

1. Drop the `.md` into `_drafts/` · 把 .md 放进 _drafts 目录
2. Run:
```bash
python publish.py           # Auto-generates front matter & page bundle
                             # 自动生成头文件 + 创建文章目录
```
3. Push:
```bash
git add . && git commit -m "New post" && git push origin main
```

The tool automatically · 工具自动完成：
- Extracts title from the first `# Heading` · 提取标题
- Guesses category based on content · 匹配分类
- Extracts keywords as tags · 生成标签
- Generates description from first paragraph · 生成摘要

### The Manual Way · 手动方式

```bash
hugo new posts/my-post/index.md
# Edit the file, set draft: false
git push origin main
```

---

## 📊 Categories · 文章分类

| Category · 分类 | Description |
|:--|:--|
| 🔬 Physics & Science · 物理与科学 | Physics, astronomy, scientific thinking |
| 📚 Exam Prep & Learning · 高考备考与学习 | Study strategies, math, Gaokao prep |
| 🤖 AI & Thinking · AI与思想 | Artificial intelligence, deep reflection |
| 💻 Tech & Software · 电脑与软件 | Programming, tools, hardware |
| 📖 Reading & Reflection · 阅读与思考 | Book notes, abstract thinking |
| 🎮 Games & Entertainment · 游戏与娱乐 | Gaming, anime, pop culture |
| 👤 People & Society · 人物与社会 | Biographies, social observations |
| 🌱 Personal Growth · 成长碎碎念 | Life reflections, self-improvement |

---

## 🛠️ Tech Stack · 技术栈

| Layer · 层级 | Technology |
|:--|:--|
| SSG · 静态生成 | [Hugo](https://gohugo.io/) v0.146+ |
| Base Theme · 基础主题 | [PaperMod](https://github.com/adityatelange/hugo-PaperMod) |
| Custom Theme · 自定义主题 | Stellar Dreamland · 星穹梦境 |
| Hosting · 托管 | [GitHub Pages](https://pages.github.com/) |
| CI/CD · 自动部署 | [GitHub Actions](.github/workflows/deploy.yml) |
| Comments · 评论 | Waline / Giscus ready |
| Analytics · 统计 | Umami ready |
| Search · 搜索 | [Fuse.js](https://www.fusejs.io/) client-side |
| Music · 音乐 | [APlayer](https://aplayer.js.org/) + NetEase |
| Font · 字体 | Noto Serif SC · 思源宋体 |

---

## 📝 License · 许可

Content © ErrorX. All rights reserved. Code under [MIT License](LICENSE).

> 🀄 博客内容版权归 ErrorX 所有。代码采用 MIT 协议开源。

---

## 🔗 Links · 链接

- 🌐 **Live Site** · 线上：[alexerrorx.github.io](https://alexerrorx.github.io/)
- 👤 **Author** · 作者：[AlexErrorX](https://github.com/AlexErrorX)

---

<p align="center">
  <i>"Weakness and ignorance are not barriers to survival, but arrogance is."</i><br>
  <i>— The Three-Body Problem · 《三体》</i><br><br>
  <b>弱小和无知不是生存的障碍，傲慢才是。</b>
</p>
