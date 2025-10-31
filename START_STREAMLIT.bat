@echo off
REM Change to the script's directory
cd /d "%~dp0"

REM Display current directory
echo Current directory: %CD%
echo.

REM Check if file exists
if not exist "app\dashboard.py" (
    echo ERROR: dashboard.py not found!
    echo Expected location: %CD%\app\dashboard.py
    pause
    exit /b 1
)

echo Starting Streamlit...
echo Dashboard file: %CD%\app\dashboard.py
echo.
echo The dashboard will open at: http://localhost:8501
echo Press Ctrl+C to stop
echo.

py -m streamlit run "app\dashboard.py"

