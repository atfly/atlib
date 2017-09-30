
#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# command line tool for reading *.strings file (the file for multi-language support
of ios, the same for android.), make it a excel file for the translator.
1. reading file: receive file name and target name
2. 
Created on Jul 18, 2011

'''

import codecs
import pyExcelerator

#采用此方式是为了解决编码问题
file = codecs.open("C:/Users/ernest/Desktop/Localizable.strings", 'r', 'utf-8')
string = file.read()
file.close()

#去除无用字段；
string = string.replace('/* No comment provided by engineer. */', '').replace('\n', '')

#拆分字段；
list = [x.split(' = ') for x in string.split(';')]

#excel操作；
workbook = pyExcelerator.Workbook()
ws = workbook.add_sheet('sheet1')
#www.iplaypy.com

for x in range(len(list)):
    for y in range(len(list[x])):
        if list[x][y]:
            ws.write(x,y,list[x][y])

workbook.save('C:/Users/ernest/Desktop/strings.xls')
