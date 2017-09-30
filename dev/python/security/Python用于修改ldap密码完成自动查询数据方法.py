
# coding=gbk

import datetime, time
import decimal
import cx_Oracle
from ftplib import FTP
import telnetlib
import sys, getpass, os.path

# 连接oracle数据库，查询用户名用户密码。并生成修改ldap密码文件 在E:/ldapmm路径中
ltime=time.localtime(time.time())
timeStr=time.strftime('%Y-%m-%d %H-%M-%S', ltime)
conn = cx_Oracle.connect('dcp', '123456', cx_Oracle.makedsn('192.168.100.34', 1521, 'test'))
cur = conn.cursor()
cur.execute('''select username, password from table''');
filename = 'e:/ldapmm/' + timeStr + '.txt';
fobj = open(filename, 'w')

for row in cur:
        fobj.write('dn:uid=%s,ou=people,dc=xx,dc=xx,dc=cn\nchangetype: modify\nreplace: userPassword\nuserPassword:%s\n\n' % (row[0], row[1]))
cur.close()
conn.close()
fobj.close()

# ftp上传相应文件到固定目录下
print 'ftp start....'
ftp=FTP('192.168.101.4')
ftp.login('root', '123456')
ftp.cwd('/apphome/testldap')
bufsize = 1024
fd = open(filename, 'rb')
ftp.storbinary('STOR %s'% os.path.basename(filename), fd, bufsize)
fd.close()
ftp.quit()
print 'ftp end!'

# telnet到服务器中并执行相关命令，修改ldap密码
#www.iplaypy.com
commands = ['cd /apphome/testldap',
            'nohup ldapmodify -c -h 192.168.101.4 -p 389 -D "cn=Directory Manager" -w 123456 -f "'+ timeStr + '.txt" &']
print 'telnet start....'
tn = telnetlib.Telnet('192.168.101.4')
tn.set_debuglevel(2)

tn.read_until('login: ')
tn.write('root\n')
tn.read_until('Password: ')
tn.write('123456\n')

for command in commands:
    tn.write(command + '\n')
tn.write('exit\n')

#print tn.read_all()
print 'telnet end!'

print 'Finish!'
