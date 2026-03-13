@echo off
echo 正在创建icons文件夹...
mkdir icons 2>nul
echo icons文件夹已创建
echo.
echo 请按照以下步骤手动添加图标：
echo 1. 在浏览器中打开: %cd%\generate-icons.html
echo 2. 等待图标下载完成
echo 3. 将下载的8个PNG文件移动到icons文件夹
echo 4. 运行: 部署图标到GitHub.bat
echo.
pause
