
#coding=utf-8
import urllib2
import re
import os

#this function from internet @littlebai

#去掉特征字符串内的html操作符
def filter_tags(htmlstr):
   re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
   re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
   re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
   re_p=re.compile('<P\s*?/?>')#处理换行
   re_h=re.compile('</?\w+[^>]*>')#HTML标签
   re_comment=re.compile('<!--[^>]*-->')#HTML注释
   s=re_cdata.sub('',htmlstr)#去掉CDATA
   s=re_script.sub('',s) #去掉SCRIPT
   s=re_style.sub('',s)#去掉style
   s=re_p.sub('\r\n',s)#将<p>转换为换行
   s=re_h.sub('',s) #去掉HTML 标签
   s=re_comment.sub('',s)#去掉HTML注释  
   blank_line=re.compile('\n+')#去掉多余的空行
   s=blank_line.sub('\n',s)
   return s

#设置下载文件的保存位置
path = "E:\\news.qq.com\\a\\20120506\\"

#匹配url规则
rege = re.compile(r"/a/\d{8}/\d{6}.htm")

#从主页获得所有存在的url链接的后半部分并排序
urlcontent = urllib2.urlopen('http://news.qq.com/a/20120506/index.htm').read()
get_url = rege.findall(urlcontent)
get_url.sort()

#根据所获得的url数量建立循环遍历所有url链接
for i in xrange(0,len(get_url)):
   get_url[i] = "http://news.qq.com"+get_url[i]#完整链接
   
   #异常处理：部分url链接打开延时或者无法打开则跳过此次循环
   try:#异常跳出
      sub_web = urllib2.urlopen(get_url[i]).read()#打开完整url链接，获取内容
      
   except urllib2.URLError, e:
      print get_url[i][-10:-4]+' Failed'
      continue

   #下面开始内容操作
   re_keyt = "<h1>.+</h1>"#获取标题，此处的标题不含腾讯新闻的后缀比较方便
   title = re.findall(re_keyt,sub_web)#去掉标题左右的html标签
   re_keyc = re.compile("<div id=\"Cnt-Main-Article-QQ\".*</P></div>\n</div>",re.DOTALL)#匹配正文内容的正则（个别页面无法获得，见if块）
   content = re_keyc.findall(sub_web)#获得正文内容
   
   #个别页面由于有视频或其他的无法匹配正文内容的正则表达式，所以无法获得内容，应给与过滤
   if len(title)==0 or len(content)==0:
      continue
   
   re_content = filter_tags(title[0]+"\r\n"+content[0])#将标题和正文放到一起并去除html标签代码
   
   w=file(path+get_url[i][-10:-4]+'.txt','w')#根据页面的文件名建立txt文件，并打开为写入方式
   w.write(re_content)#写入获得的去除了html标签代码的标题和正文
   w.close()#关闭文件
   
   #命令行输出提示文件下载进度
   print 'Completed the'+str(i+1)+" -Total "+str(len(get_url))+" THE "+get_url[i][-10:]

#完成所有url链接的下载
print "Fuck The Stupied Guy!!!!"
#退出脚本
exit()