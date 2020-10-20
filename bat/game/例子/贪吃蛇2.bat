@echo off
title &setlocal enabledelayedexpansion
::**************Happy's 贪吃蛇**************
REM 设置蛇的时钟，T值越小速度越快
  set T=3
REM 开启防闪烁，用于画质增强
  set F1=1
REM WSAD 上下左右
REM Q退出，P暂停，方向键恢复行走
REM 绿屏表示蛇正常，红屏表示蛇撞墙，紫屏表示蛇自杀

::**************方向控制台窗口**************
if "%1"=="CONTROLP" (
	MODE CON cols=15 lines=1
	echo 1 >key.ini
	for /l %%i in () do (
		choice /C WSADPQ>NUL
		echo !errorlevel!>key.ini&if !errorlevel! equ 6 (exit)
	)
)
start "" "%~f0" CONTROLP

::****************先导程序******************
REM 默认皮肤
  set "ELEMENTS=　□◇⊙★■■■■■☆★○●◎△▲¤⊙"
REM 设置窗体
  mode con cols=68 lines=38
REM 初始化元素4
  set/a "MapHeight=30,MapWidth=30"
  for /l %%i in (1,1,500) do (set "SPACE=!SPACE!")
  for /l %%N in (0,1,19) do (set "P%%N=!ELEMENTS:~%%N,1!")
  for /l %%i in (1,1,%MapWidth%) do (set "LINES=!LINES!━")
REM 构建显存
:DISRAM
color 30&cls&set "MapData=000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000008000000000000000000000000000008000000000000000000000000000008000000000000000000000000000008000000000000000000000000000008000000000000000000000000000008000000000000000000000000000005000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for /l %%j in (1,1,%MapHeight%) do (
	set "DISPLAY[%%j]="
	set "tmp=!MapData:~0,%MapWidth%!"
	for /l %%i in (1,1,%MapWidth%) do (
		set "POINT[%%i][%%j]=!tmp:~0,1!"
		set tmp=!tmp:~1!
		if !POINT[%%i][%%j]! equ 3 (set/a "X=%%i,Y=%%j")
		if !POINT[%%i][%%j]! equ 5 (set/a "Xe=%%i,Ye=%%j,POINT[%%i][%%j]=8")
		for %%P in (!POINT[%%i][%%j]!) do (
			set "DISPLAY[%%j]=!DISPLAY[%%j]!!P%%P!"
		)
	)
	set "MapData=!MapData:~%MapWidth%!"
)
set/a "SS=POINT[%Xe%][%Ye%],dx=(8-(SS|1))*(SS&1),dy=(8-(SS|1))*((SS^1)&1)"
set/a "Xo=7,Yo=3,POINT[7][13]=11,LEVEL=1,Add=11"

::****************主体程序******************
:MAIN
REM 绘图引擎
if !F1! equ 1 (2>nul echo 	!SPACE!&set/p=<NUL) else cls
echo                                       [LEVEL !LV!]  Score:!SC!
echo ┏%LINES%┓
for /l %%j in (1,1,%MapHeight%) do (if defined #%%j (echo;┃!DISPLAY[%%j]!┃&set "#%%j=") else (echo;))
echo ┗%LINES%┛
if !T! gtr 0 (for /l %%N in (1,1,!T!) do (for /l %%a in (1,1,100) do (echo;>NUL)))
:READKEY
REM 读取按键
set/p KEY=<key.ini
if "%KEY: =%"=="1" (if !dy! neq 1 (set/a "dx= 0,dy=-1,SS=8"))
if %KEY% equ 2 (if !dy! neq -1 (set/a "dx= 0,dy= 1,SS=6"))
if %KEY% equ 3 (if !dx! neq  1 (set/a "dx=-1,dy= 0,SS=9"))
if %KEY% equ 4 (if !dx! neq -1 (set/a "dx= 1,dy= 0,SS=7"))
if %KEY% equ 5 (goto READKEY)
if %KEY% equ 6 (exit)
set/a "S=POINT[%Xe%][%Ye%],Xf=X+dx,Yf=Y+dy"
REM 判断蛇的状态
if not defined POINT[%Xf%][%Yf%] (
	color C0&ping -n 2 127.1 >NUL&goto DISRAM
)
if !POINT[%Xf%][%Yf%]! lss 10 (
	if !POINT[%Xf%][%Yf%]! gtr 5 (
		color 50&ping -n 2 127.1 >NUL&goto DISRAM
	)
)
set/a "POINT[!Xe!][!Ye!]=0,POINT[!X!][!Y!]=SS,Mark=POINT[!Xf!][!Yf!]"
REM 数据处理单元
if !dy! neq 0 (
	for /l %%j in (!Y!,!dy!,!Yf!) do (
		set "DISPLAY[%%j]="
		set "#%%j=1"
		if !Yf! equ %%j (set POINT[%X%][%%j]=3)
		for /l %%i in (1,1,%MapWidth%) do (
			for %%P in (!POINT[%%i][%%j]!) do (
				set DISPLAY[%%j]=!DISPLAY[%%j]!!P%%P!
			)
		)
	)
) else (
	for /l %%j in (!Y!,1,!Y!) do (
		set "DISPLAY[%%j]="
		set "#%%j=1"
		for /l %%i in (1,1,%MapWidth%) do (
			if !Xf! equ %%i (set POINT[%%i][%Y%]=3)
			for %%P in (!POINT[%%i][%%j]!) do (
				set DISPLAY[%%j]=!DISPLAY[%%j]!!P%%P!
			)
		)
	)
)
if !Mark! lss 10 ( 
	for /l %%j in (!Ye!,1,!Ye!) do (
		set "DISPLAY[%%j]="
		set "#%%j=1"
		for /l %%i in (1,1,%MapWidth%) do (
			for %%P in (!POINT[%%i][%%j]!) do (
				set DISPLAY[%%j]=!DISPLAY[%%j]!!P%%P!
			)
		)
	)
	set/a "Xe+=(8-(S|1))*(S&1),Ye+=(8-(S|1))*((S^1)&1)"
) else (
	set/a "POINT[!Xe!][!Ye!]=S,SC+=Add,TP=LV*50,Mark1=1"
	if !SC! gtr !TP! (set/a "LV+=1,T-=1")
)
REM 时分复用随机
if !Mark1! equ 1 (
	for /l %%i in (1,1,30) do (
		if !POINT[%Xo%][%Yo%]! neq 0 (
			set/a "Xo=1+!random!%%MapHeight,Yo=1+!random!%%MapWidth"
		)	
	)
	if !POINT[%Xo%][%Yo%]! equ 0 (
		set/a "POINT[!Xo!][!Yo!]=!random!%%8+10,Add=POINT[!Xo!][!Yo!],Mark1=0"
	)
)
set/a "X=Xf,Y=Yf"
goto MAIN