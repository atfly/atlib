
import os 

#统计给定文件的行数
def countfile(test):
    f=open(test)
    num=0
    for x in f:num=num+1
    return num

#用来判断给定输入是目录还是文件，如果是文件，返回输入行数，如果是目录，迭代主程序
def count(test):
    if(os.path.isfile(test)):
        return countfile(test)  
    return total(test)

#主程序，接收输入，返回总共的行数
def total(test):
    l=os.listdir(test)
    num=0
    for x in l:num=num+count(test+'//'+x)
    return num   

print(total(r'a://1'))
#www.iplaypy.com