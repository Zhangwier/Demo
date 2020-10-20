@echo off 
for /l %%i in (1 1 70) do ( 
set /p=O<nul 
for /l %%a in (1 1 50) do ver>nul 
) 
pause>nul 