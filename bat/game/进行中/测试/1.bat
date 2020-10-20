@echo off
setlocal enabledelayedexpansion

set a=123456
echo %a:~0,1%
echo %a:~1,1%
echo %a:~1,2%
if %a:~1,1% == 2 echo 122
pause



:2
set /a game_name_r=%random%%%10
echo %game_name_r%
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
echo %game_name_r%
pause
goto 1