
#_*_coding:utf-8_*_

import os,sys
import re
from threading import Thread

#www.iplaypy.com
host=[]

if len(sys.argv) == 2:
	#配置文件配置信息检查有待改进 2011-05-12

	if os.path.isfile(sys.argv[1]):
		l_f=open(sys.argv[1],"r").readlines()

		for i in l_f:
			if re.search(r"^[1-9]",i):
				host.append(i.replace("\n","").replace("\r\n",""))
	else: 
		print("Usage: python ping_hosts.py host_config_filename")
		sys.exit(1)

elif len(sys.argv) == 1:
	if os.name == "nt":
		f=open("C:\\WINDOWS\\system32\\drivers\\etc\\hosts","r").readlines()

		for l_i in f:
			if re.search(r"^[1-9]",l_i):
				host.append(l_i.replace(" ","\t").split("\t")[0])   # 问题，需要解决 \t  空格问题

	elif os.name == "posix":  #linux系统  solairs x86
		f=open("/etc/hosts","r").readlines()

		for l_i in f:
			if re.search(r"^[1-9]",l_i):
				host.append(l_i.replace(" ","\t").split("\t")[0])

else:
	print("Usage: python ping_hosts.py")
	sys.exit(1)
	

class PING(Thread):
	def __init__(self,ip):
		Thread.__init__(self)
		self.ip=ip

	def run(self):
		if os.name== "nt":  #windows操作系统
			output=os.popen("ping -n 1 %s" % (self.ip)).read().split("\r\n")
			if "    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss)," in output:
				print("%s is OK" %(self.ip))
				#~ print output
			else:
				print("%s is ERROR" %(self.ip))
		elif os.name=="posix":
			if os.uname()[0] == "SunOS":   #x86 solaris 操作系统
				output=os.po
1a58
pen("ping %s 1" % (self.ip)).read()
				if re.search("alive",output):
					print("%s is OK" %(self.ip))
					#~ print output
				else:
					print("%s is ERROR" %(self.ip))
			elif os.uname()[0] == "FreeBSD":   # FreeBSD
				output=os.popen("ping -c 1 -W 2 %s" % (self.ip)).read().split("\n")
				if "1 packets transmitted, 1 packets received, 0.0% packet loss, 1 packets out of wait time" in output:
					print("%s is OK" %(self.ip))
				else:
					print("%s is ERROR" %(self.ip))
			elif os.uname()[0] == "AIX":           #通用linux操作系统
				output=os.popen("ping -c 1 -w 2 %s" % (self.ip)).read().split("\n")
				if "1 packets transmitted, 1 packets received, 0% packet loss" in output:
					print("%s is OK" %(self.ip))
					#~ print output
				else:
					print("%s is ERROR" %(self.ip))
			elif os.uname()[0] == "Linux":           #通用linux操作系统
				output=os.popen("ping -c 1 -W 2 %s" % (self.ip)).read().split("\n")
				if "1 packets transmitted, 1 received, 0% packet loss, time 0ms" in output:
					print("%s is OK" %(self.ip))
					#~ print output
				else:
					print("%s is ERROR" %(self.ip))

#~ host=["192.168.1.1","192.168.1.123","192.168.2.1","192.168.1.1","192.168.1.123"]

report_ok=[]
report_error=[]

#多线程同时执行
T_thread=[]


for i in host:
	t=PING(i)
	T_thread.append(t)
for i in range(len(T_thread)):
	T_thread[i].start()