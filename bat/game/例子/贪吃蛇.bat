@echo off&setlocal EnableDelayedExpansion&rem made by a2002
if "%~1" equ "Control" set fw=s&set fa=d&set fs=w&set fd=a&goto :Control
start /b "" "%~f0" Control

set Speed=100
set long=3
set Snake=■
set food=◇
set Empty=　

call :StartWith
:Main
set mov=1&call :echo
Cons Sleep,!Speed!
set /p drv=<snk.tmp
if !drv! equ w set /a X-=1
if !drv! equ a set /a Y-=1
if !drv! equ s set /a X+=1
if !drv! equ d set /a Y+=1
call :Check
call :Move !mov!
goto :Main

:StartWith
mode 80,24&set crlf=^

&Cons SetTitle,贪吃蛇游戏
Cons SetIcon,%~dp0Snake.ico&Cons HideCur
for /l %%# in (1,1,!long!) do set t=!t!1
set t=!t!00000000000000000000
set Data=!t:~0,20!
for /l %%# in (2,1,20) do set Data=!Data!00000000000000000000
set Top=┏━━━━━━━━━━━━━━━━━━━━┓
set Bot=┗━━━━━━━━━━━━━━━━━━━━┛
for /l %%# in (1,1,!long!) do set Pos=!Pos!,1.%%#
set Pos=!Pos:~1!&set /a X=1,Y=long
echo d>snk.tmp&set foodPos=378&call :Setfood
set Mark=0&exit /b

:echo
Cons SetCurPos,0,0
set _Data=!Data:0=%Empty%!&set _Data=!_Data:1=%Snake%!&set _Data=!_Data:2=%food%!
set echo=!Top!&for /l %%# in (0,20,380) do set echo=!echo!!crlf!┃!_Data:~%%#,20!┃&if %%# equ 0 set echo=!echo!分数:!mark!    蛇长:!long!
echo;!echo!!crlf!!Bot!!crlf!made by a2002     press "u" to quit
exit /b

:Control
set /p drv=<snk.tmp
set "t="&for /f "delims=" %%a in ('xcopy /w . . 2^>nul') do if not defined t set "t=%%a"
set "t=!t:~-1!"
for %%# in (w a s d) do if "!t!" equ "%%#" if !f%drv%! neq %%# echo %%#>snk.tmp
if "!t!" equ "u" Cons SendMsg,274,61536,0
goto :Control

:Getfood
set /a foodPos=!random!%%400
exit /b

:Over
set /p=Game over,press "u" to quit<nul
pause>nul

:Check
if !X! gtr 20 goto :Over
if !X! lss 1 goto :Over
if !Y! gtr 20 goto :Over
if !Y! lss 1 goto :Over
set /a t1=X*20+Y-21
if "!Data:~%t1%,1!" equ "2" call :Getfood&exit /b
if "!Data:~%t1%,1!" equ "1" goto :Over
exit /b

:Move
set /a t1=X*20+Y-21,t2=t1+1
set Data=!Data:~0,%t1%!1!Data:~%t2%!
for /f "tokens=1* delims=," %%a in ("!Pos!") do (
for /f "tokens=1,2 delims=." %%x in ("%%a") do set /a t1=%%x*20+%%y-21,t2=t1+1
if %1 equ 1 (set Pos=%%b,!X!.!Y!) else set Pos=!Pos!,!X!.!Y!)
if %1 equ 1 set Data=!Data:~0,%t1%!0!Data:~%t2%!
exit /b

:Getfood
set /a t1=X*20+Y-21,t2=t1+1,long+=1,mark+=long/10+1,mov=0
set Data=!Data:~0,%t1%!1!Data:~%t2%!
:Getfood_loop
set /a foodPos=!random!%%400
if "!Data:~%foodPos%,1!" neq "0" goto :Getfood_loop
call :Setfood&exit /b

:Setfood
set /a t1=foodPos+1
set Data=!Data:~0,%foodPos%!2!Data:~%t1%!
exit /b