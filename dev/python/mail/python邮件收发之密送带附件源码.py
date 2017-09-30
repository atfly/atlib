
import os  
import smtplib  
import mimetypes  
import xlrd 
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEBase import MIMEBase  
from email.MIMEText import MIMEText  
from email.MIMEAudio import MIMEAudio  
from email.MIMEImage import MIMEImage  
from email import encoders
from email.utils import parseaddr, formataddr
from email.header import Header
from email.Encoders import encode_base64
from email.utils import COMMASPACE

subject = u'团队工作简报第144期' #邮件主题
content_file_path = u"E:\send_Dian.txt".encode("gb2312") #邮件正文内容，用utf-8无bom格式编码
path = u"E:\测试邮箱列表.xls".encode("gb2312") #发送邮件列表
file_path = u"E:\Newsletter_20150916_147.pdf".encode("gb2312") #附件
email_name = u'E-mail Address' #发送邮件列表中邮箱信息列头
content_file = open(content_file_path)
content = content_file.read()
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendMail(gmailUser, gmailPassword, subject, text, other, *attachmentFilePaths):   
    recipient = []  
    cmail = []
    
    msg = MIMEMultipart()  
    msg['From'] = _format_addr(u'Newsletter Dian <%s>' % gmailUser) 
    msg['To'] = COMMASPACE.join(recipient)
    msg['Cc'] = COMMASPACE.join(cmail)
    msg['Subject'] = Header(subject, 'utf-8').encode()  
    msg.attach(MIMEText(content, 'plain', 'utf-8'))  
  
    for attachmentFilePath in attachmentFilePaths:  
        msg.attach(getAttachment(attachmentFilePath))  
  
    mailServer = smtplib.SMTP('mail.hust.edu.cn', 25)  #QQ邮箱需要改为smtp.qq.com
    mailServer.ehlo()  
    mailServer.starttls()  
    mailServer.ehlo()  
    mailServer.login(gmailUser, gmailPassword)  
    mailServer.sendmail(gmailUser, recipient+cmail+other, msg.as_string())  
    mailServer.close()  
  
    print "Sent  email  to  ", other 
  
def getAttachment(attachmentFilePath):  
    contentType, encoding = mimetypes.guess_type(attachmentFilePath)  
  
    if contentType is None or encoding is not None:  
        contentType = 'application/octet-stream'  
  
    mainType, subType = contentType.split('/', 1)  
    file = open(attachmentFilePath, 'rb')  
  
    if mainType == 'text':  
        attachment = MIMEText(file.read())  
    elif mainType == 'message':  
        attachment = email.message_from_file(file)  
    elif mainType == 'image':  
        attachment = MIMEImage(file.read(),_subType=subType)  
    elif mainType == 'audio':  
        attachment = MIMEAudio(file.read(),_subType=subType)  
    else:  
        attachment = MIMEBase(mainType, subType)  
    attachment.set_payload(file.read())  
    encode_base64(attachment)    
  
    file.close()  
  
    attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(attachmentFilePath))  
    return attachment  

def OneUsrSendMail(gmailUser, gmailPassword, sheetNumFrom, sheetNumTo):
    other = []
    emailCnt = 0
    #other数组里面是当前密送邮件列表，emailCnt记录提取到该密送邮件中的第几个邮箱
    book = xlrd.open_workbook(path)
    for sheetmun in range(sheetNumFrom-1, sheetNumTo):      #假设一共有23张表格，则应该0=<range<24
      sh = book.sheet_by_index(sheetmun)
      nrows = sh.nrows
      clox = sh.row_values(0).index(email_name)             #根据每张表格第一行的数据取出E-mail Address所对应的列数
      for i in range(1, nrows):
        cell_value = sh.cell_value(i,clox)
        other.append(cell_value)                            #依次取出每一行的E-mail Address，压入密送邮箱地址数组other
        emailCnt = emailCnt+1
        if emailCnt == 40:                                  #
2000
QQ邮箱能否收到邮件，设定每40个邮箱地址发送一份密送邮件
            sendMail(gmailUser, gmailPassword, subject, content, other, file_path) #发送带附件的邮件并将计数清零，重新发送新的密送邮件
            emailCnt = 0
            other = []
    if emailCnt != 0:                                       #最后的一封有可能不是40个地址一起发送的，要补充上去
        sendMail(gmailUser, gmailPassword, subject, content, other, file_path)

OneUsrSendMail('xxxxx@hust.edu.cn', 'xxxxxxxx', 1, 3) #账号，密码，从第1张sheet发到第3张