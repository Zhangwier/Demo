@echo off
setlocal ENABLEDELAYEDEXPANSION
mode con cols=50 lines=15
color f0

:num
set name=123
set num=156315
set pwd=123


:meun
cls
choice /c:bds /m:"please select"
 if %errorlevel%==1 call :build
 if %errorlevel%==2 goto d
 if %errorlevel%==3 call :s
goto meun
:d
cls
set /p t=输入账号
set time=1
for %%i in (*.txt) do if %%i == %t% set time=0 
if  %time% == 0 goto error
:d2
cls
choice /c:sdc /m:"please select"
 if %errorlevel%==1 call :seave
 if %errorlevel%==2 call :read
 if %errorlevel%==3 call :s
goto d2


:s
set /p t=输入账号名
del %t%.txt
echo 删除成功！
pause>null
goto:eof


:build
set /p t=输入账号名
call :seave
echo 创建成功！
pause>null
goto:eof


:error
echo 账号不存在！
pause>null
goto meun


:seave
echo name=%name%>%t%.txt
echo num=%num%>>%t%.txt
echo pwd=%pwd%>>%t%.txt
echo 保存成功！
pause>null
goto:eof


:read
for /f %%i in (%t%.txt) do set %%i 
echo 读取成功！
pause>null
goto:eof