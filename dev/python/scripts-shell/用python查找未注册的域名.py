
#-*- encoding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import urllib
import urllib2
import time, threading


l='abcdefghijklmnopqrstuvwxyz0123456789-'
fl=open('d:\\reg.txt','a')
#step是上次扫描到的位置
step='aao9'
t=False
for i in l:
	for j in l:
		for k in l:
			for m in l:
				if i=='-':
					continue
				if m=='-':
					continue
				s=i+j+k+m
				if s==step:
					t=True
				if t==True:
					url = 'http://vip.regsky.com/reg/domainquery.asp?domainname='+s+'%2Ecom'
					response = urllib2.urlopen(url)
					the_page = response.read()
					if the_page=='Y':
						print s+":Not reged!"
						f=open('c:\\reg.txt','a')
						f.write(s+" :Not reged!\r\n")
						f.close()
					else:
						print s +": Reged!"
						fl.write(s +": Reged!\r\n")
					#线程休息3秒钟，别被服务器屏蔽了
					time.sleep(3)

fl.close()