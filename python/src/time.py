import turtle as t
import time as tm
def drawcls():
    t.pencolor('gray88')
    drawdate("88888888")
    t.goto(-300,0)
def drawGap():
    t.penup()
    t.fd(5)
def drawline(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(a):
    drawline(True) if a in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if a in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if a in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if a in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if a in [0,4,5,8,9] else drawline(False)
    drawline(True) if a in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if a in [0,1,2,3,4,7,8,9] else drawline(False)
    t.right(180)
    t.penup()
    t.fd(20)
def drawdate(b):
    j=0
    drawcolor=["red","green","blue"]
    for i in b:
        if i in ["1","2","3","4","5","6","7","8","9","0"]:
            drawDigit(eval(i))
        else:
            j+=1
            t.write(i,font=("Arial",18,"normal"))
            t.pencolor(drawcolor[j])
            t.fd(40)
def main():
    t.speed(10)
    t.hideturtle()
    t.setup(800,500,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    t.pencolor("red")
    drawdate(tm.strftime('%Y年%m月%d日',tm.gmtime()))
    t.done()
main()
exit()
