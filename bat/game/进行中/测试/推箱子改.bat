::**************推箱子使用说明**************
REM WSAD 上下左右
REM Q退步，M设置锚点，E恢复至锚点
REM R重置，N下一关，F保存用户数据
REM G开启自动推演
cls

::**************Happy's 推箱子**************
@echo off&title 
mode con cols=80 lines=22
REM 窗体配色
  color 0F
::color F0

REM 默认皮肤
::set "ELEMENTS=○□○╳▓▓我踩"
  set "ELEMENTS=○□○╳▓■我踩"
::set "ELEMENTS=○■○╳▓◆我★"
::set "ELEMENTS=○■○╳箱◆大踩"
::set "ELEMENTS=○■○╳▓□我踩"

REM 防闪开关
  set F1=0
::set F1=1
REM 自动脚本
set AUTO=0
::set AUTO=1

REM 计数面板
set "READM1=POSITION："
set "READM3=STEPS:"
set "READM5=ANCHOR:"
set "READM7=MADE BY HAPPY"
set "READM8=　 Version3.0"

::****************先导程序******************
setlocal enabledelayedexpansion
for /l %%i in (1,1,365) do (
	set "SPACE=!SPACE!"
)
for /l %%N in (0,1,7) do (
	set P%%N=!ELEMENTS:~%%N,1!
)
if exist "%~dp0UserData.ini" (
	set/a "AUTO=1,Mark8=1"
	set "ReadFile=%~dp0UserData.ini"
) else (
	set "ReadFile=%~f0"
)
for /f "tokens=1-5" %%A in ('findstr /rc:"^ *[0-9][0-9]* *[0-9][0-9]* *[0-7][0-7].*" "%ReadFile%"') do (
	set "LINES="
	for /l %%i in (1,1,%%A) do (set "LINES=!LINES!--")
	set/a "MapWidth=%%A,MapHeight=%%B,n+=1"
	if not "%%E"=="" (set/a n=%%E)
	set "HEAD=!LINES![LEVEL !n!]"
	set "MapData=%%C"
	set "MapDataBak=%%C"
	set "StepBak=%%D"
	call :MAIN
)
exit


::****************主体程序******************
:MAIN
setlocal
::if !n! leq 2 (set "AUTO=1") else (set "AUTO=0")
if defined Mark8 (set "AUTO=1")
if !AUTO! equ 1 (set "StepStr=!StepBak!")
set/a "Mark2=0"::set/a "Check1=0,Mark2=0"
if !F1! equ 1 cls

REM 构建显存
:DISRAM
for /l %%j in (1,1,%MapHeight%) do (
	set "DISPLAY[%%j]="
	set "tmp=!MapData:~0,%MapWidth%!
	for /l %%i in (1,1,%MapWidth%) do (87
		set "POINT[%%i][%%j]=!tmp:~0,1!"
		set tmp=!tmp:~1!
		if !POINT[%%i][%%j]! equ 6 (set/a "X=%%i,Y=%%j")
		for %%P in (!POINT[%%i][%%j]!) do (
			set "DISPLAY[%%j]=!DISPLAY[%%j]!!P%%P!"
		)
	)
	set "MapData=!MapData:~%MapWidth%!"
)

:ANCHOR
set "READM2=　 (!X!,!Y!)  !AUTO!"
set "READM4=　 !steps!  "
set "READM6=　 [!MarkSteps!]  "
if !F1! equ 1 (2>nul echo 	!SPACE!) else cls

REM 绘图引擎
echo;!HEAD!
for /l %%j in (1,1,%MapHeight%) do (
	echo;!DISPLAY[%%j]:○=　!│!READM%%j!
)
echo;!LINES!

::REM 检查过关
::if not defined Mark2 (
::	if !POINT[%X%][%Y%]! neq 7 (
::		for /l %%j in (1,1,%MapHeight%) do (
::			for %%P in (!P3!) do (
::				if not "!DISPLAY[%%j]:%%P=!"=="!DISPLAY[%%j]!" (set ::Check1=1)
::			)
::		)
::		if not defined Check1 (	
::			echo 恭喜过关！
::			choice /t 1 /d y /n >NUL
::			goto NEXT
::		) else (
::			set "Check1="
::		)
::	)
::)

