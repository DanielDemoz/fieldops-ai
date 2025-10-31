@echo off
chcp 65001 >nul
echo ========================================
echo Starting FieldOps AI Dashboard...
echo ========================================
echo.
echo Checking if demo data exists...
if not exist "fieldops.db" (
    echo Database not found. Running setup...
    py run_demo.py
    echo.
)

echo.
echo Starting Streamlit server...
echo.
echo The dashboard will open at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

cd /d "%~dp0"
py -m streamlit run app/dashboard.py

