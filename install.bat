@echo off
IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Installing/updating dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Setup complete. Press any key to exit...
pause
