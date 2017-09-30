
#coding: utf-8
# www.iplaypy.com python
import sys
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
from time import sleep
while(True):
    try:
        res = urllib2.urlopen("http://www.baidu.com/")
        #baidu is encoded by gbk
        print res.read()
        sleep(3600) #per hour
    except(KeyboardInterrupt):
        print("\nbyebyebye.~")
        break
"""