@echo off
mode con cols=85 lines=21
color 0a
setlocal enabledelayedexpansion
set a=0
for %%m in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
if !a! leq 9 (set n0!a!=%%m) else (set n!b!=%%m)
set /a a+=1
set /a b=!a!-10
)
for %%M in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
set n!b!=%%M
set /a b+=1
)
for /l %%a in (1,1,20) do (
set h%%a=
for /l %%b in (1,1,20) do (
call,set code=%%n!random:~1,2!%%
if not defined code (set "code= ")
set h%%a=!code!   !h%%a!
)
)
set num=0
:a
set /a num+=1
if %num% equ 260 set num=0
ping -n>nul
cls
echo,   %h1%
echo,   %hn%
for /l %%a in (3,1,20) do echo,   !h%%a!
for /l %%a in (19,-1,1) do (
set /a n=1+%%a
set h!n!=!h%%a!
)
set hn=%h2%
set h1=
for /l %%b in (1,1,20) do (
call,set code=%%n!random:~1,2!%%
if not defined code (set "code= ")
set h1=!code!   !h1!
)

if %num% gtr 20 (if %num% lss 100 set hn=                      %h19:   = %)
if %num% gtr 40 (if %num% lss 160 set hn=                      %h19:   = %)
if %num% gtr 80 (if %num% lss 220 set hn=                      %h19:   = %)
if %num% gtr 30 (if %num% leq 60 (
set hn=%hn:~0,20%    Brain wave access......    %hn:~-20%
))
if %num% gtr 90 (if %num% leq 120 (
set hn=%hn:~0,19%      Brain wave access successful!     %hn:~-19%
))
if %num% gtr 150 (if %num% leq 180 (
set hn=%hn:~0,19%          Joining the world!        %hn:~0,19%
))
for %%a in (30 90 150) do (
if %num% equ %%a (set hn=                     =====================+================== ))
if %num%==180 goto end
goto :a
:end 
cls




title 激活验证
mode con cols=75 lines=10
set times=3
for /f %%i in (mylog.txt) do set code=%%i

:password
cls
echo #######################################################################
echo 操作： 激活密码验证 时间：%time% 日期：%date%
echo 状态： 等待验证……
echo. 
echo [ LOGIN ]
set /p pwd= 请输入您的密码：
set /A times=%times%-1
if %pwd%==%code% goto pass
echo ***** 密码验证错误，请您重新输入 您还有 %times% 次机会输入密码 *****
echo .
if %times%==0 goto close
echo 状态： 用户输入密码 验证失败 时间：%time%
goto password

:close
cls
echo 状态： 用户3次输入密码错误 程序锁定 时间：%time%
echo --------------------------------------------------------------------------------
echo 由于您3次密码验证失败，程序已经被锁定，您已经无法继续操作，您可以选择关闭
pause
goto close

:pass
cls
echo #######################################################################
echo 操作： 进入游戏 时间：%time% 日期：%date%
echo 状态： 程序已开放，欢迎使用
set /p pwd= 如需修改密码请输入1:
if %pwd%==1 (
set /p code= 请输入想要修改的密码:
call :change %code%
pause
goto pass
)
start game.bat


:change
echo %1 > mylog.txt
echo 修改成功！密码为%1
goto:eof