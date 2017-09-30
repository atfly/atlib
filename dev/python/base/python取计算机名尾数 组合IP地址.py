
#python3 取计算机名末尾数字+10 拼接成IP地址
#python3 练手

import socket
import re
import winreg
import os
#取计算机名方法1
hostname=socket.gethostname()
print(hostname)

#从环境变量中读计算机名
COMPUTERNAME = os.environ.get('COMPUTERNAME')
print(COMPUTERNAME)

#取计算机名方法3 可以理解为取最新的计算名。改完计算机名，不用重启，从这里就能直接取到新改的值。并没什么卵用？
key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName")
cn=winreg.QueryValueEx(key,"ComputerName")[0]
print(cn)

test=re.findall(r"\d+$",cn) #正则取取末尾数字

n=int(test[0])
if n>0 and n<245: #转成整型比较下IP合不合法
    n=n+10
    ip="192.168.1."+str(n)
    print(ip)

else:
    print("感觉有点不劲~")


'''
output:
>>> 
Jumper200
JUMPER200
5345JUM43534PER200
192.168.1.210
'''
