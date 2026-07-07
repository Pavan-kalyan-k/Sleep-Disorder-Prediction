@echo off
REM Quick start script for Sleep Disorder Prediction App
REM This script installs dependencies and runs the Streamlit app

echo.
echo ========================================
echo Sleep Disorder Prediction App
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version
echo.

echo [2/3] Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)
echo Package installation completed!
echo.

echo [3/3] Starting Streamlit app...
echo.
echo The app will open in your default browser at http://localhost:8501
echo Press Ctrl+C in this window to stop the server
echo.
timeout /t 2

streamlit run app.py

pause
