
import poplib

emailServer = poplib.POP3('your pop3 server name')  
emailServer.user('your mail account')  
emailServer.pass_('your mail password')  

# 设置为1，可查看向pop3服务器提交了什么命令  
emailServer.set_debuglevel(1)  
      
# 获取欢迎消息  
serverWelcome = emailServer.getwelcome()  

print serverWelcome  
      
# 获取一些统计信息  
emailMsgNum, emailSize = emailServer.stat()  

print 'email number is %d and size is %d'%(emailMsgNum, emailSize)  
      
# 遍历邮件，并打印出每封邮件的标题  
for i in range(emailMsgNum):  
    for piece in emailServer.retr(i+1)[1]:  
        if piece.startswith('Subject'):  
            print '\t' + piece  
            break  
              
emailServer.quit()  
