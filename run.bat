@echo off 

REM 
set /p play=Do you want to play rock, paper, scissors? (Y/N): 

REM 
if /i "%play%"=="Y" (
    REM 
    python ./src/main.py %*
) else (
    REM 
    exit
)

pause 
