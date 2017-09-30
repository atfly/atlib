
#!/usr/bin/python
#_*_coding:utf-8_*_


import pexpect
import datetime
from threading import Thread

host=["192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1"]

report_ok=[]
report_error=[]
class PING(Thread):
	def __init__(self,ip):
		Thread.__init__(self)
		self.ip=ip
	def run(self):
		Curtime = datetime.datetime.now()	
		#Scrtime = Curtime + datetime.timedelta(0,minute,0) 
		#print("[%s]主机[%s]" % (Curtime,self.ip))
		ping=pexpect.spawn("ping -c1 %s" % (self.ip))
		check=ping.expect([pexpect.TIMEOUT,"1 packets transmitted, 1 received, 0% packet loss"],2)
		if check == 0:
			print("[%s] 超时 %s" % (Curtime,self.ip))

		elif check == 1:
			print ("[%s] %s 可达" % (Curtime,self.ip))

		else:
			print("[%s] 主机%s 不可达" % (Curtime,self.ip))

#www.iplaypy.com
#多线程同时执行
T_thread=[]
for i in host:
	t=PING(i)
	T_thread.append(t)
for i in range(len(T_thread)):
	T_thread[i].start()
#
#print ("\n=========问题主机情况如下==========\n")
#output(report_error)
#print ("\n=========正常主机情况如下==========\n")
#output(report_ok)


执行结果：
administrator@nagios:/win/pexpect$ ./ping.py 
[2011-04-25 21:30:22.126981] 192.168.1.1 可达
[2011-04-25 21:30:22.148376] 192.168.1.1 可达
[2011-04-25 21:30:22.179846] 192.168.1.1 可达
[2011-04-25 21:30:22.203691] 192.168.1.1 可达
[2011-04-25 21:30:22.227696] 192.168.2.1 可达
[2011-04-25 21:30:22.134049] 超时 192.168.1.123
[2011-04-25 21:30:22.145610] 超时 192.168.2.1
[2011-04-25 21:30:22.157558] 超时 192.168.1.123
[2011-04-25 21:30:22.167898] 超时 192.168.2.1
[2011-04-25 21:30:22.197572] 超时 192.168.1.123
[2011-04-25 21:30:22.202430] 超时 192.168.2.1
[2011-04-25 21:30:22.215561] 超时 192.168.1.123
[2011-04-25 21:30:22.229952] 超时 192.168.1.1
