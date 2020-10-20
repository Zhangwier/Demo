@echo off
setlocal enabledelayedexpansion

:ctr_all   ::全局开关___可调控
set "f1=1"::是否图像化,未启用 
set "f2=1"::是否跳过开始动画
set "f3=0"::是否开启作弊模式
set "f4=0"::
set "f5=1"::
set "f6=0"::是否自动检测更新,未启用 
set "f7=0"::是否开启管理员权限,未启用 

:num_all  ::全局数据__可调控
set "v=0.1"::版本号
set "address_account_am=mylog.txt" ::Automated management







:begin_all ::全局初始化
mode con cols=85 lines=21
color 0a

:ctr_all_main ::全局开关设置
if %f2% == 1 goto password_begin else call :Opening animation



::-----------------------------------------------------------------------------账号登入
:password_begin ::初始化
title 登入程序
set txt=输入账号...
set password_x=1
set num=
set password=
set code_1=
set code_1_len=0
set code_2=
set code_2_len=0
set code_22=

:password_f3 ::自动登入模块
for /f %%i in (%address_account_am%) do (set "%%i")
if %mylog_0% == 1 (
    set "code_1=!mylog_00!"
    for /f %%i in (!code_1!.txt) do (set "%%i")
    goto password_pass
    )

:password_main ::主程序
call :password_map
call :password_main_map
choice /c:wshj0123456789 /m:"please select"
if %errorlevel%==1 if %password_x% NEQ 1 set /a password_x-=1
if %errorlevel%==2 if %password_x% NEQ 4 set /a password_x+=1
if %errorlevel%==3 call :password_t
if %errorlevel%==4 call :password_d
if %errorlevel%==5 call :password_log 0
if %errorlevel%==6 call :password_log 1
if %errorlevel%==7 call :password_log 2
if %errorlevel%==8 call :password_log 3
if %errorlevel%==9 call :password_log 4
if %errorlevel%==10 call :password_log 5
if %errorlevel%==11 call :password_log 6
if %errorlevel%==12 call :password_log 7
if %errorlevel%==13 call :password_log 8
if %errorlevel%==14 call :password_log 9
goto password_main

:password_map_b 图像初始化
set code_3=□
set code_4=
set code_5=
set code_6=□
goto:eof

:password_map ::图标变换
call :password_map_b
if %password_x% == 1 set "code_4=_"&&set txt=输入账号...
if %password_x% == 2 set "code_5=_"&&set txt=输入密码...
if %password_x% == 3 set code_3=■
if %password_x% == 4 set code_6=■
goto:eof

:password_main_map ::图像显示
cls
echo.
echo 时间：%time% 日期：%date%
echo 账号:%code_1%%code_4%
echo 密码:%code_22%%code_5%
echo 登入 %code_3%
echo 注册 %code_6%
echo 状态: %txt%
echo w:向上  s:向下  h:确定  j:删除
goto:eof

:password_log ::数字输入
if %password_x% == 1 (
    set "code_1=%code_1%%1"
    set /a "code_1_len+=1"
    )
if %password_x% == 2 (
    set "code_2=!code_2!%1"
    set "code_22=!code_22!*"
    set /a "code_2_len+=1"
    )
goto:eof

:password_t
if %code_1_len% == 0 set "txt=请输入账号"&&goto:eof
if %code_2_len% == 0 set "txt=请输入密码"&&goto:eof
if %password_x% == 3 (
    for %%i in (*.txt) do (
        if %%i == %code_1%.txt goto password_t_1
        )
    set txt=账号不存在!
    goto:eof
    :password_t_1
    for /f %%i in (%code_1%.txt) do set "%%i"
    if %code_2% == %password% goto password_t_2
    set txt=密码错误!
    goto:eof
    :password_t_2
    goto password_pass
    )
if %password_x% == 4 (
    echo num=%code_1% > %code_1%.txt
    echo password=%code_2% >> %code_1%.txt
    goto password_pass
    )
goto:eof

:password_d
if %password_x% == 1 (
    if %code_1_len% == 0 goto:eof
    set code_1=%code_1:~0,-1%
    set /a "code_1_len-=1"
    )
