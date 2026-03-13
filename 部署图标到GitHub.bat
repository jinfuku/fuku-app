@echo off
cd /d "%~dp0"
echo 正在提交图标到GitHub...
git add icons/
git commit -m "添加APP图标"
git push origin main
echo.
echo 图标已部署到GitHub！
echo.
echo 访问: https://jinfuku.github.io/fuku-app/
pause
