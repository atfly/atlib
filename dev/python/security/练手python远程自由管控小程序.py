
#!/etc/bin/env python
#-*-encoding=utf-8-*-

import poplib,email
from email.header import decode_header
import smtplib
import time
import os,sys
import random

def accp_mail():
        try:
                p=poplib.POP3('pop.qq.com')
                p.user('用户名')
                p.pass_('密码')
                ret = p.stat()
        except poplib.error_proto,e:
                return 1
                print "Login failed:",e
                sys.exit(1)
#       for i in range(1,ret[0]+1):
#               str=s.top(i,0)
#               strlist=[]
#               for x in str[1]:
#                       try:
#                               strlist.append(x.decode())
#                       except:
#                               try:
#                                       strlist.append(x.decode('gbk'))
#                               except:
#                                       strlist.app
2000
end(x.decode('big5'))
#                                       
#               mm = email.message_from_string('\n'.join(strlist))
#               sub=decode_header(mm['subject'])
#               if sub[0][1]:
#                       submsg = sub[0][0].decode(sub[0][1])
#               else:
#                       submsg = sub[0][0]
#
#               if submsg.strip()=='startpc':
#                       s.dele(i)
#                       return 0
#               
#       s.quit()
#       return 1
#
        for item in p.list()[1]:
                number,octets = item.split(' ')
#               print "Message %s: %sbytes"%(number,octets)
                lines = p.retr(number)[1]
                msg = email.message_from_string("\n".join(lines))
#       print msg.as_string()
                print msg.get_payload()
                if msg.get_payload()=="start\n\n":
                        return 0

def send_mail():
        try:
                handle = smtplib.SMTP('smtp.163.com', 25)
                handle.login('********@163.com','密码')
                msg = "To: ********@qq.com\r\nFrom: ********@163.com\r\nSubject: startpc \r\n\r\nstart\r\n"
                handle.sendmail('********@163.com','********@qq.com', msg)
                handle.close()
                return 1
        except:
                return 0


if __name__=='__main__':
        while send_mail()==0:
                time.sleep(2)

        while 1:
                time.sleep(5)
                if accp_mail()==0:
                        os.system('shutdown -f -s -t 10 -c closing...')
                        #print "哈哈哈哈哈哈哈，成功啦！！！！！！"
                        break
#www.iplaypy.com