if %password_x% == 2 (
    if %code_2_len% == 0 goto:eof
    set code_2=%code_2:~0,-1%
    set code_22=%code_22:~0,-1%
    set /a "code_2_len-=1"
    )
goto:eof

:password_pass ::账号通过_初始化
set txt=程序已开放，欢迎使用
set password_x=1
set "password_f1=0" ::记住账号
set "password_f2=0" ::记住密码
set "password_f3=0" ::自动登入
if %mylog_0% == 1 (if %mylog_00% == %code_1% set "password_f3=1")
for /l %%i in (1,1,%mylog_num_max%) do (
    if !mylog_%%i! == %code_1% (
        set "password_f1=1"
        if !mylog_%%i_f2! == 1 set "password_f2=1"
        )
    )
set "pass_max_code=6" ::操作最大数
goto password_main_2

:password_main_2 ::账号通过_主控程序
call :password_map2
call :password_main_map2
choice /c:wsh
if %errorlevel% == 1 if %password_x% neq 1 set /a password_x-=1
if %errorlevel% == 2 if %password_x% neq %pass_max_code% (set /a password_x+=1)
if %errorlevel% == 3 call :password_pass_t
for /f %%i in (%address_account_am%) do (set "%%i")
goto password_main_2

:password_map_b2 图像初始化
set /a t="%pass_max_code%+2"
for /l %%i in (3,1,!t!) do set "code_%%i=□"
::set code_3=□
::set code_4=□
::set code_5=□
::set code_6=□
::set code_7=□
::set code_8=□
goto:eof

:password_map2 ::图标变换
call :password_map_b2
if %password_f1% == 1 set code_4=●
if %password_f2% == 1 set code_5=●
if %password_f3% == 1 set code_6=●
if %password_x% == 1 set code_3=■
if %password_x% == 2 set code_4=■
if %password_x% == 3 set code_5=■
if %password_x% == 4 set code_6=■
if %password_x% == 5 set code_7=■
if %password_x% == 6 set code_8=■
goto:eof

:password_main_map2 ::图像显示
cls
echo.
echo 时间：%time% 日期：%date%
echo 状态: %txt%
echo 修改密码 %code_3%
echo 记住账号 %code_4%
echo 记住密码 %code_5%
echo 自动登入 %code_6%
echo 进入游戏 %code_7%
echo 退出账号 %code_8%
echo w:向上  s:向下  h:确定
goto:eof

:password_pass_t
if %password_x% == 1 (
    set /p code_2= 请输入想要修改的密码:
    echo password=%1 >> %code_1%.txt
    set "txt=密码修改成功!"
    goto:eof
    )
if %password_x% == 2 (
    if %password_f1% == 0 (
        set password_f1=1
        set /a "mylog_num_max=!mylog_num_max!+1"
        echo mylog_!mylog_num_max!=%code_1% >> %address_account_am%
        echo mylog_!mylog_num_max!_f2=%password_f2% >> %address_account_am%
        echo mylog_num_max=!mylog_num_max! >> %address_account_am%
        set "txt=保存成功"
        goto:eof
        )
    echo mylog_0=%mylog_0% > %address_account_am%
    echo mylog_00=%mylog_00% >> %address_account_am%
    if %mylog_00% == %code_1% (
        echo mylog_0=0 >> %address_account_am%
        echo mylog_00=0 >> %address_account_am%
        )
    for /l %%i in (1,1,%mylog_num_max%) do (
        if !mylog_%%i! neq %code_1% (
            echo mylog_%%i=!mylog_%%i! >> %address_account_am%
            echo mylog_%%i_f2=!mylog_%%i_f2! >> %address_account_am%
            )
        if !mylog_%%i! == %code_1% (
            set /a t=%%i+1
            for /l %%j in (%t%,1,%mylog_num_max%) do (
                set /a tt=%%j-1
                echo mylog_%tt%=!mylog_%%i! >> %address_account_am%
                echo mylog_%tt%_f2=!mylog_%%i_f2! >> %address_account_am%)
            )
        )
    set password_f1=0
    set password_f2=0
    set password_f3=0
    set /a "mylog_num_max-=1"
    echo mylog_num_max=!mylog_num_max! >> %address_account_am%
    set txt=账号已遗忘!
    goto:eof
    )
