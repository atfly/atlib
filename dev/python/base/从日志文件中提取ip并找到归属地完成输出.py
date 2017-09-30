
import os,re
from getIpFrom import Httpsocket
httpIP = Httpsocket()

LogFilePath = "./logs/logs/"
OutPutPath = "./outs/"
LogFileList = [
"site1-access_log",
"site1-error_log",
"site2-access_log",
"site2-error_log",
"site3-access_log",
"site3-error_log"]

def CheckLogFile():
    for f in LogFileList:
      if not os.path.isfile(LogFilePath+f):
         print "logfile is not existed  %s" %f
         raise SystemExit

def GetIpList(logfile):
    temp = []

    fd = open(LogFilePath+logfile,'rb')

    line = fd.readline()

    while(line):
        r = re.findall(r'(\d+\.\d+\.\d+\.\d+).*', line)
        if len(r) == 1:
           if r[0] not in temp:
              temp.append(r[0])
        else:
           print "GetIpList occuer error ip list r size:" + str(len(r))
           raise SystemExit
        line = fd.readline();
    fd.close()

    if not os.path.isdir(OutPutPath):
       os.mkdir(OutPutPath)

    op = open(OutPutPath+logfile+"_IP",'wb')
    ipstr='';

    for ip in temp:
        httpIP.setbody(ip)
        (code,ipaddress) = httpIP.getIP()
        if (code == 0):
            ipstr = ip+"\t"+ipaddress
        else:
            ipstr = ip+"\tÎÞ·¨È·¶¨"
        op.write(ipstr+os.linesep);
    op.close()

def process():
    CheckLogFile()

    for f in LogFileList:
      print "log file:"+f

      if not os.path.isfile(LogFilePath+f):
         print "logfile is not existed  %s" %f

      else:
         GetIpList(f)


if __name__ == '__main__':
   process()



import re,urllib,urllib2,cookielib

ipmat = re.compile('<li>本站主数据：.*</li>', re.M)

class Httpsocket:
    """ Build for Make a full HttpRequest via POST/GET """
    isok = 0  #default 0
    ip_url = 'http://www.ip138.com/ips.asp'
    ip_send = 'http://www.ip138.com/ips8.asp'
    ip_body = []

    def __init__(self):
        self.cookies = urllib2.HTTPCookieProcessor()
        self.opener  = urllib2.build_opener(self.cookies)
        urllib2.install_opener(self.opener)

    def connect(self,ip_url,param={},header={}):
        encodeparam = urllib.urlencode(param)
        urllib2.urlopen(urllib2.Request(ip_url,encodeparam,header) )

    def openurl(self,url,param={},header={}):
        encodeparam = urllib.urlencode(param)
        req = urllib2.Request(url,encodeparam,header)
        return urllib2.urlopen(req) 

    def setbody(self,ip):
        self.ip_body = [('ip',ip),('action','2'),]

    def getIP(self):
        r1 = (0,'')
        body = self.ip_body[:]
        try:
           self.connect(self.ip_url)
        except Exception,e:
           return (1,'')
        try:
           u = self.openurl(self.ip_url)
           data = u.read()
           if "您的IP地址是" in data:
               u2 = self.openurl(self.ip_send,param=body)
               data2 = u2.read()
               r1 = ipmat.findall(data2)
               if (len(r1)==1):
                  r1 = r1[0];
                  r1=r1.replace("</li><li>","\t2");
                  r1=r1.replace("<li>","1");
                  r1=r1.replace("</li>","1");
                  r1=(0,r1)
           else:
               return (1,'')
        except Exception,e:
           return (1,'')
        retu
2000
rn r1
