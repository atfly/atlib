
#-*- coding:cp936 -*-
import random,time,sys,os,re

m="s"

def r(a,b):
    return random.randint(a,b)

def ag(g):
    i="a"
    g=int(g)

    while i.isdigit()==False:#判断i是否为字符
        i=input("\n*************************\n设定A的GDP增长指标:")
    ag=int(i)

    if(ag<=g):
        return ag

    if(ag>g):
        return r(-10,0)      

def start():
    a=20
    b=20
    c=0
    k=20
    while c==0:
        
        #time.sleep(1)
        k=k+int(r(-5,5))
        g=int(a/10)+10
        g=int(r(1,g))#最高增长
        agint=int(ag(g))
        i=os.system('cls')#清屏
        a=a+agint
        bring=int(b/10)+10
        bring=int(r(1,bring))
        if(bring>g):
            bring=int(r(-10,0))
        b=b+bring
        aa=""
        bb=""
        #a=10 #测试数据
        #b=10
        #k=8

        if(a>b):
            aa="(领先:"+str(a-b)+")"

        if(b>a):
            bb="(领先:"+str(b-a)+")"

        kk="(全球贸易容忍度:"+str(k*2)+")"
        
        print ("---\n人民能承受的GDP最高限额是(g):"+str(g))

        #time.sleep(1)

        print ("---\nA的GDP变化:"+str(agint)+"  B的GDP变化:"+str(bring))

        print ("***\nA的GDP:"+str(a)+aa+"\nB的GDP:"+str(b)+bb)

        print ("---\n外交关系变为:"+str(k*2-a-b)+kk)

        if(a>b and a+b>k*2):
            ab=a-b
            ab=int(r(1,ab))
            a=a+ab
            b=b-ab
            k=(a+b)/2
            print ("外交关系恶劣，贸易大战，胜利者是A,B的GDP减少"+str(ab)+"，A的GDP增加"+str(ab)+"\n战后,外交关系变为:"+str(int(2*k-a-b)))
            print ("A的GDP:"+str(a)+" B的GDP:"+str(b))
        if(b>a and a+b>k*2):
            ab=b-a
            ab=int(r(1,ab))
            a=a-ab
            b=b+ab
            k=(a+b)/2
            print ("外交关系恶劣，贸易大战，胜利者是B,A的GDP减少"+str(ab)+" B的GDP增加"+str(ab)+"\n战后,外交关系变为:"+str(int(2*k-a-b)))
            print ("A的GDP:"+str(a)+" B的GDP:"+str(b))
        if(a==b and a+b>=(k*2)):
            abk=a+b-k*2
            ab=int(r(-abk,abk))
            a=a+ab
            b=b-ab
            print ("外交关系紧张，两国贸易停止,A的GDP变化"+str(ab)+" B的GDP变化"+str(ab)+"\n外交关系变为:"+str(int(2*k-a-b)))
            print ("A的GDP:"+str(a)+" B的GDP:"+str(b))
        if(a<=0 and b>0):
            print("\n##################胜利者是B##################")
            c=1
        if(b<=0 and a>0):
            print("\n##################胜利者是A##################")
            c=1
        if(a<=0 and b<=0):
            print("\n##################全部失败！！！##################")
            c=1
        if(a-b>=k or b-a>=k):
            print("\n##################www.iplaypy.com##################")
            c=1

while m=="s":
    m=""
    while m!="s" and m!="e":
        m=input("\n====\nA的GDP:20 B的GDP:20 外交关系:20\n输入\"s\"继续 输入\"e\"退出：")
        i=os.system('cls')
    if(m=="s"):        
        start()

