
# -*- coding: cp936 -*-

import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.126.com'
mail_user = 'xxx@126.com'
mail_pwd = 'hellopwd'
mail_to = 'xxao@gmail.com'
mail_cc = 'xx@xx.com'
mail_bcc = 'xx@qq.com'
content = 'this is a mail sent with python'

#表头信息www.iplaypy.com
msg = MIMEText(content)
msg['From'] = mail_user
msg['Subject'] = 'this is a python test mail'
msg['To'] = mail_to
msg['Cc'] = mail_cc
msg['Bcc'] = mail_bcc
try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    #login
    s.login(mail_user,mail_pwd)

    #send mail
    s.sendmail(mail_user,[mail_to,mail_cc,mail_bcc],msg.as_string())
    s.close()
    print 'success'

except Exception ,e:
    print e
