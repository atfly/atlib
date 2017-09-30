
# -*- coding:utf-8 -*-
world='abcdefghijklmnopqrstuvwxyz'
serch={}
for x in range(0,26):
    serch[world[x]]=x+1
#print(serch)

def sumworld(wd):
    sum=0
    nums=[]
    wd=wd.lower()
    for x in wd:
        sum=sum+serch[x]
        m=str(serch[x])
        nums.append(m)
    s='+'.join(wd).upper()
    ss='+'.join(nums)   
    sss=wd.title()+':\n'+s+' = '+ss+' = '+str(sum)
    print (sss,end='\n')     
    #print(wd.title(),':\n',s,'=',ss,'=',sum,end='\n\n')

sumworld('hardwork')
sumworld('Knowledge')
sumworld('love')
sumworld('luck')
sumworld('money')
sumworld('Leadership')
sumworld('ATTITUDE')

#www.iplaypy.com
#循环试用单词求和功能
def xunhuan():
   inworld=input('请输入一个单词(输入exit退出)：')[:-1]
   print('\n')
   if inworld=='exit':
       exit()
   sumworld(inworld)
   input()
   xunhuan()
xunhuan()