if %password_x% == 3 (
    if %password_f2% == 1 (
        set "password_f2=0"
        for /l %%i in (1,1,%mylog_num_max%) do (
            if !mylog_%%i! == %code_1% (
                echo mylog_%%i_f2=0 >> %address_account_am%
                )
            )
        set txt=密码已遗忘!
        if %mylog_00% == %code_1% (
            echo mylog_00=0 >> %address_account_am%
            echo mylog_0=0 >> %address_account_am%
            set txt=密码已遗忘!自动登入已取消!
            )
        goto:eof
        )
    for /l %%i in (1,1,!mylog_num_max!) do if !mylog_%%i! == %code_1% (
        echo mylog_%%i_f2=1 >> %address_account_am%
        set txt=密码保存成功!
        set "password_f2=1"
        goto:eof
        )
    set "txt=请先保存账号!"
    goto:eof
    )
if %password_x% == 4 (
    if %password_f3% == 1 (
        set "password_f3=0"
        set txt=自动登入已取消!
        echo mylog_0=0 >> %address_account_am%
        echo mylog_00=0 >> %address_account_am%
        goto:eof
        )
    for /l %%i in (1,1,%mylog_num_max%) do if !mylog_%%i! == %code_1% (
        if !mylog_%%i_f2! == 1 (
            set password_f3=1
            echo mylog_0=1 >> %address_account_am%
            echo mylog_00=%code_1% >> %address_account_am%
            set "txt=自动登入设置成功!"
            goto:eof
            )
        set txt=请先保存密码!
        goto:eof
        )
    set txt=请先保存账号!
    goto:eof
    )
if %password_x% == 5 goto game
if %password_x% == 6 (
    set txt=退出账号成功!
    goto password_begin
    )

::---------------------------------------------------------------------------------游戏
:game ::数据初始化
mode con cols=65 lines=20
title 测试版v0.1
color e0
goto begin


:begin ::初始化
set "ELEMENTS=-+○●□■☉⊕Θ★☆╳※▓◆" ::可用皮肤
set "max_view_w=9" ::最大视宽
set "max_view_h=9" ::最大视长
set "max_anim=20" ::最大生物容量
set "max_move_all=20" ::最大动态生物容量
set "max_mod=1" ::最大mod数
set "max_ctrs=6" ::最大按键数
set "max_num=12" ::最大生物词条
set "max_car=7" ::最大载具词条
set "max_goods=10" ::最大物品词条
set "move_all=0"
set "num_anim_bad=0"
set "mave_all=1"
call :game_anim_buil_begin ::默认生物设置
call :game_mod_bg ::mod初始化
call :map_s ::地图初始化
call :man_s ::主角初始化
call :ctr_s ::按键初始化
call :renew_all ::动画加载
goto main

:main ::主显
cls
call :renew_all
echo 当前坐标:x !A%num%_2!  y !A%num%_3!
for /l %%i in (1,1,%max_view_h%) do (
    set "p[%%i]= "
    for /l %%j in (1,1,%max_view_w%) do (
    for %%k in (!FO%%j%%i!) do set "p[%%i]=!p[%%i]!%%k"
    ))
for /l %%j in (%max_view_h%,-1,1) do echo !p[%%j]!
call :ctrl ::玩家操作
call :game_anim ::生物生成
call :game_move_all ::生物运动
goto main

:ctrl ::主控制键
choice /c:%f1%%f2%%f3%%f4%%f5%%f6% /m:"please select"
if %errorlevel%==1 call :move %num% 1
if %errorlevel%==2 call :move %num% 2
if %errorlevel%==3 call :move %num% 3
if %errorlevel%==4 call :move %num% 4
if %errorlevel%==5 call:begin
if %errorlevel%==6 call:ctr_x
call :renew_all
goto:eof

::---------------------------------------初始化
:game_mod_bg ::mod初始化
set "game_mod_1=0" ::1碰撞识别
goto:eof

