
#-*- encoding: utf-8 -*-

config = {'YES_I_WANNA_DO_IT':True,"NO_piceof_shit":False}

def setter(N):
    
    def print_iter(M = True):#开关 如果m!=0则打开闭合输入 直接进行迭代
        
        if type(N) is not list and M:
            return [N]
        else:
            return N[:]
        
    return print_iter
    
t = setter('123')

#迭代 ---www.iplaypy.com——--

for i in t():
    print i
    #output:
    #1
    #2
    #3
    
t = setter(['helloworld','其实不用修改魔术方法也可以做到 只是比较funcational',' closure(闭包) 是脚本语言的精粹 就像指针之于C'])
for j in t():
    print j
    #output:
    #123
    #helloworld
    #其实不用修改魔术方法也可以做到 funcational
    #closure(闭包) 是脚本语言的精粹 就像指针之于C
