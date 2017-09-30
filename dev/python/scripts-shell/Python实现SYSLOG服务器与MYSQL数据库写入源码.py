
import os,socket,sys,time,string
import MySQLdb

bufsize=1500

port=514

syslog_serverty={ 0:"emergency",
                   1:"alert",
                   2:"critical",
                   3:"error",
                   4:"warning",
                   5:"notice",
                   6:"info",
                   7:"debug"
                 }
syslog_facility={ 0:"kernel",
                   1:"user",
                   2:"mail",
                   3:"daemaon",
                   4:"auth",
                   5:"syslog",
                   6:"lpr",
                   7:"news",
                   8:"uucp",
                   9:"cron",
                   10:"authpriv",
                   11:"ftp",
                   12:"ntp",
                   13:"security",
                   14:"console",
                   15:"cron",
                   16:"local 0",
                   17:"local 1",
                   18:"local 2",
                   19:"local 3",
                   20:"local 4",
                   21:"local 5",
                   22:"local 6",
                   23:"local 7"
                 }


try:
  sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  sock.bind(("0.0.0.0",port))
except:
  print("error bind")
  sys.exit(1)
sql_em="insert into emergency values(%s,%s,%s,%s,%s,%s)"
sql_al="insert into alert     values(%s,%s,%s,%s,%s,%s)"
sql_cr="insert into critical  values(%s,%s,%s,%s,%s,%s)"
sql_er="insert into error     values(%s,%s,%s,%s,%s,%s)"
sql_wa="insert into warning   values(%s,%s,%s,%s,%s,%s)"
conn=MySQLdb.connect(host="127.0.0.1",db="syslog",port=18888,user="root",passwd="cinda")
curs=conn.cursor()
#f=file("syslog.txt","w")
print ("----------------syslog is start----------------\n")
#www.iplaypy.com
try:
  while 1:
    try:
      data,addr=sock.recvfrom(bufsize)
      #print data,addr
      syslog=str(data)
      n=syslog.find('>')
      serverty=string.atoi(syslog[1:n])&0x0007
      facility=(string.atoi(syslog[1:n])&0x03f8)>>3
      syslog_msg=syslog[26:]
      dev_name=syslog_msg[:syslog_msg.find(' ')]
      dev_msg=syslog_msg[syslog_msg.find(' '):]
      param=(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),dev_name,addr[0],
             syslog_facility[facility],syslog_serverty[serverty],dev_msg)
   
      if serverty==0:
        curs.execute(sql_em,param)
        print syslog_msg
      elif serverty==1:
        curs.execute(sql_al,param)
        print syslog_msg
      elif serverty==2:
        curs.execute(sql_cr,param)
        print syslog_msg
      elif serverty==3:
        curs.execute(sql_er,param)
        print syslog_msg
      elif serverty==4:
        curs.execute(sql_wa,param)
        print syslog_msg
        
      conn.commit()
      
      #print dev_msg,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
      #print syslog_serverty[serverty],syslog_facility[facility],syslog[26:]
      #f.writelines(syslog_serverty[serverty]+" "+syslog_facility[facility]+" "+syslog[26:]+'\n')
    except socket.error:
      pass
except KeyboardInterrupt:
  curs.close()
  conn.close()
  print ("------------------syslogd stop-------------\n")
  print "good bye"
  sys.exit()
#f.close