import urllib.request
url="http://127.0.0.1:5000"
p="广东"
c="福建"
p=urllib.request.quote(p)
c=urllib.request.quote(c)
data="provice"+p+"&city="+c
resp=urllib.request.urlopen(url+"?"+data)
data=resp.read()
html=data.decode()
print(html)