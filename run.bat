@echo off
IF NOT EXIST "venv" (
    echo Virtual environment not found. Please run install.bat first.
    pause
    exit /b
)

call venv\Scripts\activate

echo Launching the Streamlit app...
python -m streamlit run src\app.py

echo.
echo Press any key to exit...
pause
