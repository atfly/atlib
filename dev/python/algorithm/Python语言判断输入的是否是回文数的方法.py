
#! /usr/bin/env python

#coding=utf-8

a = input()
b = str(a)
flag = True

#www.iplaypy.com

for i in range(len(b)/2):
    if b[i]!=b[len(b)-i-1]:
        flag = False
        break

if flag:
    print "%d is huiwen number!" % a

else:
    print "%d is not huiwen number!" % a

