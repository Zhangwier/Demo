@echo off
setlocal ENABLEDELAYEDEXPANSION
mode con cols=24 lines=10
title 走迷宫 v3.0
color e0
set lv=1
set see=5

:start
(
cls
echo 加载中，请稍后...
echo Loading...
setlocal
if "%1"=="/z" (set file=map\zdy) else set file=map\level%lv%
set Y=0
if not exist !file!.txt exit
for /f "eol=; delims=" %%i in (!file!.txt) do (
 set "seti=%%i"
 if /i "!seti:~0,2!"=="#k" (
  for /f "tokens=2,* delims= " %%j in ("!seti!") do set "key%%j=%%k"
 ) else if /i "!seti:~0,2!"=="#p" (
  for /f "tokens=2,* delims= " %%j in ("!seti!") do set "pap%%j=%%k"
 ) else (
  set /a "Y+=1" & set z!Y!=%%i
  for %%j in (z!Y!) do if "!%%j:♀=!" neq "!%%j!" (
   call :len "!seti!" X
   for /l %%k in (0 1 !X!) do if "!seti:~%%k,1!"=="♀" set /a "manX=%%k+1,manY=!Y!"
)))
)
set "seti="

:game
(
cls
set /a "Xs=!manX!-2,Ys=!manY!-2"
set /a "Xe=!Xs!+%see%-1,Ye=!Ys!+%see%-1"
set /a "Xs+=(((!Xe!-!X!)*2-1)%%2+1)/2*(!X!-!Xe!)"
set /a "Ys+=(((!Ye!-!Y!)*2-1)%%2+1)/2*(!Y!-!Ye!)"
set /a "Xs+=(((!Xs!-1)*(-2)-1)%%2+1)/2"
set /a "Ys+=(((!Ys!-1)*(-2)-1)%%2+1)/2"
set /a "Xe=!Xs!+%see%-1,Ye=!Ys!+%see%-1"
for /l %%i in (!Ys! 1 !Ye!) do (
 set /a "tp=!Xs!-1"
 for %%j in (!tp!) do echo,!z%%i:~%%j,%see%!
)
if "!paper!"=="on" echo !pap%manX%,%manY%!

choice /c wiskajdl56rt /n>nul
set /a "err=(!errorlevel!+1)/2,error=!errorlevel!"
if !error!==12 exit
if !error!==11 endlocal & goto start
if !error! geq 9 if !error! leq 10 (
 set /a "lv+=2*(!error!-9)-1"
 if exist map\level!lv!.txt for %%i in (!error!) do (
  endlocal
  set /a "lv+=2*(%%i-9)-1"
  goto start
 )
) else goto game
if !err! leq 2 (set "mbX=!manX!") else set "mbY=!manY!"
if !err!==4 set /a "mbX=!manX!+1"
if !err!==3 set /a "mbX=!manX!-1"
if !err!==2 set /a "mbY=!manY!+1"
if !err!==1 set /a "mbY=!manY!-1"

rem 转换为for型变量
for %%i in (!mbX!) do for %%j in (!mbY!) do for %%k in (!manX!) do ^
for %%l in (!manY!) do set /a "tp=%%i-1" & for %%m in (!tp!) do ^
set /a "tp=%%k-1" & for %%n in (!tp!) do (

set "mb=!z%%j:~%%m,1!"
if "!mb!" neq "█" set "paper="
if "!mb!"=="　" (
 set "z%%j=!z%%j:~0,%%m!♀!z%%j:~%%i!"
 set "z%%l=!z%%l:~0,%%n!　!z%%l:~%%k!"
 set /a "manX=!mbX!,manY=!mbY!"
)
if "!mb!"=="▓" (
 set "paper=on"
 set "z%%j=!z%%j:~0,%%m!♀!z%%j:~%%i!"
 set "z%%l=!z%%l:~0,%%n!　!z%%l:~%%k!"
 set /a "manX=!mbX!,manY=!mbY!"
)
if "!mb!"=="☉" (
 set "z%%j=!z%%j:~0,%%m!♀!z%%j:~%%i!"
 set "z%%l=!z%%l:~0,%%n!　!z%%l:~%%k!"
 set /a "manX=!mbX!,manY=!mbY!"
 for %%o in ("e,　" "p,▓" "k,☉" "w,█") do (
  for /f "tokens=1,2 delims=," %%p in ("%%~o") do set "tp=!key%%p%%i,%%j!" & (
   if "!tp!" neq "" set "tp=!tp: =" "!" & for %%r in ("!tp!") do (
    for /f "tokens=1,2 delims=," %%s in ("%%~r") do set /a "tp=%%s-1" & (
     for %%u in (!tp!) do set "z%%t=!z%%t:~0,%%u!%%q!z%%t:~%%s!"
 ))))
)
if "!mb!"=="★" (
 cls
 set /a lv+=1
 if exist map\level!lv!.txt (
  echo,你赢了这一关！
  set /p =请按任意键继续...<nul
  pause>nul & cls
  endlocal
  set /a lv+=1
  goto start
 ) else (
  echo,你赢了所有关！
  set /p =请按任意键退出...<nul
  pause>nul & exit
 )
) else goto game

rem 转换结束
)
)
goto game

:len
set "string=%~1"
set "len=1"
if "!string!"=="" set "string=" & set "%~2=%len%" & goto :eof
:lenloop
if "!string:~%len%,1!"=="" (
 set "string="
 set "%~2=%len%"
 goto :eof
) else (
 set /a "len=%len%+1"
 goto lenloop
)