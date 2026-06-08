---
title: "这是发布文章的第一次测试"
date: 2026-04-04T10:00:00+08:00
draft: false
categories:
  - 成长碎碎念
tags:
  - 标签1
  - 标签2
description: "文章简介，会显示在列表页"
---
# Xcarus茶思屋 - 博客使用指南

## 📁 项目结构

```
xcarus-blog/
├── content/              # 博客文章存放目录
│   ├── posts/           # 文章目录（每篇文章一个子文件夹）
│   ├── categories/      # 专栏分类页面
│   ├── about.md         # 关于页面
│   ├── message.md       # 留言墙页面
│   ├── search.md        # 搜索页面
│   └── archives.md      # 归档页面
├── static/              # 静态资源
│   └── hero-wallpapers/ # 首页背景壁纸（自动轮播）
├── assets/              # 主题资源
│   ├── css/extended/    # 自定义样式（dream.css）
│   └── js/              # 自定义脚本（stars.js）
├── layouts/             # 页面模板（覆盖 PaperMod 主题）
│   ├── index.html       # 首页模板
│   ├── _default/        # 默认模板
│   └── partials/        # 可复用组件
├── themes/PaperMod/     # PaperMod 主题（Git 子模块）
├── hugo.yaml            # 博客配置文件
├── package.json         # Node.js 脚本
└── .github/workflows/   # GitHub Actions 自动部署
```

## 📝 如何发布文章

### 1. 使用 Hugo 命令创建文章

```bash
# 在项目根目录执行
hugo new posts/文章目录名/index.md
```

这会自动使用 `archetypes/default.md` 模板创建文章。

### 2. 文章头部格式（Front Matter）

每篇文章开头必须包含以下信息：

```yaml
---
title: "文章标题"
date: 2026-04-04T10:00:00+08:00
draft: false
categories:
  - 成长碎碎念
tags:
  - 标签1
  - 标签2
description: "文章简介，会显示在列表页"
---
```

**重要**：发布前确保 `draft: false`，否则文章不会出现在网站上。

### 3. 可用分类

当前有以下专栏分类（在 `content/categories/` 目录中定义）：

| 分类 | 说明 |
|------|------|
| `成长碎碎念` | 个人成长、思考感悟 |
| `物理与科学` | 科学知识、物理相关 |
| `电脑与软件` | 技术、软件、编程 |
| `阅读与思考` | 读书笔记、书评 |
| `游戏与娱乐` | 游戏、娱乐内容 |
| `高考备考` | 高考复习、学习方法 |
| `AI与思想` | 人工智能、科技思考 |
| `人物与社会` | 人物评述、社会观察 |

### 4. Markdown 语法支持

```markdown
# 一级标题
## 二级标题
### 三级标题

**粗体** *斜体* ~~删除线~~

- 无序列表
- 列表项

1. 有序列表
2. 列表项

> 引用文字

`行内代码`

```python
# 代码块（支持语法高亮）
print("Hello World")
```

[链接](https://example.com)
![图片](/images/pic.jpg)

| 表格 | 表头 |
|------|------|
| 内容 | 内容 |
```

**LaTeX 公式支持**：

```latex
行内公式：$E = mc^2$

块级公式：
$$
F = q(E + v \times B)
$$
```

## 🖥️ 本地预览

```bash
# 进入博客目录
cd xcarus-blog

# 方式一：使用 npm（推荐）
npm run dev

# 方式二：直接使用 Hugo
hugo server -D

# 访问 http://localhost:1313 预览
```

## 🚀 发布到网站

```bash
# 1. 确保文章 draft: false
# 2. 提交到 GitHub
git add .
git commit -m "新增文章：文章标题"
git push origin main

# GitHub Actions 会自动部署到 GitHub Pages
# 约 2-3 分钟后访问 https://alexerrorx.github.io/
```

也可以在 GitHub 仓库页面手动触发部署：`Actions → Deploy Hugo site → Run workflow`

## 🎨 自定义设置

### 修改网站配置

编辑 `hugo.yaml` 文件：

```yaml
title: "Xcarus茶思屋"          # 网站标题
params:
  description: "个人博客描述"     # 网站描述
  author: "ErrorX"               # 作者名
  walineServerURL: "..."         # Waline 评论服务器
  umamiWebsiteId: "..."          # Umami 统计 ID（可选）
```

### 更换首页壁纸

将图片放入 `static/hero-wallpapers/` 目录即可，系统会自动扫描并轮播（每 20 分钟切换一张）。

支持的格式：`.jpg`、`.jpeg`、`.png`、`.webp`

### 修改主题样式

编辑 `assets/css/extended/dream.css` 文件。

主题色板：
- 星空蓝：`#165DFF`
- 星云紫：`#7B61FF`
- 深空黑：`#0F172A`
- 星光白：`#F1F5F9`

## 🔧 第三方服务配置

### Waline 评论

评论系统使用 Waline，已配置在 `hugo.yaml` 中：

```yaml
params:
  walineServerURL: "https://xcarus-waline.vercel.app"
```

### Umami 访问统计

如需启用 Umami 统计，在 `hugo.yaml` 中配置：

```yaml
params:
  umamiWebsiteId: "你的 Website ID"
  umamiScriptUrl: "https://analytics.umami.is/script.js"
```

不配置则不会加载任何追踪脚本。

### GitHub Actions 自动部署

配置文件位于 `.github/workflows/deploy.yml`，推送 `main` 分支时自动触发。

要求：GitHub 仓库的 Settings → Pages → Source 设为 "GitHub Actions"。

## 🐛 常见问题

**Q: 文章不显示？**
A: 检查 `draft: false`，草稿文章在正式环境中不会显示。本地预览时加 `-D` 参数可查看草稿。

**Q: 分类不生效？**
A: 确保分类名称和 `content/categories/` 目录中定义的完全一致。分类名区分中英文。

**Q: 图片不显示？**
A: 图片放在 `static/` 目录下，引用路径以 `/` 开头。例如 `static/images/pic.jpg` → `![alt](/images/pic.jpg)`。

**Q: 如何添加新分类？**
A: 在 `content/categories/` 下创建新文件夹并添加 `index.md`，然后在文章 front matter 中使用该分类名。

## 📞 需要帮助？

- Hugo 官方文档：https://gohugo.io/documentation/
- PaperMod 主题文档：https://github.com/adityatelange/hugo-PaperMod/wiki
- Markdown 语法：https://www.markdownguide.org/
