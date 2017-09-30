
#coding:utf-8
#!/usr/bin/python

import pexpect
import datetime
import time
def getToday():
	return datetime.date.today()
	
def telnet_hw3552(ip,login,passwd,su_passwd):
	try:
		foo = pexpect.spawn('/usr/bin/telnet %s' % (ip))
		index = foo.expect(['sername:', 'assword:'])	
		if index == 0:
			foo.sendline(login)
			foo.expect("assword:")
			foo.sendline(passwd)
			#print(foo.before,foo.after)
		elif index == 1:
			foo.sendline(passwd)
	
		foo.expect(">")
		foo.sendline("super")
		#print("suerp--->",foo.before,foo.after)
		foo.expect("assword:")
		foo.sendline(su_passwd)
		#print("super pwd ok")
		foo.expect(">")
		foo.sendline("tftp 10.241.11.115 put %s %s " % ("vrpcfg.cfg",ip+"_hw_"+str(getToday())+".cfg"))
		index=foo.expect(["successfully","Error"])
		if index == 1:
			foo.sendline(" ")
			foo.expect(">")
			foo.sendline("tftp 10.241.11.115 put %s %s " % ("vrpcfg.zip",ip+"_hw_"+str(getToday())+".zip"))
		foo.sendline("quit")
	except pexpect.EOF:
		foo.close()
	else:
		foo.close		

#ios系统交换机
def telnet_ciscoios(ip,login,passwd,su_passwd):
	try:
		foo = pexpect.spawn('/usr/bin/telnet %s' % (ip))
		index = foo.expect(['sername:', 'assword:'])	
		if index == 0:
			foo.sendline(login)
			foo.expect("assword:")
			foo.sendline(passwd)
		elif index == 1:
			foo.sendline(passwd)
		foo.expect(">")
		foo.sendline("en")
		foo.expect("assword:")
		foo.sendline(su_passwd)
		foo.expect("#")
		foo.sendline("copy running-config tftp")
		foo.expect(".*remote.*")
		foo.sendline("%s" % ("10.241.11.115"))
		foo.expect(".*filename.*")
		foo.sendline("%s" % (ip+"_ciscoIos_"+str(getToday())+"_runningconfig.cfg"))
		foo.expect("#")
		foo.sendline("exit")
	except pexpect.EOF:
		foo.close()
	else:
		foo.close
		
#h3c防火墙
def telnet_h3cfirewallf1000(ip,login,passwd,su_passwd):
	try:
		foo = pexpect.spawn('/usr/bin/telnet %s' % (ip))
		index = foo.expect(['sername:', 'assword:'])	
		if index == 0:
			foo.sendline(login)
			foo.expect("assword:")
			foo.sendline(passwd)
			
		elif index == 1:
			foo.sendline(passwd)
	
		foo.expect(">")
		foo.sendline("tftp 10.241.11.115 put %s %s " % ("startup.cfg",ip+"_h3cf1000_"+str(getToday())+"_startup.cfg"))
		foo.expect(">")
		foo.sendline("tftp 10.241.11.115 put %s %s " % ("system.xml",ip+"_h3cf1000_"+str(getToday())+"_system.xml"))
		foo.expect(">")
		foo.sendline("quit")
	except pexpect.EOF:
		foo.close()
	else:
		foo.close		
	
#netscreen firewall
def telnet_netscren(ip,login,passwd,su_passwd):
	try:
		foo = pexpect.spawn('/usr/bin/telnet %s' % (ip))
		index = foo.expect(['login:', 'assword:'])	
		if index == 0:
			foo.sendline(login)
			foo.expect("assword:")
			foo.sendline(passwd)
		elif index == 1:
			foo.sendline(passwd)
	
		foo.expect(">")
		foo.sendline(su_passwd)
		foo.expect(">")
		foo.sendline("save config to tftp 10.241.11.115 %s" % (ip+"_netscreen_"+str(getToday())+".cfg"))
		foo.expect("Succeeded")
		foo.expect(">")
		foo.sendline("exit")
		#foo.expect(" save\? [y]/n")
		foo.expect(".*save.*")
		foo.sendline("Y")		
	except pexpect.EOF:
		foo.close()
	else:
		foo.close		

		
'''函数使用'''

telnet_hw3552("10.241.11.27","admin","******","#######") #cfg
telnet_hw3552("10.241.11.28","admin","******","#######")
telnet_hw3552("10.23.98.100","admin","******","#######")  #zip
telnet_hw3552("10.23.98.101","admin","******","#######")
telnet_netscren("10.203.10.167","netscreenroot","#######","#######") #netscreen
telnet_netscren("10.203.10.168","netscreenroot","#######","#######")
telnet_h3cfirewallf1000("10.241.11.124","admin","#######","")   #h3c firewal f1000
telnet_h3cfirewallf1000("10.241.11.125","admin","#######","")
telnet_hw3552("10.221.103.16","admin","******","#######")  #hw 8505
telnet_ciscoios("10.223.10.23","admin","******","#######") #cisco switch ios
#www.iplaypy.com