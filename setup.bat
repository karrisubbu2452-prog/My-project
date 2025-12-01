@echo off
echo ======================================
echo   AI PODCAST PROJECT AUTO SETUP
echo ======================================

REM Create Virtual Environment
echo Creating virtual environment...
python -m venv venv

REM Activate environment
echo Activating environment...
call venv\Scripts\activate

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo ======================================
echo SETUP COMPLETE!
echo ======================================

echo IMPORTANT:
echo 1. Create a file named .env inside the project folder
echo 2. Add this line:
echo    OPENAI_API_KEY=your_api_key_here
echo\

echo To run the project:
echo    venv\Scripts\activate
echo    python src\orchestrator.py

pause
