@echo off
set c=00123456789ABCDEF0
:loop
set /a num=%random%%%16
call set col=%%c:~%num%,2%%
COLOR %col%
ping -n3 127.1>nul
goto loop