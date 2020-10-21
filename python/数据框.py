import random as rd
import re
import turtle
import xeger
import faker

#随机值产生(函数规则) -doing
def rul_dat(rul):
    if rul == 'none':
        return 'none'
    elif rul == 'name':
        return randname()
    elif rul == 'Name':
        return randname(1)
    elif rul[:5] == '''f(x)=''':
        return 0
    else :
        try:
            _x = xeger.Xeger()
            return _x.xeger(rul)
        except:
            return 'none'
def randname(t=0):
    max_randname=7
    name_list=["ann",'smith','johnson','davis','wilson','taylor','thomas']
    rname=name_list[rd.randint(0,max_randname-1)]
    if t == 1:
        rname[0]=chr(ord(rname[0])-32)
    return rname
#构图 -doing
def rgo(n,r=90,t=0):
    turtle.right(r)
    if t==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.fd(n)
    turtle.right(-r)
    turtle.pendown()
def pgoto(x,y):
    turtle.pendown()
    turtle.goto(x,y)
def pup(n):
    turtle.penup()
    turtle.fd(n)
    turtle.pendown()
def pbeg():
    turtle.setpos(0,0)
    turtle.clear()
    turtle.seth(0)
    turtle.penup()
    turtle.goto(-200,-200)
    move=((-200,300),(-200,-200),(300,-200),(-200,-200))
    for i in move:#绘制坐标轴
        pgoto(i[0],i[1])
def plot(x,y,xlab='none',ylab='none',w=0):
    pbeg()
    if xlab == 'none':
        xlab = x
    if ylab == 'none':
        ylab = y
    turtle.right(-90)
    turtle.goto(-220,-200)
    for i in range(11):#纵坐标
        txt=i*50/500*(max(y)-min(y))+min(y)
        turtle.pendown()
        turtle.write(txt)
        turtle.penup()
        turtle.fd(50)
    goto(-170,-220)
    for i in range(len(x)):#横坐标
        turtle.seth(90)
        turtle.pendown()
        turtle.write(xlab[i])
        pup(20)
        turtle.fd((y[i]-min(y))/(max(y)-min(y))*500)
        pup(10)
        turtle.write(ylab[i])
        turtle.penup()
        turtle.fd(-(y[i]-min(y))/(max(y)-min(y))*500-30)
        turtle.right(90)
        turtle.fd(500/len(x))
def hist(x,y,w=10,xlab='none',ylab='none'):
    pbeg()
    if xlab == 'none':
        xlab = x
    if ylab == 'none':
        ylab = y
    turtle.right(-90)
    turtle.goto(-220,-200)
    for i in range(11):#纵坐标
        txt=i*50/500*(max(y)-min(y))+min(y)
        turtle.pendown()
        turtle.write(txt)
        turtle.penup()
        turtle.fd(50)
    goto(-170,-220)
    for i in range(len(x)):#横坐标
        turtle.seth(90)
        turtle.pendown()
        turtle.write(xlab[i])
        pup(20)
        rgo(w/2,-90)
        turtle.fd((y[i]-min(y))/(max(y)-min(y))*500)
        pup(10)
        rgo(w/2,90)
        turtle.write(ylab[i])
        pup(-10)
        rgo(w/2,-90)
        rgo(w,90,1)
        turtle.pendown()
        turtle.fd(-(y[i]-min(y))/(max(y)-min(y))*500)
        turtle.penup()
        turtle.fd(-20)
        rgo(w/2,-90)
        turtle.penup()
        turtle.right(90)
        turtle.fd(500/len(x))
def plots(x,y,xlab='none',ylab='none'):
    pbeg()
    if xlab == 'none':
        xlab = x
    if ylab == 'none':
        ylab = y
    turtle.right(-90)
    turtle.goto(-220,-200)
    for i in range(11):#纵坐标
        txt=i*50/500*(max(y)-min(y))+min(y)
        turtle.pendown()
        turtle.write(txt)
        turtle.penup()
        turtle.fd(50)
    goto(-170,-220)
    turtle.seth(0)
    for i in range(len(x)):#横坐标
        turtle.pendown()
        turtle.write(xlab[i])
        turtle.penup()
        turtle.fd(500/len(x))
    turtle.penup()
    turtle.goto(-200+i*500/len(x)+30,-200+(y[i]-min(y))/(max(y)-min(y))*500)
    turtle.pendown()
    for i in range(len(x)):
        turtle.goto(-200+i*500/len(x)+30,-200+(y[i]-min(y))/(max(y)-min(y))*500)
#定义文件类型 -end
class file:
    def __init__(self,address):
        self.adr=address
        try:
            with open(self,mode='r') as f:
                self.line=f.readlines()
        except:
            print("error in address!")
#人 -doing
class people:
    def __init__(self,**date):
        for i in date:
            self.i=date[i]
    name=rul_dat
    age=rd.randint(1,120)
