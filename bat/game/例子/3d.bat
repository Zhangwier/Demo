@echo off & setlocal enabledelayedexpansion & chcp 936 & title 3D Torus Vortex
color f0

set "Path=%SystemRoot%\system32" & for /f "delims==" %%a in ('set') do if /i "%%a" neq "Path" set "%%a="

set "SIN=(t-t*t/1875*t/320000+t*t/1875*t/15625*t/16000*t/2560000-t*t/1875*t/15360*t/15625*t/15625*t/16000*t/44800000)"
set "COS=(10000-t*t/20000+t*t/1875*t/15625*t/819200-t*t/1875*t/15360*t/15625*t/15625*t/10240000+t*t/1875*t/15360*t/15625*t/15625*t/16000*t/15625*t/229376000)"
set /a "ZM=10000, p=31416, p2=62832, pn2=-62832, p#2=15708, p3#2=47124, p3#2_=p3#2-1, DEG=31416/180"

set /a "Cols=wid=330, lines=hei=130, lines_plus_1=lines+1"
mode !Cols!,!lines_plus_1!

set "TAB=	" & for /F %%a in ('"prompt $h&for %%b in (1) do rem"')do Set "BS=%%a"
set /a "buffwid = wid, linesWantBackAbove = hei - 1 + 1, cntBS = 2 + (buffwid + 7) / 8 * linesWantBackAbove"
set "BSs=" & for /L %%a in (1 1 !cntBS!) do set "BSs=!BSs!%BS%"
set "aLineBS=" & for /L %%a in (1 1 !wid!) do set "aLineBS=!aLineBS!%BS%"

set "LN0=" & for /L %%C in (1 1 !Cols!) do set "LN0= !LN0!"
for /L %%L in (1 1 !lines!) do set "LN%%L=!LN0!"


set /a "pixel_h=5, pixel_w=3" & rem 字体像素高宽比
REM zscr 屏幕 Z 轴坐标, zeye 视点 Z 轴坐标
set /a "XC = Cols/2, YC = lines/2, zscr = 108, zeye = 400, zs2e=zscr-zeye"

set /a "R1 = 64, r2 = 44, mp = 10, np = 90, Z_cut_ZM=999*ZM"  & rem Z_cut_ZM 是 平行于 xOy 平面的切割平面, 值够大时不会切割

for /l %%m in (1 1 !mp!) do (

    for /l %%n in (1 1 !np!) do (

            set /a "TH1=p2* %%m /mp+p2*%%n/np, TH1 %%= p2, TH1 += TH1>>31&p2, t=TH1, s1=(t-p#2^t-p3#2)>>31, s3=p3#2_-t>>31, t=(-t&s1)+(t&~s1)+(p&s1)+(pn2&s3), SIN_TH1=%SIN%, t=%COS%, COS_TH1=(-t&s1)+(t&~s1)"

            set /a "th2=p2*%%n/np, th2 %%= p2, th2 += th2>>31&p2, t=th2, s1=(t-p#2^t-p3#2)>>31, s3=p3#2_-t>>31, t=(-t&s1)+(t&~s1)+(p&s1)+(pn2&s3), SIN_th2=%SIN%, t=%COS%, COS_th2=(-t&s1)+(t&~s1)"

            title 3D Torus Vortex  %%m / !mp! TH1:!TH1! th2:!th2!

            set /a "z_ZM=(R1*ZM + r2*COS_th2)/ZM * SIN_TH1, z_t2eye_ZM=z_ZM -zeye*ZM, x=XC + (R1*ZM + r2*COS_th2)/ZM * COS_TH1 *zs2e* pixel_h /(z_t2eye_ZM * pixel_w), y=YC + r2 * SIN_th2 *zs2e/z_t2eye_ZM"

            set /a "inner=(th2-p#2^th2-p3#2)" & rem 到 y 轴距离 < 大圆半径 R

            if !z_ZM! LSS !Z_cut_ZM! (

                    set /a "ind=x+1, lenL=ind-1" & rem  lenR=Cols-ind"
                    for /f "tokens=1-3" %%a in ("!lenL! !ind! !y!") do (
                        if !TH1! LSS !p! (
                            if !inner! LSS 0 (  set "LN%%c=!LN%%c:~0,%%a!#!LN%%c:~%%b!"
                            ) else (            set "LN%%c=!LN%%c:~0,%%a!o!LN%%c:~%%b!"
                            )
                        ) else (
                            if !inner! LSS 0 (  set "LN%%c=!LN%%c:~0,%%a!*!LN%%c:~%%b!"
                            ) else (            set "LN%%c=!LN%%c:~0,%%a!.!LN%%c:~%%b!"
                            )
                        )
                    )
            )

            <nul set /p "=!aLineBS!" & (2>nul echo;%TAB%!BSs!) & <nul set /p "=%BS%"
            for /L %%d in (1 1 !lines!) do <nul set /p "=%BS%!LN%%d!"
    )
)
>nul pause
exit