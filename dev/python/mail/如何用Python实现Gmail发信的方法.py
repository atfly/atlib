
#coding:utf-8

from email.mime.text import MIMEText

import smtplib

class Gamil (object ):
    def __init__ (self ,account,password):
        self .account=" %s @gmail.com" %account
        self .password=password

#www.iplaypy.com

    def send (self ,to,title,content):
        server = smtplib.SMTP('smtp.gmail.com' )
        server.docmd("EHLO server" )
        server.starttls()
        server.login(self .account,self .password)

        msg = MIMEText(content)
        msg['Content-Type' ]='text/plain; charset="utf-8"'
        msg['Subject' ] = title
        msg['From' ] = self .account
        msg['To' ] = to
        server.sendmail(self .account, to ,msg.as_string())
        server.close()

if __name__=="__main__" :
    gmail=Gamil("你自己的邮箱帐号" ,"你的邮箱对应的密码" )
    gmail.send("xxxx@gmail.com,xxxx@gmail.com" ,"快来测试一下" ,"玩蛇网Gmail自动发邮件" )

