
# -*— utf-8 -*-
'''
Created on 2011-12-27

'''
year=[]
month=[]
date=[]

for y in range(10000):
    x= '%04i'%y
    #不够四位的用0填充
    year.append(x)
    #加入到列表中

for m in range(1,13):
    x='%02i'%m
    #月份不够两位的用0填充
    month.append(x)
    #加入到列表中

YearAndMonth=[a+b for a in year for b in month]
#加年和月组合成如201201这样的字符串并建立一个新的列表

for i in YearAndMonth:
    x=YearAndMonth.index(i)
    #在新的列表中，用i的位置与12取余，余数是0,2,4,6,7,9,11则是31天的

    if x%12 in [0,2,4,6,7,9,11]:

        for d in range(1,32):
            y='%02i'%d
            date.append(i+y)

    elif x%12==1:
        #如果是二月的情况

        if x%12%4==0 or x%12%400==0:
            #用i的位置与12取余之后，得到的是年份的顺序
            #再进行闰年判断

            for d in range(1,30):
                y='%02i'%d
                date.append(i+y)
        else:
            for d in range(1,29):
                y='%02i'%d
                date.append(i+y )

    else:
        #30天月份的情况
        for d in range(1,31):
            y = '%02i'%d
            date.append(i+y)

#www.iplaypy.com

for i in date:
    x=list(i)
    x.reverse()
    #将x换成列表，然后转置，再重新还原成字符串
    y="".join(x)

    if y==i:
        #如果反转之后还相等，那么就是回文
        print(i)
