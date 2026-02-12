@echo off
REM ========================================
REM Django Project Startup Script
REM ========================================

echo.
echo ========================================
echo Starting Django Project...
echo ========================================
echo.

REM Activate virtual environment
echo [1/3] Activating virtual environment...
call "c:\Modeling\env\Scripts\activate.bat"

REM Navigate to project directory
echo [2/3] Navigating to project directory...
cd /d "c:\Modeling\Modeling, Detecting, and Mitigating Threats Against\Modeling_Detecting_and_Mitigating_Threats\modeling_detecting_and_mitigating_threats"

REM Start Django server
echo [3/3] Starting Django server...
echo.
echo ========================================
echo Server will start at: http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo ========================================
echo.

"c:\Modeling\env\Scripts\python.exe" run_server_new.py

pause
