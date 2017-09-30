
import urllib.request
import http.cookiejar

import socket
import time
import re


timeout = 20
socket.setdefaulttimeout(timeout)


sleep_download_time = 10 
time.sleep(sleep_download_time)

def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def saveFile(save_path,txts):
    f_obj = open(save_path,'w+')
    for item in txts:
        f_obj.write(item+'\n')
    f_obj.close()

#get_code_list
code_list='http://www.kujiang.com/book/catalog/6557'

url_main='http://www.kujiang.com'
oper = makeMyOpener()
uop = oper.open(code_list,timeout=1000)
data = uop.read().decode('utf-8','ignore')

pattern = re.compile('li class="one small-tablet third.*?<a href="(.*?)".*?>(.*?)</a></li>',re.S)

items = re.findall(pattern,data)

print ('获取列表完成')
url_path='url_wmjlyw.txt'

url_r=open(url_path,'r')
url_arr=url_r.readlines(100000)
url_r.close()
print (len(url_arr))




url_file=open(url_path,'a')


print ('获取已下载网址')



i=2
for tmp in items:
    if i > len(items):
        print('game over')
        break
    save_path = tmp[1].replace(' ','')+'.txt'
    url = url_main+tmp[0]
    i=i+1
    if url+'\n' in url_arr:
        continue
    print('%d' %i+'写日志：'+url+'\n')
    url_file.write(url+'\n')
    opene = makeMyOpener()
    op1 = opene.open(url,timeout=1000)
    data = op1.read().decode('utf-8','ignore')
    opene.close()
    pattern = re.compile('<p>　　(.*?)</p>',re.S)
    txts = re.findall(pattern,data)
    saveFile(save_path,txts)
    

url_file.close()