#数据框类文件 -end
class fdata(file):
    def __init__(self,file='none',druls='none',dlen='none'):
        if file != 'none':
            self.druls={}
            for i in file.line[0].append():
                self.druls[i]=none
            self.dlens={len(druls),len(file.line)-1}
            self.dlst=[]
            for i in file.line[1:]:
                self.dlst[i]={}
                t=0
                for j in druls:
                    self.dlsr[i][j]=file.lind.split()[t]
                    t+=1
        elif druls != 'none' and dlen != 'none':
            self.druls=druls
            self.dlens=dlen
            self.dlst=[]
            for i in range(dlen[1]):
                self.dlst[i]={}
                t=0
                for j in druls:
                    self.dlst[i][j]=rul_dat(druls[j])
                    t+=1
        else:
            with open("D:\\newdata.txt",mode='w') as f:
                self.adr='D:\\newdata.txt'
                self.druls={name:'name',age:'1:20'}
                self.dlens=[2,10]
                self.dlst=[]
                for i in range(10):
                    self.dlst[i]={name:rul_dat(name),age:range(1,20)}
        def rdlst(self,begin=0,end='none'):
            if end == 'none':
                end=self.dlens[1]
            for i in range(begin,end):
                self.dlst[i].clear()
                t=0
                for j in druls:
                    self.dlst[i][j]=rul_dat(druls[j])
                    t+=1
            return self
        def rtype(self,*tpname):
            for i in tpname:
                for j in range(dlens[1]):
                    self.dlst[j][i]=rul_dat(druls[i])
            return self
        def del_dlst(self,num):
            for i in range(num):
                self.dlst.pop(rd.randint(1,self.dlens[1]))
            self.dlens[1]-=num
            return self
        def del_dtype(self,*tpname):
            for i in tpname:
                self.druls.pop(i)
                for j in range(dlens(1)):
                    self.dlst[j].pop(i)
            self.dlens[0]-=len(tpname)
            return self
        def add_dlst(self,num):
            begin=self.dlens[1]
            self.dlens[1]+=num
            rdlst(self,begin,self.dlens[1])
            return self
        def add_dtype(self,*nruls):
            for i in nruls:
                self.druls[i]=nruls[i]
                rtype(self,i)
            self.dlens[1]+=len(nruls)
            return self
        def del_random(self,num='rg',tpname='alltp'):
            if num == 'rg' :
                num=int(self.dlens[1]*self.dlens[0]/10)
                if num < 0:
                    num=int(self.dlens[1]*self.dlens[0]/2)
            if tpname[0] == 'alltp' and len(tpname) == 1:
                for i in range(1,num):
                    y=rd.randint(0,self.dlens[1])
                    t=self.dlst[y].popitem()
                    self.dlst[y][t[0]]='none'
            else :
                for i in range(1,num):
                    y=rd.randint(0,self.dlens[1])
                    t=self.dlst[y].popitem()
                    while t[0] in tpname:
                        self.dlst[y][t[0]]=t[1]
                        t=self.dlst[y].popitem()
                    self.dlst[y][t[0]]='none'
            return self
        def __add__(self,other):
            self.druls.update(other.druls)
            self.dlens[0]=len(self.druls)
            self.dlens[1]=len(self.dlens[1]+other.dlens[1])
            rdlst(self)
            return self
        def __mul__(self,num):
            if re.search('\d*',num):
                add_dlst(self,num)
            return self
        def savefd(self):
            try:
                with open(self.adr,mode='w') as f:
                    count=0
                    for i in self.druls :
                        f.write("{:^8}".format(self.druls[i]))
                        count+=1
                        if count == self.dlens[0]:
                            f.write("\n")
                    for i in range(self.dlst):
                        count=0
                        for j in self.druls :
                            f.write("{:^8}".format(self.dlst[i].\
                                                 setdefault(j,'none')))
                            count+=1
                            if count == self.dlens[0] :
                                f.write('\n')
            except:
                print("error!")
        def printfd(self):
            count=0
            for i in self.druls :
                print("{:^8}".format(self.druls[i]),end='')
                count+=1
                if count == self.dlens[0]:
                    print("\n")
                for i in range(self.dlst):
                    count=0
                    for j in self.druls :
                        print("{:^8}".format(\
                            self.dlst[i].setdefault(j,'none')),end='')
                        count+=1
                        if count == self.dlens[0] :
                            print('\n')
#一维数据拟合(你是想不开了?)
def fitdt(x):
    return 'none'
#交互 -doing
def main():
    try:
        print("""{:^10}\n{:<10}\n{:<10}\n{:<10}\n"""\
              .format('请输入功能前的数据!','1:创建数据','2:读取数据','3:修改数据'))
        t=eval(input())
        key=(1,2,3)
        while t not in key:
            t=eval(input('格式错误!重新输入:'))
        if t == 1:
            ad=input("{:<10}".format('输入数据地址:'))
            try:
                with open(ad,'w') as f:
                    print('{:<10}'.format('文件创建成功'))
            except:
                print('{:<}'.format('error in build address'))
            t=input("输入所有数据种类，以空格隔开")
            d=input("""输入所有数据产生规则,以空格隔开,格式如下
1,英文姓名: name|Name (区别在于首字母是否大写)
2,中文姓名: chinaname
3,范围随机:
4,函数规则: f(x)=  (在等号后输入函数)
5,随机字符串:  (请按正则规则输入)
""")
            t=t.split()
            d=d.split()
            ru={}
            count=0
            for i in t:
                ru[i]=d[count]
                count+=1
            nm=eval(input('输入数据条数:'))
            try:
                fdata(ad,ru,nm)
            except:
                print('创建失败!')
main()