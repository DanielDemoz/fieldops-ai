@echo off
REM Upload FieldOps AI to GitHub
REM Repository: https://github.com/DanielDemoz/fieldops-ai

echo ========================================
echo Uploading FieldOps AI to GitHub
echo Repository: https://github.com/DanielDemoz/fieldops-ai
echo ========================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Check if git is initialized
if not exist ".git" (
    echo Initializing Git repository...
    git init
    echo.
)

REM Check if remote exists
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Setting up remote origin...
    git remote add origin https://github.com/DanielDemoz/fieldops-ai.git
    echo.
)

echo Adding all files...
git add .
echo.

echo Creating commit...
git commit -m "Initial commit - FieldOps AI platform by Brukd Consultancy"
echo.

echo Setting main branch...
git branch -M main
echo.

echo Pushing to GitHub...
echo Please enter your GitHub credentials when prompted.
git push -u origin main
echo.

echo ========================================
echo Upload complete!
echo Repository: https://github.com/DanielDemoz/fieldops-ai
echo ========================================
pause

