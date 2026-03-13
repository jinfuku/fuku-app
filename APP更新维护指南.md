# 📝 APP更新维护指南

本指南教你如何更新福库心理APP的文章、调整布局和插入图片。

## 📖 目录
1. [更新文章内容](#更新文章内容)
2. [调整页面布局](#调整页面布局)
3. [插入图片](#插入图片)
4. [部署更新](#部署更新)

---

## 📝 更新文章内容

### 文章数据存储位置

所有文章数据存储在 `index.html` 文件的 `<script>` 标签中：

```javascript
const articles = [
    {
        id: 1,
        title: '文章标题',
        category: '分类',
        summary: '文章摘要',
        date: '2024-01-15',
        isPremium: false
    },
    // 更多文章...
];
```

### 如何添加新文章

1. **打开文件**
   ```
   fuku-app/index.html
   ```

2. **找到 articles 数组**（约第329行）

3. **在数组中添加新文章**，例如：

   ```javascript
   {
       id: 8,  // 使用新的ID号
       title: '你的新文章标题',
       category: '身',  // 分类：身/心/神/伴侣关系/AI
       summary: '这是文章的简短摘要，会显示在文章卡片上',
       date: '2024-03-13',  // 使用YYYY-MM-DD格式
       isPremium: false  // true=付费文章, false=免费文章
   },
   ```

4. **如果是付费文章**，添加价格字段：

   ```javascript
   {
       id: 8,
       title: '付费文章标题',
       category: '心',
       summary: '这是一篇付费文章的摘要',
       date: '2024-03-13',
       isPremium: true,
       price: '99元'  // 付费文章需要设置价格
   },
   ```

### 如何修改现有文章

1. 找到对应的文章（通过id或标题）
2. 直接修改字段值：

   ```javascript
   {
       id: 1,
       title: '修改后的标题',        // 修改标题
       category: '心',               // 修改分类
       summary: '修改后的摘要',      // 修改摘要
       date: '2024-03-13',          // 修改日期
       isPremium: true               // 改为付费文章
   },
   ```

### 如何删除文章

1. 找到要删除的文章对象
2. 删除整个对象（包括逗号）

**删除前：**
```javascript
{
    id: 1,
    title: '旧文章',
    // ...
},  // ← 删除这个逗号
{
    id: 2,
    title: '下一篇文章',
    // ...
},
```

**删除后：**
```javascript
{
    id: 2,
    title: '下一篇文章',
    // ...
},
```

### 文章字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | 数字 | ✅ | 唯一标识符，不能重复 |
| `title` | 字符串 | ✅ | 文章标题 |
| `category` | 字符串 | ✅ | 分类：身/心/神/伴侣关系/AI |
| `summary` | 字符串 | ✅ | 文章摘要 |
| `date` | 字符串 | ✅ | 发布日期（YYYY-MM-DD） |
| `isPremium` | 布尔值 | ✅ | 是否为付费文章 |
| `price` | 字符串 | ❌ | 付费文章的价格（仅isPremium=true时需要） |

---

## 🎨 调整页面布局

### 颜色主题修改

所有颜色定义在 `<style>` 标签中（约第7-261行）：

#### 1. 修改主题色

**顶部导航栏渐变色**（第26行）：
```css
header {
    background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
}
```
- `#00c853` - 绿色
- `#2196f3` - 蓝色

**按钮主题色**（第243-245行）：
```css
.feature-btn.primary {
    background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
}
```

**分类按钮激活色**（第69-72行）：
```css
.category-btn.active {
    background: #00c853;
    color: white;
}
```

#### 2. 修改背景色

**页面背景色**（第16行）：
```css
body {
    background-color: #f5f5f5;  /* 浅灰色背景 */
}
```

**文章卡片背景**（第87行）：
```css
.article-card {
    background: white;  /* 白色背景 */
}
```

### 字体大小调整

#### 1. 修改标题大小

**页面主标题**（第35-38行）：
```css
header h1 {
    font-size: 20px;  /* 增大或减小这个值 */
}
```

**文章卡片标题**（第122-126行）：
```css
.article-title {
    font-size: 16px;  /* 文章标题大小 */
}
```

#### 2. 修改文字大小

**文章摘要**（第129-133行）：
```css
.article-summary {
    font-size: 14px;  /* 摘要文字大小 */
}
```

**分类按钮文字**（第57-67行）：
```css
.category-btn {
    font-size: 14px;  /* 按钮文字大小 */
}
```

### 间距调整

#### 1. 页面内边距

**主内容区域**（第80-82行）：
```css
main {
    padding: 15px;  /* 增大或减小内边距 */
}
```

#### 2. 卡片间距

**文章卡片**（第88-89行）：
```css
.article-card {
    padding: 15px;           /* 卡片内边距 */
    margin-bottom: 15px;      /* 卡片底部间距 */
}
```

#### 3. 按钮大小

**功能按钮**（第229-231行）：
```css
.feature-btn {
    padding: 15px;  /* 增大或减小按钮内边距 */
}
```

### 分类按钮修改

#### 添加新分类

1. 找到分类导航部分（第269-277行）：
```html
<div class="category-nav">
    <button class="category-btn active" onclick="filterCategory('all')">全部</button>
    <button class="category-btn" onclick="filterCategory('身')">身</button>
    <!-- 在这里添加新分类 -->
</div>
```

2. 添加新分类按钮：
```html
<button class="category-btn" onclick="filterCategory('新分类')">新分类</button>
```

3. 在文章中使用新分类：
```javascript
{
    id: 8,
    title: '文章标题',
    category: '新分类',  // 使用新分类名
    summary: '摘要',
    date: '2024-03-13',
    isPremium: false
}
```

---

## 🖼️ 插入图片

### 方法1：在文章中显示图片（简单方案）

由于APP的文章是通过JavaScript动态加载的，目前只显示标题、摘要和日期。如果要在文章中添加图片，有以下两种方案：

#### 方案A：在文章卡片上显示缩略图

1. **修改文章数据结构**，添加图片字段：

```javascript
const articles = [
    {
        id: 1,
        title: '文章标题',
        category: '身',
        summary: '文章摘要',
        date: '2024-01-15',
        isPremium: false,
        image: 'images/article-1.jpg'  // 添加图片路径
    },
];
```

2. **修改渲染函数**，显示图片：

找到 `renderArticles` 函数（约第393-414行），修改文章卡片HTML：

```javascript
articleList.innerHTML = filteredArticles.map(article => `
    <div class="article-card" onclick="openArticle(${article.id})">
        ${article.image ? `<img src="${article.image}" class="article-image" alt="${article.title}">` : ''}
        <div class="article-category">${article.category}${article.isPremium ? '<span class="premium-badge">🔒 付费</span>' : ''}</div>
        <div class="article-title">${article.title}</div>
        <div class="article-summary">${article.summary}</div>
        <div class="article-date">${article.date}</div>
    </div>
`).join('');
```

3. **添加图片样式**：

在 `<style>` 标签中添加：

```css
.article-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
}
```

4. **创建images文件夹并添加图片**：

```bash
mkdir images
```

将你的图片文件放到 `images/` 文件夹中，例如：
- `images/article-1.jpg`
- `images/article-2.png`

#### 方案B：创建完整的文章详情页面

如果你想要完整的文章内容（包括多张图片），需要创建文章详情页面。这需要更多开发工作。

### 方法2：使用Base64编码内嵌图片（小图片）

如果图片较小（小于50KB），可以直接将图片转换为Base64编码内嵌：

1. **将图片转换为Base64**：
   - 在线工具：https://www.base64-image.de/
   - 上传图片，复制Base64代码

2. **在文章中使用**：

```javascript
{
    id: 1,
    title: '文章标题',
    category: '身',
    summary: '文章摘要',
    date: '2024-01-15',
    isPremium: false,
    image: 'data:image/png;base64,iVBORw0KGgoAAAANS...'  // Base64编码
}
```

**优点：** 不需要额外文件，图片随HTML一起加载
**缺点：** 只适合小图片，会增加文件大小

### 图片格式建议

| 格式 | 用途 | 特点 |
|------|------|------|
| JPEG | 照片类图片 | 压缩率高，适合照片 |
| PNG | 图标、logo | 支持透明背景 |
| WebP | 现代格式 | 压缩率高，质量好 |
| SVG | 矢量图 | 可缩放，适合图标 |

### 图片尺寸建议

| 用途 | 推荐尺寸 | 文件大小 |
|------|----------|----------|
| 文章缩略图 | 400x300 px | < 100KB |
| 文章大图 | 800x600 px | < 300KB |
| 头像图标 | 100x100 px | < 20KB |

---

## 🚀 部署更新

修改完成后，按以下步骤部署到GitHub Pages：

### 方法1：使用命令行（推荐）

1. **打开PowerShell**，进入APP目录：
   ```powershell
   cd c:/Users/jinfu/WorkBuddy/Claw/fuku-app
   ```

2. **提交更改**：
   ```powershell
   git add .
   git commit -m "更新文章内容"
   ```

3. **推送到GitHub**：
   ```powershell
   git push origin main
   ```

4. **等待GitHub Pages自动部署**（1-3分钟）

5. **清除浏览器缓存并刷新**：
   - 按 `Ctrl + Shift + Delete`
   - 或 `Ctrl + Shift + R`

### 方法2：使用GitHub Desktop

1. 打开GitHub Desktop
2. 选择 `fuku-app` 仓库
3. 查看更改，输入提交信息
4. 点击"Commit to main"
5. 点击"Push origin"

### 方法3：直接在GitHub上编辑

1. 访问 https://github.com/jinfuku/fuku-app
2. 点击 `index.html` 文件
3. 点击右上角 ✏️ 铅笔图标
4. 修改内容
5. 在页面底部输入提交信息
6. 点击 "Commit changes"

---

## 💡 最佳实践

### 1. 文章更新建议

- ✅ 定期更新文章，保持内容新鲜
- ✅ 使用清晰的分类
- ✅ 写好摘要，吸引点击
- ✅ 设置合理的日期

### 2. 图片优化建议

- ✅ 压缩图片，减小文件大小
- ✅ 使用合适的图片尺寸
- ✅ 选择最佳格式（JPEG/WebP）
- ✅ 为图片提供alt文本（可访问性）

### 3. 布局设计建议

- ✅ 保持简洁，避免过度装饰
- ✅ 使用合适的间距
- ✅ 确保文字可读性
- ✅ 响应式设计，适配各种屏幕

### 4. 版本管理

- ✅ 每次更新写清楚的提交信息
- ✅ 重要更新可以创建备份
- ✅ 定期检查和测试

---

## 🔧 常见问题

### Q1: 修改后没有看到变化？

**A:** 清除浏览器缓存：
- Chrome: Ctrl + Shift + Delete
- 或强制刷新: Ctrl + Shift + R

### Q2: 图片不显示？

**A:** 检查以下几点：
- 图片路径是否正确
- 文件名是否匹配（区分大小写）
- 图片文件是否已提交到GitHub
- 等待GitHub Pages部署完成

### Q3: 布局乱了？

**A:** 检查CSS语法：
- 确保所有大括号 `{}` 成对
- 确保所有属性以 `;` 结尾
- 检查是否有拼写错误

### Q4: 文章不显示？

**A:** 检查数据结构：
- id是否唯一
- 字段是否完整
- JSON格式是否正确（逗号位置）

---

## 📞 需要帮助？

如果遇到问题：
1. 检查浏览器控制台的错误信息（F12 → Console）
2. 检查GitHub Pages部署状态
3. 查看本文档的相关章节

祝你的福库心理APP越来越完善！🎉
