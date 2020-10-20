@echo off
setlocal ENABLEDELAYEDEXPANSION
mode con cols=65 lines=20
title ²âÊÔ°æv0.1
color e0

:c1
cls
choice /c:wsad /m:"please select"
 if %errorlevel%==1 echo ctt=1 >ctt.txt
 if %errorlevel%==2 echo ctt=2 >ctt.txt
 if %errorlevel%==3 echo ctt=3 >ctt.txt
 if %errorlevel%==4 echo ctt=4 >ctt.txt
goto c1



pause>null