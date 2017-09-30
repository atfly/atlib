
#! /usr/bin/env python
#coding=utf-8

import random
#密码字符串池
pwdStrPool = '23456789'\
    'abcdefghijkmnpqrstuvwxyz'\
    '~@#$%^&*()_+'\
    'ABCDEFGHIJKMNPQRSTUVWXYZ'\

#密码字符串池长度
pwdStrPoolSize = len(pwdStrPool)
#定义所要生成的密码长度
pwdLen = [16,16]

#获取一个随机数
def GetRandomNum(p):

    randomNum = random.randint(0,pwdStrPoolSize-1)
    return pwdStrPool[randomNum]

#www.iplaypy.com
#获取随机密码
def GetRandomPwd(pwdLen):

    RandomPwd = ''.join(map(GetRandomNum, xrange(pwdLen)))
    return RandomPwd
    
def tester():

    print GetRandomPwd(random.randint(pwdLen[0],pwdLen[1]))

if __name__ == '__main__':
    tester()
