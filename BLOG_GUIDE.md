# Xcarus茶思屋 - 博客使用指南

## 📁 项目结构

```
xcarus-blog/
├── content/              # 博客文章存放目录
│   ├── posts/           # 文章目录
│   └── about.md         # 关于页面
├── static/              # 静态资源
│   ├── hero-wallpapers/ # 首页背景壁纸
│   └── images/          # 文章图片
├── assets/              # 主题资源
│   └── css/             # 自定义样式
├── layouts/             # 页面模板
├── config.yml           # 博客配置
└── themes/              # 主题目录
```

## 📝 如何发布文章

### 1. 创建文章文件

在 `content/posts/` 目录下创建 `.md` 文件：

```bash
# 文件名格式：YYYY-MM-DD-文章标题.md
# 例如：
2026-04-04-我的第一篇博客.md
```

### 2. 文章头部格式（Front Matter）

每篇文章开头必须包含以下信息：

```markdown
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

# 正文开始

这里是文章内容，支持 Markdown 语法。

## 二级标题

- 列表项1
- 列表项2

**粗体文字** *斜体文字*

[链接文字](https://example.com)

![图片描述](/images/图片名.jpg)
```

### 3. 可用分类

目前设置了以下专栏分类：

- `成长碎碎念` - 个人成长、思考感悟
- `物理与科学` - 科学知识、物理相关
- `电脑与软件` - 技术、软件、编程
- `阅读与思考` - 读书笔记、书评
- `游戏与娱乐` - 游戏、娱乐内容
- `生活点滴` - 日常生活记录
- `音乐与艺术` - 音乐、艺术相关
- `社会观察` - 社会现象观察

### 4. Markdown 语法支持

```markdown
# 一级标题
## 二级标题
### 三级标题

**粗体** *斜体* ~~删除线~~

- 无序列表
- 列表项
  - 子列表

1. 有序列表
2. 列表项

> 引用文字

`行内代码`

```python
# 代码块
print("Hello World")
```

[链接](https://example.com)
![图片](/images/pic.jpg)

| 表格 | 表头 |
|------|------|
| 内容 | 内容 |
```

### 5. 本地预览

```bash
# 进入博客目录
cd xcarus-blog

# 启动本地服务器
hugo server -D

# 访问 http://localhost:1313 预览
```

### 6. 发布到网站

```bash
# 1. 保存文章
# 2. 提交到 GitHub
git add .
git commit -m "新增文章：文章标题"
git push origin main

# GitHub Actions 会自动部署到网站
# 约 2-3 分钟后访问 https://alexerrorx.github.io/
```

## 🎨 自定义设置

### 修改网站配置

编辑 `config.yml` 文件：

```yaml
title: "Xcarus茶思屋"          # 网站标题
description: "个人博客描述"     # 网站描述
author: "ErrorX"               # 作者名
```

### 更换首页壁纸

将图片放入 `static/hero-wallpapers/` 目录，支持自动轮播。

### 修改主题样式

编辑 `assets/css/extended/dream.css` 文件。

## 🐛 常见问题

**Q: 文章不显示？**
A: 检查 `draft: false`，草稿不会显示。

**Q: 分类不生效？**
A: 确保分类名称和 `config.yml` 中定义的完全一致。

**Q: 图片不显示？**
A: 图片放在 `static/images/` 目录，引用路径以 `/images/` 开头。

**Q: 如何添加新分类？**
A: 在 `config.yml` 的 `params.categories` 中添加，然后创建对应分类的文章。

## 📞 需要帮助？

- Hugo 官方文档：https://gohugo.io/documentation/
- Markdown 语法：https://www.markdownguide.org/
