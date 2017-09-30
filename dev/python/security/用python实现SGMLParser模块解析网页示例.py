
#-*-coding:utf-8
#!/usr/bin/env python 2011-08-11 am

import urllib2
from sgmllib import SGMLParser

class parserXml(SGMLParser):

       def __init__(self):
            SGMLParser.__init__(self)
            self.hrefs = []
            self.srcs= []
            #保存视频数组
            self.hrefs2=[]
      #获取超链接href值
       def start_a(self, attrs):
            href = [v for k, v in attrs if k == "href"]
            self.hrefs.extend(href)
     #获取图片超链接href值
       def start_img(self, attrs):
            src = [v for k, v in attrs if k == "src"]
            self.srcs.extend(src)
     #获取视频超链接href值
       def start_embed(self,attrs):
           href2=[v for k, v in attrs if k=="href"]
           self.hrefs2.extend(href2)

#--------www.iplaypy.com---------

#写入到文件中
def write(parser):
    hrefs=open("e:/tmp/urls.txt","w")
    #分行显示,链接
    for href in parser.hrefs:
       hrefs.write("%s%s" % (href,"\n"))
    hrefs.close()
    #分行显示图片链接
    imgs=open("e:/tmp/imgs.txt","w")
    for src in parser.srcs:
       imgs.write("%s%s" % (src,"\n"))
    imgs.close()


    #分行显示视频链接
    shipin=open("e:/tmp/shipin.txt","w")
    for href2 in parser.hrefs2:
        shipin.write("%s%s" % (href2,"\n"))
    shipin.close()

def main():
    parser=parserXml()
    #防止抓取网站有设防（回避spider抓取），改为浏览器请求，（抓取网站网页所有内容）
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req=urllib2.Request("http://www.xunlei.com",headers=headers)
    page_hander=urllib2.urlopen(req)
    page=page_hander.read()
    print page
    f=open("save.txt","w")
    f.writelines(page)
    f.close()

    #解析
    parser.feed(page)
    write(parser)
    parser.close()

if __name__=='__main__':
    main()