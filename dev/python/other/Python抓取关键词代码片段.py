
#-*- coding: UTF-8 -*-  
#Python UTF-8
#key.txt是抓取文件配置

import cgi,urllib #URL读取
import re #正则匹配
import MySQLdb #MySQL
import datetime #时间
#import time,thread #多线程

"""
MySQL表结构
CREATE TABLE `baidu` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `url` varchar(200) NOT NULL,
  `title` varchar(600) NOT NULL,
  `keys` varchar(100) NOT NULL,
  `bdurl` varchar(200) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
"""
def Yang_Config ():
	fp = open('key.txt','r')
	for line in fp.read().split('@'):
		word = line.split(',') #word 是字典
		#for item in word :
			#print item.encode("UTF-8")
			#print '------'
		if len(word) > 1:
			yang_u = word[0]
			yang_k = word[1]
			Yang_Spider(yang_u,yang_k)


#抓取页面开始
def Yang_Spider(yang_u,yang_k):
	url = 'http://www.baidu.com/s?wd=%s+site:%s&&rn=100'% (yang_k,yang_u)
	print url
	fp = urllib.urlopen(url).read()
	#print fp re.search
	m = re.findall(r"<table cellpadding=\"0\" cellspacing=\"0\" class=\"result\" id=\"(\d+)\"\s*?><tr><td class=f><h3 class=\"t\">(<font.*?<\/font>)?<a.*?href=\"(.*?)\"\s*?target=\"_blank\">(.*?)<\/a>\s*?<\/h3><font size=\-1>.*?<span class=\"g\">.*? ((\d{4}\-\d{1,2}\-\d{1,2})|(\d+小时前)|(\d+分钟前)) .*?<\/span>.*?<br><\/font><\/td><\/tr><\/table>",fp)
	if m:  
		#print m #
		for s in m:#数组抓取过来是gbk 转码成utf8.encode("UTF-8") 是汉字decode('gbk') ASNII转UTF8 入数据库操作print str(s[3]) #
			print '~~~'.join(s) #切割数组
			Yang_MySQL (yang_k,yang_u,s)
			#入库
		#for i, s in enumerate(m.group(3)):
			#print i,s
	else:  
		print 'not search'

def Yang_MySQL (k,u,s):
	global cursor,d
	cursor.execute("set names utf8")
	key_unicode = s[3].decode('gb2312') #gb2312
	key_utf8 = key_unicode.encode('utf-8')
	SQL = " INSERT INTO `baidukey`.`baidu` (`url` ,`title` ,`keys` ,`bdurl` ,`date`) VALUES ('%s', '%s', '%s','%s','%s'); " % (s[2],key_utf8,k,u,d)
	insert = cursor.execute(SQL)
	#print SQL

#www.iplaypy.com	
#运行抓取函数
conn = MySQLdb.connect(host="localhost",user="phper",passwd="123456",db="baidukey")
cursor = conn.cursor()
t = datetime.datetime.now()
d = t.strftime('%Y-%m-%d')#%H:%M:%S
Del = " DELETE FROM `baidukey`.`baidu` WHERE date = '%s'" % (d)
cursor.execute(Del)
Yang_Config()