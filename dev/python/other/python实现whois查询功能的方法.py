
# -*- coding:utf-8 -*-

import urllib.request

def str_cut(str,startsep,endsep):
    str1=str.split(startsep)[1]
    str2=str1.split(endsep)[0]
    return str2

def whois(host):
      url='http://whois.chinaz.com/'+host
      data=urllib.request.urlopen(url).read()
      data=data.decode()
      if data.find('<div id="whoisinfo" class="div_whois">')==-1:
          data="该域名未注册，目前可以注册"
      else:
          data=str_cut(data,'<div id="whoisinfo" class="div_whois">','</div>')
          data=data.replace('<br/>','\n')[:-1]
      return '查询域名:'+host+'\n'+'-'*60+'\n'+data

def query():
   host=input('请输入域名不含"http://www."(q/Q退出):')[:-1]
   #data=whois(host)
   #print(data)
   host=host.lower()
   if host == 'q':
       exit()
   else:
       data=whois(host)
       print(data)
       input('\n输入enter继续...\n')
   query()
query()
    