:map_s ::地图初始化
for /l %%i in (1,1,%max_view_w%) do (
             for /l %%j in (1,1,%max_view_w%) do set /a "IO%%i%%j=0"
             )
goto:eof

:renew_all ::动画加载
For /l %%i in (1,1,%max_view_w%) do (
    For /l %%j in (1,1,%max_view_h%) do (
        set "FO%%i%%j=-"
        set "renew_all_t=!IO%%i%%j!"
        set "renew_all_tt=A!renew_all_t!_1"
        for %%k in (!renew_all_tt!) do (
            set "renew_all_ttt=!%%k!"
            if !renew_all_ttt! == 1 set "FO%%i%%j=+"
            if !renew_all_ttt! == 0 set "FO%%i%%j=-"
            if !renew_all_ttt! == 2 set "FO%%i%%j=o"
            if !renew_all_ttt! == 3 set "FO%%i%%j=o"
            )
        )
    )
GOTO:EOF

:man_s ::主角初始化
set num=%code_1%
set "IO11=%num%"
set "A%num%_0="
set "A%num%_1=1"
set "A%num%_2=1"
set "A%num%_3=1"
set "A%num%_4=呆瓜"
set "A%num%_5=100"
set "A%num%_6=100"
set "A%num%_7=100"
set "A%num%_8=0"
set "A%num%_9=0"
set "A%num%_10=0"
set "A%num%_11=0"
set "A%num%_12=0"
goto:eof

:ctr_s ::按键初始化
set f1=w
set f1_s=向上移动
set f2=s
set f2_s=向下移动
set f3=a
set f3_s=向左移动
set f4=d
set f4_s=向右移动
set f5=r
set f5_s=游戏初始化
set f6=o
set f6_s=按键修改
goto:eof

::--------------------------------------按键功能库
:ctr_x ::按键修改
cls
for /l %%i in (1,1,%max_ctrs%) do (
    echo %%i !f%%i_s! : !f%%i!
    )
set /p t=输入对应序号进行修改(输入0退出)
if %t% GEQ 1 (
    if %t% LEQ %max_ctrs% (
    set /p tt=输入按键
    set f!t!=!tt!
    echo 修改成功!
    pause>null
    ))
if %t% == 0 goto:eof
goto ctr_x

:game_seave ::存档
echo num=%num% > %num%.txt
echo password=%password% >> %num%.txt
for /l %%i in (1,1,%max_num%) echo %num%_%%i=!%num%_%%i! >> %num%.txt
for /l %%i in (1,1,%max_ctrs%) echo f%%i=!f%%i! >> %num%.txt
echo 保存成功！
pause>null
goto:eof

::-------------------------------------动态控制

:game_anim ::生物生成
if %num_anim_bad% neq 0 goto:eof
call :game_anim_bad
goto:eof

:game_anim_bad ::敌对生成
set /a r_w=%RANDOM%%%!max_view_w!+1
set /a r_h=%RANDOM%%%!max_view_h!+1
if !IO%r_w%%r_h%! == 0 call :game_anim_buil %r_w% %r_h% 2 else goto game_anim_bad
set /a num_anim_bad+=1
set /a move_all+=1
set "B%move_all%_num=%game_name_r%"
goto:eof

:game_anim_buil ::生物设置
call :game_name_ram
set "IO%2%3=%game_name_r%"
for /l %%i in (1,1,%max_num%) do (
   for %%j in (A%3_%%i) do (
        set "A!IO%2%3!_%%i=!%%j!"
        )
    )
goto:eof

:game_goods_buil ::物品设置
call :game_name_ram
set "IO%2%3=%game_name_r%"
for /l %%i in (1,1,%max_num%) do (
   for %%j in (game_goods_%3_%%i) do (
        set "A!IO%2%3!_%%i=!%%j!"
        )
    )
goto:eof

:game_car_buil ::载具设置
call :game_name_ram
set "IO%2%3=%game_name_r%"
for /l %%i in (1,1,%max_num%) do (
   for %%j in (game_car_%3_%%i) do (
        set "A!IO%2%3!_%%i=!%%j!"
        )
    )
goto:eof

:game_name_ram ::生物辨识码生成
set /a game_name_r=%random%%%10
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
set /a t="%random%%%10"
set game_name_r=!game_name_r!%t%
goto:eof