REM 按键反馈
:CHOISE
set Xp=!X!
set Yp=!Y!
if !AUTO! equ 1 (
	if "!StepStr:~%steps%,1!"=="1" (set/a Y-=1)
	if "!StepStr:~%steps%,1!"=="2" (set/a Y+=1)
	if "!StepStr:~%steps%,1!"=="3" (set/a X-=1)
	if "!StepStr:~%steps%,1!"=="4" (set/a X+=1)
	if "!StepStr:~%steps%,1!"=="D" (
		if defined Mark6 (set "Mark6=")
		for /f "tokens=1 delims=D" %%a in ("!StepStr!") do (
			set "StepStr=%%a"
		)
		set/a AUTO=0
		goto CHOISE
	)
	if defined Mark6 (choice /t 1 /d y /n >NUL)
	goto ANCHOR2
)
choice /C WSADRNQMEFG >NUL
if %errorlevel% equ 1 (set/a Y-=1)
if %errorlevel% equ 2 (set/a Y+=1)
if %errorlevel% equ 3 (set/a X-=1)
if %errorlevel% equ 4 (set/a X+=1)
if %errorlevel% equ 5 (
	endlocal 
	goto MAIN
)
if %errorlevel% equ 6 (
	goto NEXT
)
if %errorlevel% equ 7 (
	set/a Mark4+=1
	if !Mark4! equ 2 (
		set/a "X=Xp,Y=Yp"
		set "Mark4=1"		
		goto CHOISE
	)
	set/a "Xp=X-dx,Yp=Y-dy,1/(dx+dy)" 2>NUL||goto CHOISE
	set/a "POINT[!Xp!][!Yp!]=POINTv0,POINT[!X!][!Y!]=POINTv1,POINT[!Xf!][!Yf!]=POINTv2"
	set/a "Mark3=1,steps-=1,Mark7=1"
	set "StepStr=!StepStr:~0,-1!"
	goto DISGPU 
)
if %errorlevel% equ 8 (
	set/a "Mark5=1,MarkSteps=steps"
	for /l %%j in (1,1,%MapHeight%) do (
		for /l %%i in (1,1,%MapWidth%) do (
			set "POINT_M[%%i][%%j]=!POINT[%%i][%%j]!"
		)
	)
	goto CHOISE
)
if %errorlevel% equ 9 (
	if not defined Mark5 (goto CHOISE)
	for /l %%j in (1,1,%MapHeight%) do (
		set "tmp="
		for /l %%i in (1,1,%MapWidth%) do (
			set "tmp=!tmp!!POINT_M[%%i][%%j]!"
		)
		set "MapData=!MapData!!tmp!"
	)
	set/a "steps=MarkSteps.Mark7=1"
	set "StepStr=!StepStr:~0,%steps%!"
	goto DISRAM
)
if %errorlevel% equ 10 (
	echo %MapWidth% %MapHeight% %MapDataBak% %StepStr%D !n!>"%~dp0UserData.ini"
	exit
)
if %errorlevel% equ 11 (
	if defined Mark8 (
		echo 没有演示文件！
		choice /t 1 /d y /n >NUL
		set "Mark8="
		goto CHOISE
	)
	if "!StepBak!"=="" (
		echo 没有演示文件！
		choice /t 1 /d y /n >NUL
		goto CHOISE
	)
	set "MapData=!MapDataBak!"
	set "StepStr=!StepBak!"
	set/a "AUTO=1,Mark6=1,steps=0"
	goto DISRAM
)

:ANCHOR2
REM 增量坐标
set/a "dx=X-Xp,dy=Y-Yp,Xf=X+dx,Yf=Y+dy"
set POINTv0=!POINT[%Xp%][%Yp%]!
set POINTv1=!POINT[%X%][%Y%]!
set POINTv2=!POINT[%Xf%][%Yf%]!
set "Mark4="

REM 数据一次处理
if !POINTv1! equ 1 (
		set "Mark1=1"		
)
if !POINTv1! equ 2 (
		set/a "POINT[!X!][!Y!]=6
		set "Mark2=1"		
)
if !POINTv1! equ 3 (
		set/a "POINT[!X!][!Y!]=7"
		set "Mark2=1"		
)
if !POINTv1! equ 4 (
		if !POINTv2! equ 1 (set "Mark1=1")
		if !POINTv2! equ 2 (
			set "Mark2=1"
			set/a "POINT[!X!][!Y!]=6,POINT[!Xf!][!Yf!]=4"
		)
		if !POINTv2! equ 3 (
			set "Mark2=1"
			set/a "POINT[!X!][!Y!]=6,POINT[!Xf!][!Yf!]=5"		
		)
		if !POINTv2! equ 4 (set "Mark1=1")
		if !POINTv2! equ 5 (set "Mark1=1")	
)
if !POINTv1! equ 5 (
		if !POINTv2! equ 1 (set "Mark1=1")
		if !POINTv2! equ 2 (
			set "Mark2=1"
			set/a "POINT[!X!][!Y!]=7,POINT[!Xf!][!Yf!]=4"
		)
		if !POINTv2! equ 3 (
			set "Mark2=1"
			set/a "POINT[!X!][!Y!]=7,POINT[!Xf!][!Yf!]=5"
			
		)
		if !POINTv2! equ 4 (set "Mark1=1")
		if !POINTv2! equ 5 (set "Mark1=1")
)
	
REM 数据二次处理
if defined Mark1 (
	set/a "X=Xp,Y=Yp,Mark4=1"
	set "Mark1="
	goto CHOISE
)
set/a steps+=1
if defined Mark2 (
	if !POINTv0! equ 7 (
		set/a "POINT[!Xp!][!Yp!]=3"
	) else (
		set "POINT[!Xp!][!Yp!]=2"
	)
	set "Mark2="
)

REM 绘图加速引擎
:DISGPU
if !dy! equ 0 (
	if not defined Mark7 (
		if !dx! gtr 0 (
			set "StepStr=!StepStr!4"
		) else (
			set "StepStr=!StepStr!3"
		)
	) else (set "Mark7=")
	
	set "DISPLAY[%Yp%]="
	for /l %%i in (1,1,%MapWidth%) do (
		for %%P in (!POINT[%%i][%Y%]!) do (
			set DISPLAY[%Y%]=!DISPLAY[%Y%]!!P%%P!
		)
	)
) else (
	if not defined Mark7 (
		if !dy! gtr 0 (
			set "StepStr=!StepStr!2"
		) else (
			set "StepStr=!StepStr!1"
		)
	) else (set "Mark7=")
	for /l %%j in (!Yp!,!dy!,!Yf!) do (
		set "DISPLAY[%%j]="
		for /l %%i in (1,1,%MapWidth%) do (
			for %%P in (!POINT[%%i][%%j]!) do (
				set DISPLAY[%%j]=!DISPLAY[%%j]!!P%%P!
			)
		)
	)
)
if defined Mark3 (
	set/a "X=Xp,Y=Yp,Mark4=1"
	set "Mark3="
)
goto ANCHOR

:NEXT
endlocal
goto :EOF