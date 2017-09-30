
import re

fp = open('c:/1.txt', 'r')

s = fp.readline()
print(s)
aList = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s) #使用正规表达式搜索字符串
print(aList)

#www.iplaypy.com

for ss in aList:
    print(ss[0]+ss[2])
    aNum = float((ss[0]+ss[2]))
    print(aNum)
fp.close()

文件内容：

 

12.540  56.00  1.2e2 -1.2E2 3.0e-2 4e+3