:game_move_all  ::主动控制
for /l %%I in (1,1,%move_all%) do call:ai_move !B%move_all%_num!
goto:eof

:ai_move ::ai移动判断
if !A%1_1:~1,1! == 1 (
   if !A%1_10! neq 0 (
        call :ai_move_track %1 !B%1_10! 1
        goto:eof
        )
    call :r_move %1
    )
goto:eof

:ai_move_track ::目标距离判断
pause
set /a ai_move_track_dx=!A%1_2!-!A%2_2!
set /a ai_move_track_dx=!A%1_3!-!A%2_3!
if %ai_move_track_dx% geq 0 (
    if %ai_move_track_dy% geq 0 (
        set /a ai_move_judge=ai_move_track_dx-ai_move_track_dy
        if %ai_move_judge% geq 0 set ai_move_judge=2 else set ai_move_judge=3
        )
    if %ai_move_track_dy%  0 lss 0 (
        set /a ai_move_judge=ai_move_track_dx+ai_move_track_dy
        if %ai_move_judge% geq 0 set ai_move_judge=1 else set ai_move_judge=3
        )
    )
if %ai_move_track_dx% lss 0 (
    if %ai_move_track_dy% geq 0 (
        set /a ai_move_judge=ai_move_track_dx+ai_move_track_dy
        if %ai_move_judge% geq 0 set ai_move_judge=4 else set ai_move_judge=2
        )
    if %ai_move_track_dy%  0 lss 0 (
        set /a ai_move_judge=ai_move_track_dx-ai_move_track_dy
        if %ai_move_judge% geq 0 set ai_move_judge=4 else set ai_move_judge=1
        )
    )
if %3 == 0 (
    if %ai_move_judge% == 1 set ai_move_judge=2
    if %ai_move_judge% == 2 set ai_move_judge=1
    if %ai_move_judge% == 4 set ai_move_judge=3
    if %ai_move_judge% == 3 set ai_move_judge=4
    )
goto:eof

:r_move ::随机移动
set /a r_move_f=%RANDOM%%%4+1
call :move %1 %r_move_f%
goto :eof

:move ::行动
call :pmove %2 !A%1_2! !A%1_3!
if %tmove% == 1 (
    set IO!A%1_2!!A%1_3!=0
    set A%1_2=%pti%
    set A%1_3=%ptj%
    set "IO!A%1_2!!A%1_3!=1"
    )
goto:eof

:pmove ::行动预处理
set tmove=0
set pti=%2
set ptj=%3
if %1 == 1 set /a ptj+=1
if %1 == 2 set /a ptj-=1
if %1 == 3 set /a pti-=1
if %1 == 4 set /a pti+=1
if !IO%pti%%ptj%! == 0 set tmove=1
if %ptj% gtr %max_view_h% set tmove=0
if %pti% gtr %max_view_w% set tmove=0
if %ptj% leq 0 set tmove=0
if %pti% leq 0 set tmove=0
if %game_mod_1% == 1 (if %tmove% == 0 call :game_mod_1 %pti% %ptj%)
goto:eof

::-----------------------------------数据库

:game_anim_buil_begin ::生物

::-----------------空气
set "A0_0=0"
set "A0_1=0"
set "A0_2="
set "A0_3="
set "A0_4=死"
set "A0_5=0"
set "A0_6=0"
set "A0_7=0"
set "A0_8=0"
set "A0_9=0"
set "A0_10=0"
set "A0_11=0"
set "A0_12=0"

::-----------------jok
set "A1_0=0"
set "A1_1=24"
set "A1_2="
set "A1_3="
set "A1_4=jok"
set "A1_5=100"
set "A1_6=100"
set "A1_7=100"
set "A1_8=0"
set "A1_9=0"
set "A1_10=%num%"
set "A1_11=0"
set "A1_12=0"

::-----------------普通敌对npc
set "A2_0=0"
set "A2_1=41"
set "A2_2="
set "A2_3="
set "A2_4=西瓜"
set "A2_5=100"
set "A2_6=100"
set "A2_7=100"
set "A2_8=0"
set "A2_9=0"
set "A2_10=%num%"
set "A2_11=0"
set "A2_12=0"

