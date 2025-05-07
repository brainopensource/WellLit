@echo off
setlocal

REM Solicita mensagem do usuário
set /p msg=Enter commit message: 

REM Gera um timestamp para deixar a mensagem única
for /f %%i in ('powershell -Command "Get-Date -Format yyyyMMdd-HHmmss"') do set timestamp=%%i

REM Concatena a mensagem com o timestamp
set "fullmsg=%msg% [%timestamp%]"

REM Executa os comandos Git
git add .
git commit -m "%fullmsg%"
git push

echo.
echo Commit and push completed: %fullmsg%
pause
