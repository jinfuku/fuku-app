@echo off
echo ========================================
echo 福库心理APP图标生成器
echo ========================================
echo.

cd /d "%~dp0"

echo 正在检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未检测到Python，请先安装Python
    echo 下载地址: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python环境正常
echo.

echo 正在检查Pillow库...
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo ❌ 未安装Pillow库，正在安装...
    pip install pillow
    if errorlevel 1 (
        echo ❌ Pillow安装失败
        pause
        exit /b 1
    )
    echo ✅ Pillow安装成功
    echo.
)

echo ========================================
echo 正在生成APP图标...
echo ========================================
echo.

python generate-icons.py

if errorlevel 1 (
    echo ❌ 图标生成失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo 生成完成！
echo ========================================
echo.
echo 图标已保存到 icons 文件夹
echo.
echo 下一步：运行 部署图标到GitHub.bat
echo.

pause
