
#!/usr/bin/env python
#encoding=utf-8

from smtplib import SMTP
import subprocess
 
smtp = "smtp.qq.com"
user = '1234567'
password = 'xxxx'
 
run_comd = subprocess.Popen('w¦grep pts',shell=True,stdout=subprocess.PIPE)
data = run_comd.stdout.read()
mailb = ["服务器有新用户登录",data]
mailh = ["From: 1234567@qq.com", "To: xxxx@gmail.com", "Subject: 用户登录监控"]
mailmsg = "\r\n\r\n".join(["\r\n".join(mailh), "\r\n".join(mailb)])
 
#www.iplaypy.com
def send_mail():
    send = SMTP(smtp)
    send.login(user,password)
    result = send.sendmail("1234567@qq.com", ("xxxx@gmail.com",), mailmsg)
    send.quit()
if data == '':
    pass
else:
    send_mail()
