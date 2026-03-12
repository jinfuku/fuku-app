@echo off
chcp 65001 > nul
echo ========================================
echo 福库心理 APP - 部署到 GitHub Pages
echo ========================================
echo.

cd /d %~dp0

echo 第一步：检查 Git 远程仓库...
git remote -v
echo.

if not exist ".git\refs\remotes\origin" (
    echo 检测到没有配置远程仓库
    echo.
    echo 请先执行以下步骤：
    echo 1. 访问 https://github.com/jinfuku/new
    echo 2. 创建名为 "fuku-app" 的新仓库
    echo 3. 然后执行命令：
    echo    git remote add origin https://github.com/jinfuku/fuku-app.git
    echo 4. 重新运行此脚本
    echo.
    pause
    exit /b 1
)

echo 第二步：提交当前更改...
git add .
git commit -m "更新 APP 内容"
echo 提交完成！
echo.

echo 第三步：推送到 GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo 推送失败！请检查：
    echo 1. 网络连接是否正常
    echo 2. GitHub 账户认证信息
    echo 3. 仓库是否已创建
    pause
    exit /b 1
)
echo 推送成功！
echo.

echo ========================================
echo 部署成功！
echo ========================================
echo.
echo 下一步操作：
echo 1. 访问 https://github.com/jinfuku/fuku-app/settings/pages
echo 2. 在 Source 中选择 "Deploy from a branch"
echo 3. 在 Branch 中选择 "main" 分支
echo 4. 点击 Save 按钮
echo 5. 等待 1-3 分钟
echo.
echo APP 地址：https://jinfuku.github.io/fuku-app/
echo ========================================
echo.

echo 提示：
echo - 在手机上打开 APP 地址
echo - 将 APP 添加到主屏幕
echo - 像原生 APP 一样使用
echo.

pause
