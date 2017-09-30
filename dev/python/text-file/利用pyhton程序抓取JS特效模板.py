
#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib,os,sys
import gevent,re
from gevent import monkey
from bs4 import BeautifulSoup
gevent.monkey.patch_socket()

'''
Description：Python 爬虫抓取懒人图库的JS脚本模板
Author：admin
Create-Date：2015-05-25
Version：1.0
'''

HTTP_URL = 'http://www.lanrentuku.com%s'
DOWNLOAD_URL = HTTP_URL[:-2] + '/js/d%szip'
reg=r'\d{1,}\.+'

def encode(text):
    return text.encode("utf8")

def createDirectory(curPath):
    myPath = os.path.join(getSubDirectory(), u'JS代码模板')
    if not os.path.exists(myPath):
        os.mkdir(myPath)
    return os.path.join(myPath, curPath)

def getSubDirectory():
    return os.getcwd()

def schedule(a, b, c): 
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    sys.stdout.write('%.1f%%\r' % per)
    sys.stdout.flush()

def geturllist(url):
    url_list = {}
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    # 用BeautifulSoup解析
    decodeHtml = BeautifulSoup(content)
    try:
        aTags = decodeHtml.find_all('div', {'class':'list-pngjs'})[0].find_all('a')
    except IndexError, e:
        print e
        aTags = None
    # 获取链接地址和标题
    if aTags is not None:
        for a_tag in aTags:
            url_list[HTTP_URL % a_tag.get('href')] = a_tag.get_text()
    return url_list
   
def download(down_url):
    try:
        m=re.search(reg,down_url[0])
        name = DOWNLOAD_URL % m.group(0)
        urllib.urlretrieve(name,createDirectory(down_url[1] + name[-4:]),schedule)
    except Exception, e:
        print e.message
   
def getpageurl(xUrl):
    # 进行列表页循环
    return [xUrl % page for page in xrange(1,49)]

if __name__ == '__main__':
    jobs = []
    pageurl = getpageurl('http://www.lanrentuku.com/js/p%s.html')
    # 爬取所有链接
    for i in pageurl:
        for k in geturllist(i).items():
            jobs.append(gevent.spawn(download, k))
    gevent.joinall(jobs)
