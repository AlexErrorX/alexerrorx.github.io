# Xcarus茶思屋 · 发布 SOP

## 三步上线

```
① 写 .md（不用写头文件）
② 丢进 _drafts/
③ 双击 发布.bat 或运行 python publish.py
```

没了。等 2 分钟刷新 https://alexerrorx.github.io/ 就能看到。

---

## 示例

```
_drafts/带电粒子运动.md       ← 随便写的 .md
        ↓
python publish.py              ← 一键：自动加头文件 → 构建 → git push
        ↓
2 分钟后 https://alexerrorx.github.io/ 上线
```

---

## 本地预览

```bash
hugo server -D -p 1313
```

---

## 还有问题？

打开 `PUBLISH.md` 看详细版，或者直接问我。
