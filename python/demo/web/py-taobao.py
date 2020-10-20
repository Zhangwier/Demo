import requests
import re
import bs4

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error1")
        return ""
    
def parsePage(ilt,html):
    try:
        plt=re.findall(r'\<strong\>\d+.\d+\</strong\>',html)
        tlt=re.findall(r'title=\".*?\"',html)
        for i in range(len(plt)):
            plt[i]=eval(plt[i][9:-9])
            tlt[i]=tlt[i][5:]
            ilt[i],append([plt[i],tlt[i]])
        return ilt
    except:
         print("error2")
         return []

def printGoodList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt :
        count = count+1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = input('输入搜索商品: ')
    depth = eval(input("输入统计页数: "))
    start_url = 'https://uland.taobao.com/sem/tbsearch?q='+ goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&page='+ str(i+1)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)

main()
    
    
    
	
