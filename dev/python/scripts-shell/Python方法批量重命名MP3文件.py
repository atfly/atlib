
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys

nowpath=os.getcwd()
files=os.listdir(nowpath)

def rename(old,new):
    print 'begin to rename',old,new

    new2=''

    for i in range(0,len(new)):
        a=new[i]

        if a!=u'\x00':
            new2+=a

    if new2!=old and new2:

        os.rename(old,new2)

        print 'rename',old,'to',new2


for name in files:
    if os.path.isfile(name) and len(name)>20:
        '''
        www.iplaypy.com
        len(name)限定仅限于文件名长度超过20的，如果想要用此方法重命名原有的mp3文件，那么
        可将此限定去掉，不过最好保证要改名的文件有规范的mp3id
        
        '''
        print name       

        f=open(name,'r')
        f.seek(-128,2)

        if f.read(3)=='TAG':
            temp=f.read(21)
            temp=unicode(temp,'gbk','ignore')

            f.close()

            temp= temp+'.mp3'

            rename(name,temp)

