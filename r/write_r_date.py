import random as rd
import re
import turtle
import xeger

#定义数据框(重载运算符)
class fdata:
    def rcallList(self,begin=0,end='none'):
        if end == 'none':
            end=self.len
        tlist=[]
        theaders=[]
        for i in range(begin,end):
            theaders.append(self.headers[i])
        for i in theaders:
            tlist.append([])
            if re.search('\d*:\d*',self.Dim[i]):
                tlist[begin].append(rd.randint(\
                    eval(self.Dim[i].split(':')[0]),\
                    eval(self.Dim[i].split(':')[1])))
            elif self.Dim[i] == 'name':
                tlist[begin].append(randname())
            elif self.Dim[i] == 'Name':
                tlist[begin].append(randname(t=1))
            elif re.search('\w*,f\(x\)=.*',self.Dim[i]):
                tlist[begin].append(ctrfx(self.Dim[i]))
            else :
                tlist[begin].append(randre(self.Dim[i]))
        return self
    def addType(self,tpname,tprul):
        return self
    def delType(self,tpname,tprul):
        return self
    def addLen(self,num):
        return self
    def delLen(self,num):
        return self
    def delData(self,num='none',rul=1):
        if num == 'none':
            num=range(int(self.len/10))
        return self
    def __init__(self,file_da,str_header,data_ep,data_len,data_rule):
        self.adr=file_da
        j=0
        self.ruls={}
        for i in str_header.split():
            self.rusl[i]=data_ep.split()[j]
            j+=1
        self.len=[data_len,len(str_header.split())]
        self.List=[]
        rcallList(self)
        
    def __len__(self):
        return (self.type,self.len)
    def __add__ (self,other):
        if type(other) == fdata :
            return self
        else:
            return self
    #写入数据_new
    def wrt(self):
        return ''

#正相关离散规则
def ctrkx(x,y,k=1,r=80,d=0):
    for i in range(len(x)):
        y[i]=k*x[i]*rd.randint(r,100)/100+rd.randint(0,d)
    return y

#函数规则(当前支持:none)
def ctrfx(x,str,r=80,d=0):
    return y

#随机字母 -end
def randword(minlen=4,maxlen=6):
    word_len=rd.randint(minlen,maxlen)
    t=chr(rd.randint(97,122))
    for i in range(word_len):
        t=t+chr(rd.randint(97,122))
    return t

#随机姓名(数据更新|爬虫)
def randname(t=0):
    max_randname=7
    name_list=["ann",'smith','johnson','davis','wilson','taylor','thomas']
    rname=name_list[rd.randint(0,max_randname-1)]
    if t == 1:
        rname[0]=chr(ord(rname[0])-32)
    return rname

#正则表达随机数据 -end
def randre(strre,num=0):
    _x = xeger.Xeger()
    if num >0:
        tre=[]
    for i in range(num):
        if num > 0:
            tre[i]= _x.xeger(strre)
        else:
            tre = _x.xeger(strre)
    return tre

#写入数据_old -end
def wrt_old(file_da,str_header,data_ep,data_len):
    with open(file_da,mode='w') as f:
        f.write(str_hd+'\n')
        for i in range(data_len):
            for j in range(len(data_header)):
                if ',' in data_ep[j]:
                    k=data_ep[j].split(',')
                    data_rg=rd.randint(eval(k[0]),eval(k[1]))
                elif 'name' in data_ep[j]:
                    data_rg=randname()
                elif 'Name' in data_ep[j]:
                    data_rg=randname(1)
                else :
                    t=data_ep[j]
                    data_rg=randword(eval(t[1:]))
                if j == len(data_header)-1:
                    f.write("{}\n".format(data_rg))
                else :
                    f.write("{} ".format(data_rg))
    return ""

#读入数据
def red_data(file_da):
    return ""

#绘图规则
def drowFdata(fdata,rule=1):
    return 1

#交互窗口_old
try:
    file_da=input("请输入所创建文件名(or地址,带后缀,地址不存在时将创建文件):\n")
    str_hd=input("输入每类数据名称，以空格隔开:\n")
    data_header=str_hd.split()
    data_ep=[]
    for i in range(len(data_header)):
        data_ep[i]=input("输入第{}类数据范围:\
(例如0,10|字母输入a加字母数量，如a5|姓名输入name,首字母大写输入Name)\n".format(i+1))
    data_len=eval(input('输入数据条数:\n'))
    wrt_old(file_da,str_header,data_ep,data_len)
except:
    print("进程出错!请及时反馈!")









