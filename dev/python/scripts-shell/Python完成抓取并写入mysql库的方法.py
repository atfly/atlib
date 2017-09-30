
#!/usr/bin/env python

#-*-coding:utf-8-*-
#encoding=utf-8


import sys;
import os;
import re;
import random;
import urllib2;
import time;
import datetime;
#import socket;
import MySQLdb as mysql;

reload(sys)

sys.setdefaultencoding('utf-8')

#--转到目录--
os.chdir('img')

#urllib2.socket.setdefaulttimeout(15)

User = 'username'
Passwd = 'password'
Host = 'localhost'
Db = 'dbname'

#目标网站需替换
home = "目标网站"

#--链接数据库--
contents = mysql.connect(user=User,passwd=Passwd,host=Host,db=Db,charset='utf8').cursor()

lsid = []

pnext = []

for sid in xrange(1,100,10):
    lsid.append(str(sid))

print "进行列表分段",lsid,"完成."
for tid in reversed(xrange(2,len(lsid)+1)):
    for i in reversed(xrange(int(lsid[(int(tid)-2):(int(tid)-1)][0]),int(lsid[(int(tid)-1):int(tid)][0]))):
        #print i
        #==进行列表获取==#
        request = urllib2.Request("http://www.8264.com/portal-list-catid-251-page-"+str(i)+".html")
        request.add_header('User-Agent','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
        for u in reversed(re.findall('<h2><a href=\"(.*?)\" title=\'',re.findall('<div class=\"title_8264\">(.*?)<div class=\"pg\">',urllib2.urlopen(request).read(),re.DOTALL)[0],re.DOTALL)):
            #print u

            #--获取内容页面--
            newsurl = urllib2.Request(u)
            newsurl.add_header('User-Agent','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
            news = urllib2.urlopen(newsurl).read()
            time.sleep(int(random.uniform(1,5)))

            #--获取标题--
            title = re.findall('<div class=\"newstitle\">(.*?)<\/div>',news,re.DOTALL)

            #--获取时间--
            dates = list(eval(re.sub('\,0',',',re.sub(':| |-',',',re.findall('<td align=\"center\" valign=\"middle\">.*?<div style=\"line-height:1.8; text-align:center;\">\xcc\xed\xbc\xd3\xca\xb1\xbc\xe4\xa3\xba(.*?)&nbsp;',news,re.DOTALL)[0]))))

            #--进行时间格式化--
            #--2011-05-10 08:19 to 1305010787.029--
            ttime = datetime.datetime(dates[0],dates[1],dates[2],dates[3],dates[4])
            ptime = time.mktime(ttime.timetuple())

            #--获取作者--
            athour = re.sub('<.*?>','',re.findall('&nbsp;\xd7\xf7\xd5\xdf\xa3\xba(.*?)<br \/><a',news,re.DOTALL)[0])

            #--获取分页链接--
            page = re.findall('<div class=\"pg\">(.*?)<\/div>',news,re.DOTALL)
            if page != []:
                pnext = re.findall('<a href=\"(.*?)\">[0-9]*<\/a>',page[0],re.DOTALL)
                one_img = []
                one_txt = re.sub('<[a|A].*?>|<\/[a|A]>','',re.findall('<div class=\"newstext\">(.*?)<\/div>',news,re.DOTALL)[0])
                newstxt = re.sub('[http:\/\/image.8264.com\/portal\/[0-9]*\/[0-9]*\/|http:\/\/image.8264.com\/portal\/photo\/[0-9]*\/[0-9]*\/]','',one_txt)
                one_img.extend(re.findall('<IMG src=\"(.*?)\">',one_txt,re.DOTALL))
                for one_dimg in one_img:

                    #--下载文章内图片--
                    one_yscurl = 'wget -q '+one_dimg
                    os.system(one_yscurl)
                for p in pnext:
                    #print p,"\n"
                    more_img = []
                    morepage = urllib2.Request(p)
                    morepage.add_header('User-Agent','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
                    pnewtxt = urllib2.urlopen(morepage).read()
                    txt = re.sub('<[a|A].*?>|<\/[a|A]>','',re.findall('<div class=\"newstext\">(.*?)<\/div>',pnewtxt,re.DOTALL)[0])

                    #--得到入库的内容--
                    ntxt = re.sub('[http:\/\/image.8264.com\/portal\/[0-9]*\/[0-9]*\/
2000
|http:\/\/image.8264.com\/portal\/photo\/[0-9]*\/[0-9]*\/]','',txt)

                    #--处理内容中的图片--
                    more_img.extend(re.findall('<IMG src=\"(.*?)\">',txt,re.DOTALL))
                    for more_dimg in more_img:
                        more_syscurl = 'wget -q '+more_dimg
                        os.system(more_syscurl)

                    newstxt += ntxt
                texts = title[0].decode('gbk','ignore').encode('utf-8'),newstxt.decode('gbk','ignore').encode('utf-8'),athour.decode('gbk','ignore').encode('utf-8'),ptime

                #--进行数据插入--
                contents.execute("INSERT INTO `dbname`.`table_name` (`aid`, `class_id`, `title`, `content`, `author`, `order`, `state_radio`, `time`, `view_num`, `img`, `CityID`) VALUES (NULL, '2', %s, %s, %s, '0', '2', %s, '0', '', '53');",texts);
                print athour.decode('gbk','ignore').encode('utf-8'),"在",tuple(dates),"发表的",title[0].decode('gbk','ignore').encode('utf-8'),"发布成功!"
                time.sleep(int(random.uniform(30,90)))

#www.iplaypy.com

            else:
                #pass
                only_img = []
                only_txt = re.sub('<[a|A].*?>|<\/[a|A]>','',re.findall('<div class=\"newstext\">(.*?)<\/div>',news,re.DOTALL)[0])
                newstxt = re.sub('[http:\/\/image.8264.com\/portal\/[0-9]*\/[0-9]*\/|http:\/\/image.8264.com\/portal\/photo\/[0-9]*\/[0-9]*\/]','',only_txt)
                only_img.extend(re.findall('<IMG src=\"(.*?)\">',only_txt,re.DOTALL))
                for only_img in only_img:
                        only_syscurl = 'wget -q '+only_img
                        os.system(only_syscurl)
                texts = title[0].decode('gbk','ignore').encode('utf-8'),newstxt.decode('gbk','ignore').encode('utf-8'),athour.decode('gbk','ignore').encode('utf-8'),ptime
                contents.execute("INSERT INTO `dbname`.`table_name` (`aid`, `class_id`, `title`, `content`, `author`, `order`, `state_radio`, `time`, `view_num`, `img`, `CityID`) VALUES (NULL, '2', %s, %s, %s, '0', '2', %s, '0', '', '53');",texts);
                print athour.decode('gbk','ignore').encode('utf-8'),"在",tuple(dates),"发表的",title[0].decode('gbk','ignore').encode('utf-8'),"发布成功!"
                time.sleep(int(random.uniform(30,90)))

        print "第",i,"页采集完成.休息一下,进入下一页采集."

        #--停顿一会--
        time.sleep(int(random.uniform(1200,3200)))
#--关闭数据库连接--
contents.close();