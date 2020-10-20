@echo off
setlocal ENABLEDELAYEDEXPANSION
mode con cols=65 lines=20
title ²âÊÔ°æv0.1
color e0
call :begin

:main
cls
call :renew_all
echo µ±Ç°×ø±ê:x %ti%  y %tj%
echo %FO91%%FO92%%FO93%%FO94%%FO95%%FO96%%FO97%%FO98%%FO99%
echo %FO81%%FO82%%FO83%%FO84%%FO85%%FO86%%FO87%%FO88%%FO89%
echo %FO71%%FO72%%FO73%%FO74%%FO75%%FO76%%FO77%%FO78%%FO79%
echo %FO61%%FO62%%FO63%%FO64%%FO65%%FO66%%FO67%%FO68%%FO69%
echo %FO51%%FO52%%FO53%%FO54%%FO55%%FO56%%FO57%%FO58%%FO59%
echo %FO41%%FO42%%FO43%%FO44%%FO45%%FO46%%FO47%%FO48%%FO49%
echo %FO31%%FO32%%FO33%%FO34%%FO35%%FO36%%FO37%%FO38%%FO39%
echo %FO21%%FO22%%FO23%%FO24%%FO25%%FO26%%FO27%%FO28%%FO29%
echo %FO11%%FO12%%FO13%%FO14%%FO15%%FO16%%FO17%%FO18%%FO19%
call :ctrl
goto main


:ctrl
choice /c:wsadr /m:"please select"
if %errorlevel%==1 call :move 1 %ti% %tj%
if %errorlevel%==2 call :move 2 %ti% %tj%
if %errorlevel%==3 call :move 3 %ti% %tj%
if %errorlevel%==4 call :move 4 %ti% %tj%
if %errorlevel%==5 call:begin
call :renew_all
goto:eof

:move
call :pmove %1 %2 %3
if %tmove%==1 (
  set IO%2%3=0
  set ti=%pti%
  set tj=%ptj%
  set IO!ti!!tj!=1
  )
GOTO:EOF


:pmove
set pti=%2
set ptj=%3
if %1 == 1 set /a pti+=1
if %1 == 2 set /a pti-=1
if %1 == 3 set /a ptj-=1
if %1 == 4 set /a ptj+=1
if !IO%pti%%ptj%! == 0 set tmove=1
if %ptj% geq 10 set tmove=0
if %pti% geq 10 set tmove=0
if %ptj% leq 0 set tmove=0
if %pti% leq 0 set tmove=0
GOTO:EOF


:begin
for /l %%i in (1,1,9) do (
             for /l %%j in (1,1,9) do set /a "IO%%i%%j=0"
             )
set /a "IO11=1"
set /a ti=1
set /a tj=1
call :renew_all
GOTO:EOF


:renew_all
For /l %%i in (1,1,9) do (
   For /l %%j in (1,1,9) do (
      if !IO%%i%%j! == 0 set "FO%%i%%j=-"
      if !IO%%i%%j! == 1 set "FO%%i%%j=+"
   )  )
GOTO:EOF