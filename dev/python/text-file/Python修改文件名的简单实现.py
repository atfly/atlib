
#!/usr/bin/env python
#coding=utf-8

import os,shutil,string

dir = '/home/tt-ava/test'
#这里如果是windows系统，请按windows的目录形式写，如c:\\text

for i in os.listdir(dir):
    newfile = i.replace('.','_')                                
    #用_替代.，规则可以自己写。

    oldname = dir +'/'+str(i)

    newname = dir +'/'+str(newfile)

    shutil.move(oldname,newname)                  
    #shutil的用法在上篇日志中有描述。

print 'Rename finished!'﻿

#www.iplaypy.com