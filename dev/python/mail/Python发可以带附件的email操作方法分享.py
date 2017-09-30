
#encoding=utf-8

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib

mail_host = 'smtp.126.com'
mail_user = 'xx@126.com'
mail_pwd = 'xx'
mail_to = 'xxzhao@gmail.com'


msg = MIMEMultipart()

att = MIMEText(open('d:\\a.txt','rb').read(),'base64','gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="hello.txt"'
msg.attach(att)

message = 'content part'
body = MIMEText(message)
msg.attach(body)
msg['To'] = mail_to
msg['from'] = mail_user
msg['subject'] = 'this is a python test mail'

try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user,mail_pwd)

    s.sendmail(mail_user,mail_to,msg.as_string())
    s.close()

    print 'success'
except Exception,e:
    print e
#www.iplaypy.com
    