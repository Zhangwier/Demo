@Echo off
If "%1"=="" Start /b "" %0 a&Exit
Setlocal EnableDelayedExpansion
Title MapEdit v1.0  by yslyxqysl

Call :SetLv
Call :SetSize
Call :Clean
Set btn=0
Set /a ChoX=1,ChoY=1
Set /a ManX=1,ManY=1
Set /a EndX=!row!,EndY=!line!
Set /a tp=!ManX!-1
For %%i in (!ManX!) do For %%j in (!ManY!) do For %%k in (!tp!) do (
 Set "z%%j=!z%%j:~0,%%k!♀!z%%j:~%%i!"
)
Set /a tp=!EndX!-1
For %%i in (!EndX!) do For %%j in (!EndY!) do For %%k in (!tp!) do (
 Set "z%%j=!z%%j:~0,%%k!★!z%%j:~%%i!"
)
Goto Edit

::-------------Edit--------------
:Edit
Cls & For /l %%k in (1 1 %line%) do Set /p "=█"<nul
Echo ██
For /l %%j in (1 1 %line%) do echo █!z%%j!█
For /l %%k in (1 1 %line%) do Set /p "=█"<nul
Echo ██
Echo W A S D  上 下 左 右
Echo H J K L  空 墙 按钮 提示
Echo T    退出     M    菜单     N    事件
Echo O    起点     P    终点
Echo !choX! !choY!
Choice /c wasdhjkltmnop /n>nul
Set err=!ErrorLevel!
If !err!==1 If !choY! neq 1 Set /a choY-=1
If !err!==2 If !choX! neq 1 Set /a choX-=1
If !err!==3 If !choY! neq %row% Set /a choY+=1
If !err!==4 If !choX! neq %line% Set /a choX+=1
If %btn%==0 (
 If "!choX!,!choY!" neq "!ManX!,!ManY!" If "!choX!,!choY!" neq "!EndX!,!EndY!" (
  Set /a "tp=!choX!-1"
  For %%i in (!choX!) do For %%j in (!choY!) do For %%k in (!tp!) do (
   If !err!==5 Set "z%%j=!z%%j:~0,%%k!　!z%%j:~%%i!"
   If !err!==6 Set "z%%j=!z%%j:~0,%%k!█!z%%j:~%%i!"
   If !err!==7 Set "z%%j=!z%%j:~0,%%k!☉!z%%j:~%%i!"
   If !err!==8 Set "z%%j=!z%%j:~0,%%k!▓!z%%j:~%%i!"
  )
 )
) else (
 If !err!==6 Set "Str="
)
If !err!==9 (
 Choice /c ync /n /m "保存？[Y,N,C]"
 If !ErrorLevel! equ 1 Call :Save
 If !ErrorLevel! equ 3 (Goto Edit) else Exit
)
If !err!==10 Goto Menu
If !err!==11 Set "btn=1" & Set Sub
If !err!==12 (
 If "!choX!,!choY!" neq "!End!" (
  Set "z!tp:~1!=♀"
  Set "z!Man!=　"
  Set "Man=!choX!,!choY!"
 )
)
If !err!==13 (
 If "!choX!,!choY!" neq "!Man!" (
  Set /a tp=!choX!-1
  For %%i in (!choX!) do For %%j in (!choY!) do For %%k in (!tp!) do (
   Set "z%%j=!z%%j:~0,%%k!★!z%%j:~%%i!"
  )
  Set /a tp=!EndX!-1
  For %%i in (!EndX!) do For %%j in (!EndY!) do For %%k in (!tp!) do (
   Set "z%%j=!z%%j:~0,%%k!　!z%%j:~%%i!"
  )
  Set /a "EndX=!choX!,EndY=!choY!"
 )
)
Goto Edit
::-------------Edit--------------

::-------------Menu--------------
:Menu
Cls
Echo 新建(N)  打开(O)  保存(S)
Echo 属性(P)  清空(C)  返回(Q)
Choice /c nospcq /n>nul
If %ErrorLevel%==1 (
 Choice /c ync /n /m "保存？[Y,N,C]"
 If !ErrorLevel! equ 1 Call :Save
 If !ErrorLevel! equ 3 (Goto Menu) else Goto SetLv
)
If %ErrorLevel%==2 (
 Choice /c ync /n /m "保存？[Y,N,C]"
 If !ErrorLevel! equ 1 Call :Save
 If !ErrorLevel! equ 3 (Goto Menu) else Call :open
 Goto Edit
)
If %ErrorLevel%==3 Call :Save & Goto Edit
If %ErrorLevel%==4 Goto Property
If %ErrorLevel%==5 Call :Clean & Goto Edit
If %ErrorLevel%==6 Goto Edit
::-------------Menu--------------

::----------Properties-----------
:Property
Cls
Echo 更改关数(L)  更改地图大小(S)
Echo 返回菜单(B)  返回界面(Q)
Choice /c lsbq /n
If %ErrorLevel%==1 Call :SetLv & Goto Edit
If %ErrorLevel%==2 Call :SetSize & Goto Edit
If %ErrorLevel%==3 Goto Menu
If %ErrorLevel%==4 Goto Edit
::----------Properties-----------

::-----------Functions-----------
:SetLv
Cls & Set "lv=" & Set /p "lv=请输入地图所在关卡："
Echo "!lv!"|FindStr "^.[1-9][0-9]*.$">nul||Goto SetLv
Goto :eof

:SetSize
Cls & Set "size=" & Set /p "size=请输入地图大小[排,列]："
Echo "!size!"|FindStr "^.[0-9][0-9]*\,[0-9][0-9]*.$">nul||Goto SetSize
For /f "tokens=1,2 Delims=," %%a in ("%size%") do (
 For /f "tokens=* Delims=0" %%i in ("%%a") do Set row=%%i
 For /f "tokens=* Delims=0" %%j in ("%%b") do Set line=%%j
)
Goto :eof

:Clean
For /l %%i in (1 1 %row%) do (
 Set "z%%i="
 For /l %%j in (1 1 %line%) do Set "z%%i=!z%%i!　"
)
Goto :eof

:Open
Set /p "lv=选择关数："
Echo "!lv!"|FindStr "^.[0-9]*.$">nul||Goto Open
If not exist level!lv!.txt Goto Open

Goto :eof

:Save
(
Cls & For /l %%k in (1 1 %line%) do Set /p "=█"<nul
Echo ██
For /l %%i in (1 1 %row%) do (
 Set /p "=█"<nul
 For /l %%j in (1 1 %line%) do Set /p "=!z%%i,%%j!"<nul
 Echo █
)
For /l %%k in (1 1 %line%) do Set /p "=█"<nul
Echo ██
)>level!lv!.txt
Goto :eof
::-----------Functions-----------