# 福库心理 APP - GitHub Pages 发布指南

## 📋 准备工作

### 第一步：在 GitHub 上创建仓库

1. **访问 GitHub**
   - 打开：https://github.com/jinfuku/new

2. **创建新仓库**
   - Repository name: `fuku-app`
   - Description: `福库心理 - 身心同调 APP`
   - Public/Private: 选择 **Public**（必须公开才能使用 GitHub Pages）
   - 勾选 "Add a README file"（可选）
   - 点击 **Create repository**

3. **记录仓库地址**
   - 仓库地址将是：https://github.com/jinfuku/fuku-app

### 第二步：配置 Git 远程仓库

创建仓库后，在本地执行以下命令：

```powershell
cd c:\Users\jinfu\WorkBuddy\Claw\fuku-app
git remote add origin https://github.com/jinfuku/fuku-app.git
git branch -M main
```

### 第三步：推送到 GitHub

```powershell
git push -u origin main
```

**注意：** 可能需要输入 GitHub 用户名和密码（或个人访问令牌）

## 🚀 部署到 GitHub Pages

### 方法一：使用 gh-pages 分支（推荐）

#### 1. 创建并推送 gh-pages 分支

```powershell
cd c:\Users\jinfu\WorkBuddy\Claw\fuku-app

# 创建 gh-pages 分支
git checkout --orphan gh-pages

# 清空当前目录
git rm -rf .

# 复制 index.html 到根目录
copy index.html index.html.bak
git checkout main -- index.html
del index.html.bak

# 添加并提交
git add .
git commit -m "Deploy to GitHub Pages"

# 推送到 GitHub
git push origin gh-pages
```

#### 2. 配置 GitHub Pages

1. 访问：https://github.com/jinfuku/fuku-app/settings/pages
2. 配置：
   - **Source:** Deploy from a branch
   - **Branch:** gh-pages
   - **Directory:** / (root)
3. 点击 **Save**

#### 3. 访问 APP

部署成功后，访问：
**https://jinfuku.github.io/fuku-app/**

### 方法二：使用 main 分支

如果您想使用 main 分支部署，更简单：

1. **直接推送 main 分支**

```powershell
cd c:\Users\jinfu\WorkBuddy\Claw\fuku-app
git push -u origin main
```

2. **配置 GitHub Pages**

   访问：https://github.com/jinfuku/fuku-app/settings/pages

   配置：
   - **Source:** Deploy from a branch
   - **Branch:** main
   - **Directory:** / (root)
   - 点击 **Save**

3. **访问 APP**

   **https://jinfuku.github.io/fuku-app/**

## 📱 在手机上使用

### 方法一：添加到主屏幕

1. **在手机浏览器中打开 APP**
   - 访问：https://jinfuku.github.io/fuku-app/

2. **添加到主屏幕**

   **Android (Chrome):**
   - 点击菜单按钮（三个点）
   - 选择 "添加到主屏幕" 或 "安装应用"
   - 确认安装

   **iPhone (Safari):**
   - 点击分享按钮（方框加箭头）
   - 滚动到底部，点击 "添加到主屏幕"
   - 点击 "添加"

3. **使用**
   - APP 图标会出现在主屏幕
   - 点击即可像原生 APP 一样使用

### 方法二：创建桌面快捷方式

1. **在手机浏览器中打开 APP**
2. **创建书签/快捷方式**
3. **移动到主屏幕**

## 🎨 自定义 APP

### 修改 APP 名称

编辑 `index.html` 文件，找到 `<title>` 标签：

```html
<title>福库心理 - 身心同调 APP</title>
```

### 修改 APP 图标

1. **准备图标文件**
   - 尺寸：192x192 像素
   - 格式：PNG
   - 命名：`icon-192.png`

2. **添加到 index.html**

在 `<head>` 部分添加：

```html
<link rel="apple-touch-icon" sizes="192x192" href="icon-192.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
```

### 修改主题色

编辑 `index.html` 中的 CSS：

```css
header {
    background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
    /* 修改这里的颜色 */
}
```

### 添加文章

编辑 `index.html`，找到 `articles` 数组，添加新文章：

```javascript
const articles = [
    {
        title: "新文章标题",
        category: "mind",  // 身、心、神、伴侣、AI
        summary: "文章摘要...",
        date: "2026-03-13",
        url: "https://jinfuku.github.io/fukuxinli/mind/新文章/"
    },
    // ... 其他文章
];
```

## 🔄 更新 APP

### 更新内容

1. **编辑 index.html**
2. **提交并推送**

```powershell
cd c:\Users\jinfu\WorkBuddy\Claw\fuku-app
git add .
git commit -m "更新 APP 内容"
git push origin main
```

3. **等待部署**
   - GitHub Pages 会自动更新
   - 通常需要 1-3 分钟

4. **刷新 APP**
   - 在手机上刷新页面
   - 或重新打开 APP

## 📊 查看统计

### 访问统计
访问：https://github.com/jinfuku/fuku-app/graphs/traffic

### 部署历史
访问：https://github.com/jinfuku/fuku-app/deployments

## 🆘 常见问题

### Q1: 推送时提示认证错误

**解决方案：**
1. 使用个人访问令牌而不是密码
2. 确保用户名是 `jinfuku`
3. 检查令牌是否具有 `repo` 权限

### Q2: APP 显示 404

**解决方案：**
1. 确认仓库是 Public（公开）
2. 等待 2-3 分钟让 GitHub 处理
3. 清除浏览器缓存
4. 检查 GitHub Pages 设置

### Q3: 如何在手机上获得更好的体验？

**建议：**
1. 将 APP 添加到主屏幕
2. 允许浏览器创建桌面图标
3. 使用全屏模式浏览

### Q4: APP 可以离线使用吗？

**当前版本：** 需要联网

**未来方案：**
- 开发原生 APK 支持 Service Worker
- 实现离线缓存功能

## 🎯 下一步

### 短期目标
- [ ] 成功部署到 GitHub Pages
- [ ] 在手机上测试 APP
- [ ] 收集用户反馈
- [ ] 优化用户体验

### 中期目标
- [ ] 添加应用图标
- [ ] 优化移动端体验
- [ ] 添加更多文章
- [ ] 实现离线阅读

### 长期目标
- [ ] 开发 Flutter 原生 APP
- [ ] 生成 APK 安装包
- [ ] 发布到应用商店
- [ ] 添加推送通知

## 📞 联系方式

如有问题，请联系福库老师。

## 🌐 重要链接

- **APP 地址：** https://jinfuku.github.io/fuku-app/
- **GitHub 仓库：** https://github.com/jinfuku/fuku-app
- **完整网站：** https://jinfuku.github.io/fukuxinli/

---

**福库心理 APP，陪伴您身心成长！** 🌱