::-----------------普通npc
set "A3_0=0"
set "A3_1=31"
set "A3_2="
set "A3_3="
set "A3_4=香瓜"
set "A3_5=100"
set "A3_6=100"
set "A3_7=100"
set "A3_8=0"
set "A3_9=0"
set "A3_10="
set "A3_11=0"
set "A3_12=0"

goto:eof

:game_anim_buil_begin_car ::载具设置

::-------------原型车
set game_car_1_1=助推器
set game_car_1_2=2
set game_car_1_3=0
set game_car_1_4=0
set game_car_1_5=3
set game_car_1_6=1
set game_car_1_7=0
set game_car_2_1=四轮车
set game_car_2_2=2
set game_car_2_3=0
set game_car_2_4=1
set game_car_2_5=10
set game_car_2_6=4
set game_car_2_7=0
set game_car_3_1=巴士
set game_car_3_2=2
set game_car_3_3=0
set game_car_3_4=2
set game_car_3_5=10
set game_car_3_6=4
set game_car_3_7=0

::---------------改装车
set game_car_11_1=单人作战机甲
set game_car_11_2=2
set game_car_11_3=1
set game_car_11_4=0
set game_car_11_5=8
set game_car_11_6=1
set game_car_11_7=0
set game_car_21_1=装甲车
set game_car_21_2=2
set game_car_21_3=1
set game_car_21_4=1
set game_car_21_5=15
set game_car_21_6=4
set game_car_21_7=0
set game_car_31_1=反恐装甲
set game_car_31_2=2
set game_car_31_3=1
set game_car_31_4=1
set game_car_31_5=20
set game_car_31_6=4
set game_car_31_7=1

goto:eof

:game_anim_buil_begin_goods ::物品设置
::----------------物品原型
set game_goods_1_1=小石块
set game_goods_1_2=1
set game_goods_1_3=0
set game_goods_1_4=0
set game_goods_1_5=1
set game_goods_1_6=1
set game_goods_1_7=1
set game_goods_1_8=3
set game_goods_1_9=0
set game_goods_1_10=0
set game_goods_2_1=长剑
set game_goods_2_2=1
set game_goods_2_3=1
set game_goods_2_4=0
set game_goods_2_5=4
set game_goods_2_6=20
set game_goods_2_7=2
set game_goods_2_8=0
set game_goods_2_9=0
set game_goods_2_10=0
set game_goods_3_1=背包
set game_goods_3_2=0
set game_goods_3_3=0
set game_goods_3_4=1
set game_goods_3_5=1
set game_goods_3_6=-1
set game_goods_3_7=0
set game_goods_3_8=5
set game_goods_3_9=0
set game_goods_3_10=0

::----------------物品改装
set game_goods_1_1=子弹
set game_goods_1_2=2
set game_goods_1_3=0
set game_goods_1_4=0
set game_goods_1_5=1
set game_goods_1_6=1
set game_goods_1_7=5
set game_goods_1_8=4
set game_goods_1_9=0
set game_goods_1_10=0
set game_goods_2_1=激光剑
set game_goods_2_2=1
set game_goods_2_3=0
set game_goods_2_4=0
set game_goods_2_5=5
set game_goods_2_6=20
set game_goods_2_7=3
set game_goods_2_8=0
set game_goods_2_9=0
set game_goods_2_10=0
set game_goods_3_1=登山包
set game_goods_3_2=0
set game_goods_3_3=0
set game_goods_3_4=2
set game_goods_3_5=1
set game_goods_3_6=-1
set game_goods_3_7=1
set game_goods_3_8=5
set game_goods_3_9=0
set game_goods_3_10=0

goto:eof



::---------------------------------------mod库
:game_mod_1 ::目标识别
echo !IO%1%2!
goto:eof










::---------------------------------------------------------------------------通用函数
:abs ::绝对值
if %2 lss 0 set /a %1=-%2
goto:eof










::----------------------------------------------------------------------------代码世界
:Opening animation
mode con cols=85 lines=21
color 0a
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
goto password_begin
goto:eof