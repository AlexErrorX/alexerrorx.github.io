---
title: "留言墙"
date: 2026-04-04
draft: false
---

## 💬 欢迎留言

这里是留言墙，你可以在这里：
- 留下你的想法和建议
- 提出问题或讨论
- 随便聊聊

---

<div id="waline-comment"></div>

<script type="module">
  import { init } from 'https://unpkg.com/@waline/client@v3/dist/waline.js';
  init({
    el: '#waline-comment',
    serverURL: 'https://xcarus-waline.vercel.app',
    dark: 'auto',
    lang: 'zh-CN',
    placeholder: '欢迎留下你的想法...',
    pageview: true,
    comment: true,
  });
</script>
