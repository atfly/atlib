
#python版一行内容分行输出
#依山居 18:14 2015/11/4

a="aA1一bB2二cC3三dD4四eE5五fF6六gG7七hH8八iI9九"
"""
分行输出为:
abcdefghi
ABCDEFGHI
123456789
一二三四五六七八九
"""

print("方法一:===============")
for r in range(0,4):
    t=''
    for s in range(0+r,len(a),4):
        t=t+a[s]
    print(t)

print("方法二:===============")

#=_=这个方法会不会看起来比较傻?
l=list(a)
ta=tb=tc=td=''
for r in range(0,9):
    for s in range(0,4):
        if s==0:
            ta=ta+l.pop(0)
        if s==1:
            tb=tb+l.pop(0)
        if s==2:
            tc=tc+l.pop(0)
        if s==3:
            td=td+l.pop(0)
print(ta)
print(tb)
print(tc)
print(td)
      
print("方法3:回字有N种写法===============")
import string
ta=tb=tc=td=''
la=string.ascii_lowercase
ua=string.ascii_uppercase
nb=string.digits
ub="一二三四五六七八九"
for s in a:
    if s in la:
        ta=ta+s
    if s in ua:
        tb=tb+s
    if s in nb:
        tc=tc+s
    if s in ub:
        td=td+s
print(ta)
print(tb)
print(tc)
print(td)

print("方法4:回字有一种叫做正则的写法===============")
import re
#这正则写法感觉不科学,暂时没有好的想法
reg=["[a-z]","[A-Z]","\d","[^\da-zA-Z]"]
for s in reg:    
    rega=re.compile(s)
    s=re.findall(rega,a)
    print("".join(s))

"""

输出:
方法一:===============
abcdefghi
ABCDEFGHI
123456789
一二三四五六七八九
方法二:===============

abcdefghi
ABCDEFGHI
123456789
一二三四五六七八九
方法3:回字有N种写法===============

abcdefghi
ABCDEFGHI
123456789
一二三四五六七八九
方法4:回字有一种叫做正则的写法===============

abcdefghi
ABCDEFGHI
123456789
一二三四五六七八九
"""