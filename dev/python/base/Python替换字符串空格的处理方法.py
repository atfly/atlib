
# -*- coding: utf-8 -*-

#替换字符串开头的空格
i=0
while s[i].isspace():
    i=i+1
else:
    ss=s[0:i].replace(' ','*')
    s=ss+s[i:]
    print s

#www.iplaypy.com

#替换字符串结尾的空格
i=-1
while  s[i].isspace():
    i=i-1
else:
    ss=s[i+1:].replace(' ','*')#list 用负数进行索引时，[a:-1]，-1仍然是取不到的
    s=s[:i+1]+ss
    print s