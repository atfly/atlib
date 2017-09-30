
import urllib
import re

url="http://feelssh.com/"
#url中的网址有时会遇到打不开的情况哦！

html=urllib.urlopen(url)

result=html.read().decode('utf-8')

#f=file('ssh.txt','w')
#f.write(result.encode('utf-8'))
#f.close()

#www.iplaypy.com
pattern='([^\x00-\xff]{6}\d+.\d+.\d+.\d+)<'
server=re.findall(pattern,result)
pattern='(SSH[^\x00-\xff]{3}\d{2})<'
port=re.findall(pattern,result)
pattern='(SSH[^\x00-\xff]{3}[A-Za-z]+)<'
account=re.findall(pattern,result)
pattern='>\n\n\s(\S{9})\n<'
psw=re.findall(pattern,result)

for i in range(len(server)):
        print '\t%s'%server[i],'\n\t%s'%port[i],'\n\t%s'%account[i],'\n\t%s'%'密码：'+str(psw[i]),'\n\n'
