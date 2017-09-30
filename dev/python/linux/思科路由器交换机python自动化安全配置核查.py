
#coding: utf-8
#!/usr/bin/python
'''
1，用于Cisco设备的配置核查，原理上是在show running-config结果中对关键配置命令进行搜索，H3C设备后续再做吧。
2，将本脚本（pz.py）和收集到的配置文件放在同一个目录下。
3，配置文件的格式需要保证，文件名以设备IP开头，内容第一行为设备IP地址（用于辨识设备），第二行以下为show running-config结果。
4，pz.py执行前请保证当前目录下仅有配置文件和本核查脚本，否则会影响脚本中循环（i-1）的执行。
5，脚本执行完成之后生成2个文本：
    Cisco.txt为所有思科设备以IP列项的核查结果。
    Ciscozong.txt为所有思科设备以核查项列项的核查结果。
6，检查项的分类原则大致为，帐号与登录，认证授权，日志审计，协议安全，服务安全5部分，具体检查项分类见最后部分的注释。
7，脚本中保存了大量注释，便于理解和改进。
8，检查项包括路由器和交换机的所有安全项目，单一检查项有路由器or交换机的控制开关保证能够分别开路由器和交换机的不同检查项。
9，本脚本依照最全的配置核查规定，实际在写报告中也截取必要结果即可。
10，当结果出现“锘?”乱码，需要将配置文件用notepad++打开，并保存为“以UTF-8无BOM格式保存”
'''
import os
import sys
import re
info = os.getcwd()#获取脚本所在的路径
list = os.listdir(info)#返回指定目录下的所有文件和目录名
print list
for i in range(0,len(list) - 1):
	openfile = open(list[i],'r')
	f = openfile.read()  
	s = f.split('!')
	t = f.split('\n')
	r = f.split('#')
	m = i + 1
	lastfile = open('Cisco.txt','a')#每次读取一个配置文档，变量lastfile都会重新指向CiscoSwitch.txt或CiscoRouter.txt
	#每次读取一个配置文档，以下参数都会归零
	aa1 = aa2 = bb1 = bb2 = cc1 = dd1 = ee1 = ff1 = ff2 = ff3 = ff4 = gg1 = hh1 = hh2 = ii1 = ii2 = 0
	jj1 = jj2 = kk1 = kk2= 0
	ll1 = ll2 = ll3 = ll4 = ll5 = ll6 = ll7 = ll8 = ll9 = ll10 = ll11 = ll12 = ll13 = ll14 = 0
	mm1 = mm2 = mm3 = nn1 = nn2 = oo1 =oo2 = pp1 = pp2 = pp3 = pp4 = pp5 = pp6 = pp7 = pp8 = pp9 = qq1 = 0
	rors = 0
	lastfile.write("+----------------------------+\n" + "[NO." + str(m) +"]: " + t[0] + ":\r\n")
	#lastfile.write("+----------------------------+\n + '*'") #每次读取一个配置文档，都写一个抬头标志和IP地址
	#lastfile.write(str(i))
	#lastfile.write("',' + t[0] + '*'+'\r\n'")
	for j in range(0,len(s)):
		#1，检查口令加密存放-enable密码
		if re.findall('enable secret',s[j]):
			aa1 = 1 
		else:
			pass
		#2，检查口令加密存放-用户密码
		if re.findall(r'username(.|\n)*secret',s[j]):
			aa2 = 1
		else:
			pass
		#3，检查是否已配置console接口密码
		if re.findall('line con 0(.|\n|\r)*password',s[j]):
			bb1 = 1                          
		else:
			pass
		if re.findall('line con 0(.|\n)*login authentication',s[j]):
			bb2 = 1                          
		else:
			pass		
		#4，检查是否使用加密协议进行远程管理	注意telnet和ssh同时允许的情况，此逻辑还是正确的
		if re.findall(r'line vty(.|\n)*transport input ssh',s[j]):
			cc1 = 1                          
		else:
			pass	
		#5，检查是否限制可远程登录管理的IP地址
		if re.findall(r'line vty 0 4(.|\n)*access-class(.|\n)*line vty 5 15(.|\n)*access-class',s[j]):
			dd1 = 1                          
		else:
			pass	
		#6，检查是否配置vty登录认证
		if re.findall(r'line vty(.|\n)*login local',s[j]):
			ee1 = 1
		else:
			pass
		#7，检查是否已配置超时登出时间-ssh
		if re.findall('ip ssh time-out',s[j]):
			ff1 = 1                          
		else:
			pass	
		#8，检查是否已配置超时登出时间-vty
		if re.findall(r'line vty(.|\n)*exec-timeout',s[j]):
			ff2 = 1                          
		else:
			pass	
		#9，检查是否已配置超时登出时间-con
		if re.findall(r'line con(.|\n)*exec-timeout',s[j]):
			ff3 = 1                          
		else:
			pass	
		#10，检查是否已配置超时登出时间-aux
		if re.findall(r'line aux(.|\n)*exec-timeout',s[j]):
			ff4 = 1                          
		else:
			pass	
		#11，检查是否配置远程认证服务器审计功能
		if re.findall('aaa accounting',s[j]):
			gg1 = 1                          
		else:
			pass
		#12，检查是否启用AAA认证服务器
		if re.findall(r'aaa new-model',s[j]):
			hh1 = 1
		else:
			pass
		#13，检查是否配置radius认证服务器
		if re.findall(r'radius-server',s[j]):
			ii1 = 1                          
		else:
			pass						
		#14，检查是否开启tacacs认证服务器
		if re.findall(r'tacacs-server',s[j]):
			ii2 = 1                          
		else:
			pass					
		#15，检查是否启用SNMPv3
		if re.findall(r'snmp-server host(.|\n)*version 3 auth',s[j]):
			jj1 = 1                          
		else:
			pass
		#16，检查是否SNMP community 权限是否仅为RO		
		if re.findall('RO',s[j]):
			jj2 = 1                          
		else:
			pass		
		#17，检查是否配置统一设备的系统日志源地址		
		if re.findall('logging source-interface',s[j]):
			kk1 = 1                          
		else:
			pass
		#18，检查是否已开启远程日志功能		
		if re.findall(r'logging (\d)*',s[j]):
			kk2 = 1                          
		else:
			pass	
		#19，检查路由协议是否启用协议加密功能-vrrp
		if re.findall(r'vrrp',s[j]):
			ll1 = 1                          
		else:
			pass
		if re.findall(r'vrrp(.|\n)*authentication md5',s[j]):
			ll2 = 1                          
		else:
			pass		
		#20，检查路由协议是否启用协议加密功能-hsrp
		if re.findall(r'standy',s[j]):
			ll3 = 1                          
		else:
			pass
		if re.findall(r'standby(.|\n)*authentication md5',s[j]):
			ll4 = 1                          
		else:
			pass	
		#21，检查路由协议是否启用协议加密功能-isis
		if re.findall(r'router isis',s[j]):
			ll5 = 1                          
		else:
			pass
		if re.findall(r'authentication mod md5',s[j]):
			ll6 = 1                          
		else:
			pass
		#22，检查路由协议是否启用协议加密功能-eigrp
		if re.findall(r'router eigrp',s[j]):
			ll7 = 1                          
		else:
			pass
		if re.findall(r'ip authentication mode',s[j]):
			ll8 = 1                          
		else:
			pass				
		#23，检查路由协议是否启用协议加密功能-ospf
		if re.findall(r'router ospf',s[j]):
			ll9 = 1                          
		else:
			pass
		if re.findall(r'ip ospf message-digest-key',s[j]):
			ll10 = 1                          
		else:
			pass					
		#24，检查路由协议是否启用协议加密功能-rip
		if re.findall(r'router rip',s[j]):
			ll11 = 1                          
		else:
			pass
		if re.findall(r'ip rip authentication mod',s[j]):
			ll12 = 1                          
		else:
			pass								
		#25，检查路由协议是否启用协议加密功能-bgp
		if re.findall(r'router bgp',s[j]):
			ll13 = 1                          
		else:
			pass
		if re.findall(r'router bgp(.|\n)*neighbor(.|\n)*password',s[j]):
			ll14 = 1                          
		else:
			pass		
		#26，检查是否启用BGP防广播风暴功能
		if re.findall(r'router bgp',s[j]):
			mm1 = 1                          
		else:
			pass
		if re.findall(r'bgp dampening',s[j]):
			mm2 = 1                          
		else:
			pass
		#27，过滤路由更新
		if re.findall(r'neighbor(.|\n)*prefix-list(.|\n)*out',s[j]):
			mm3 = 1                          
		else:
			pass	
		#28，是否配置启用NTP
		if re.findall('ntp server',s[j]):
			nn1 = 1                          
		else:
			pass				
		#29，检查NTP协议是否启用协议加密功能
		if re.findall(r'ntp authenticate',s[j]):
			nn2 = 1                          
		else:
			pass
		#30，检查是否开启连接保持
		if re.findall(r'tcp-keepalives-out',s[j]):
			oo1 = 1                          
		else:
			pass					
		if re.findall(r'tcp-keepalives-in',s[j]):
			oo2 = 1                          
		else:
			pass
		#31，是否关闭不必要的协议-cdp
		if re.findall('no cdp enable',s[j]) or re.findall('no cdp run',s[j]):
			pp1 = 1                          
		else:
			pass
		#32，是否关闭不必要的协议-pad
		if re.findall('no service pad',s[j]):
			pp2 = 1                          
		else:
			pass
		#33，是否关闭不必要的协议-bootp
		if re.findall('no ip bootp server',s[j]):
			pp3 = 1                          
		else:
			pass
		#34，是否关闭不必要的协议-source-route
		if re.findall('no ip source-route',s[j]):
			pp4 = 1                          
		else:
			pass
		#35，是否关闭不必要的协议-http
		if re.findall('no ip http server',s[j]):
			pp5 = 1                          
		else:
			pass			
		#36，是否关闭不必要的协议-small
		if re.findall('no service.*small-servers',s[j]):
			pp6 = 1  			
		else:
			pass	
		#37，是否关闭不必要的协议-finger
		if re.findall('no ip finger',s[j]):
			pp7 = 1  
		else:
			pass	
		#38，检查是否关闭不必要的功能-arp-proxy
		if re.findall(r'no ip proxy-arp',s[j]):
			pp8 = 1                          
		else:
			pass
		#39，检查是否关闭不必要的功能-redirect
		if re.findall(r'no ip redirects',s[j]):
			pp9 = 1                          
		else:
			pass		
		#40，检查是否配置全面的网络风暴防护
		if re.findall(r'storm-control broadcast.unicast(.|\n)*multicast',s[j]):
			qq1 = 1                          
		else:
			pass				
#R&S开关
		if re.findall(r'switchport',f):
			rors = 1                          
		else:
			pass
#1	
	if aa1 == 0:
		lastfile.write('.未设置密文存放的enable密码' + "\r\n") 
	else:
		pass  	
#2			
	if aa2 == 0:
		lastfile.write('.未密文存放用户密码' + "\r\n") 
	else:
		pass
#3				
	if bb1 == bb2 == 0:
		lastfile.write('.console密码未配置' + "\r\n") 
	else:
		pass  
#4	
	if cc1 == 0:
		lastfile.write('.未配置SSH登录管理' + "\r\n")  
	else:
		pass	
#5			
	if dd1 == 0:
		lastfile.write('.未限制远程可登录IP范围' + "\r\n")  
	else:
		pass	
#6
	if ee1 == 0:
		lastfile.write('.vty接口未配置登录认证' + "\r\n")  
	else:
		pass	
#7
	if ff1 == 0:
		lastfile.write('.SSH超时未配置' + "\r\n")  
	else:
		pass
#8
	if ff2 == 0:
		lastfile.write('.vty超时未配置' + "\r\n")  
	else:
		pass
#9
	if ff3 == 0:
		lastfile.write('.console超时未配置' + "\r\n")  
	else:
		pass
#10
	if ff4 == 0:
		lastfile.write('.aux超时未配置' + "\r\n")  
	else:
		pass
#11
	if gg1 == 0:
		lastfile.write('.未配置设备远程审计功能' + "\r\n")  
	else:
		pass	
#12
	if hh1 == 0:
		lastfile.write('.AAA认证未启用' + "\r\n")  
	else:
		pass
#13
	if ii1 == 0:
		lastfile.write('.RADIUS服务器未配置' + "\r\n")  
	else:
		pass
#14
	if ii2 == 0:
		lastfile.write('.TACACS服务器未配置' + "\r\n")  
	else:
		pass	
#15
	if jj1 == 0:
		lastfile.write('.SNMPv3未启用' + "\r\n")  
	else:
		pass
#16			
	if jj2 == 0:
		lastfile.write('.SNMP的community权限未设置为RO' + "\r\n")  
	else:
		pass	
#17		
	if kk1 == 0:
		lastfile.write('.未配置统一的日志源地址' + "\r\n")  
	else:
		pass	
#18			
	if kk2 == 0:
		lastfile.write('.未配置远程日志功能' + "\r\n")  
	else:
		pass
#19		
	if ll1 == 1 and ll2 == 0:
		lastfile.write('.VRRP未启用协议加密' + "\r\n")  
	else:
		pass	
#20
	if ll3 == 1 and ll4 == 0:
		lastfile.write('.HSRP未启用协议加密' + "\r\n")  
	else:
		pass	
#21
	if ll5 == 1 and ll6 == 0:
		lastfile.write('.ISIS未启用协议加密' + "\r\n")  
	else:
		pass
#22
	if ll7 == 1 and ll8 == 0:
		lastfile.write('.EIGRP未启用协议加密' + "\r\n")  
	else:
		pass
#23
	if ll9 == 1 and ll10 == 0:
		lastfile.write('.OSPF未启用协议加密' + "\r\n")  
	else:
		pass
#24
	if ll11 == 1 and ll12 == 0:
		lastfile.write('.RIP未启用协议加密' + "\r\n")  
	else:
		pass
#25
	if ll13 == 1 and ll14 == 0:
		lastfile.write('.BGP未启用协议加密' + "\r\n")  
	else:
		pass
#26
	if mm1 == 1 and mm2 == 0:
		lastfile.write('.BGP未启用防路由风暴功能' + "\r\n")  
	else:
		pass
#27
	if mm1 == 1 and mm3 == 0:
		lastfile.write('.BGP未对路由更新进行过滤' + "\r\n")  
	else:
		pass
#28
	if nn1 == 0:
		lastfile.write('.NTP未启用' + "\r\n")  
	else:
		pass
#29
	if nn1 == 1 and nn2 == 0:
		lastfile.write('.NTP未配置协议加密' + "\r\n")  	
	else:
		pass	
#30
	if oo1 == 0 and oo2 == 0:
		lastfile.write('.保持激活服务未开启' + "\r\n")  
	else:
		pass		
#31
	if pp1 == 0:
		lastfile.write('.CDP未关闭' + "\r\n")  
	else:
		pass	
#32		
	if pp2 == 0:
		lastfile.write('.PAD未关闭' + "\r\n")  
	else:
		pass	
#33	
	if pp3 == 0:
		lastfile.write('.BOOTP未关闭' + "\r\n")  
	else:
		pass	
#34		
	if pp4 == 0:
		lastfile.write('.源路由转发未关闭' + "\r\n")  
	else:
		pass	
#35			
	if pp5 == 0:
		lastfile.write('.HTTP未关闭' + "\r\n")  
	else:
		pass	
#36		
	if pp6 == 0:
		lastfile.write('.small未关闭' + "\r\n")  
	else:
		pass	
#37		
	if pp7 == 0:
		lastfile.write('.finger未关闭' + "\r\n")  
	else:
		pass
#38
	if pp8 == 0 and rors == 0:		#判定为路由设备且没有配置关闭ARP代理
		lastfile.write('.ARP代理未关闭' + "\r\n")  
	else:
		pass
#39
	if pp9 == 0 and rors == 0:#判定为路由设备且没有配置关闭IP重定向
		lastfile.write('.IP重定向由未关闭' + "\r\n")  
	else:
		pass
#40
	if qq1 == 0 and rors == 1:
		lastfile.write('.未配置网络风暴防护' + "\r\n")  
	else:
		pass		
	print str(m) + 'th device of Cisco is OK!'   
	lastfile.close() 
crm = open('Cisco.txt')
cro = crm.read() 
#print o 
crp = cro.split('+----------------------------+\n')
czong = open('Ciscozong.txt','a')
czong.write('***********************************配置核查报表************************************')


#1
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0001'+"\r\n")
czong.write('名称：检查是否设置密文存放enable密码'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未设置密文存放的enable密码',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('设置密文存放enable密码'+"\r\n")
czong.write('Router(config)#enable secret ********')
#2
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0002'+"\r\n")
czong.write('名称：检查是否设置密文存放所有用户密码'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未密文存放用户密码',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('设置密文存放enable密码'+"\r\n")
czong.write('Router(config)#username manager secret ********')
#3
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0003'+"\r\n")
czong.write('名称：检查是否配置console密码'+"\r\n")
czong.write('说明：：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('console密码未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('设置console密码'+"\r\n")
czong.write('Router(config)#line con 0'+"\r\n")
czong.write('Router(config-line)# login authentication **'+"\r\n")
czong.write('或'+"\r\n")
czong.write('Router(config-line)# password 0(或7) ***')
#4		
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0004'+"\r\n")
czong.write('名称：检查是否配置使用SSH登录管理'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未配置SSH登录管理',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置采用SSH登录管理'+"\r\n")
czong.write('Router(config)#line vty <num1> [<num2>]'+"\r\n")
czong.write('Router(config-line)#transport input ssh')		
#5	
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0005'+"\r\n")
czong.write('名称：检查是否限制允许远程登录的IP地址范围'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未限制远程可登录IP范围',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('限制允许远程登录的IP地址范围'+"\r\n")
czong.write('Switch(config)#line vty <num1> [<num2>]'+"\r\n")
czong.write('Switch(config-line)#access-class <tag> in')
#6
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0006'+"\r\n")
czong.write('名称：检查是否设置vty接口登录认证'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('vty接口未配置登录认证',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('参考配置手册设置vty接口登录认证')
#7
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0007'+"\r\n")
czong.write('名称：检查是否配置SSH超时'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('SSH超时未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置SSH超时'+"\r\n")
czong.write('Switch(config)#ip ssh time-out <secr> ')		
#8
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0008'+"\r\n")
czong.write('名称：检查是否配置VTY超时'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('vty超时未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置VTY超时'+"\r\n")
czong.write('Router(config)#line vty <num1> [<num2>] '+"\r\n")
czong.write('Router(config-line)#exec-timeout <mins> ')				
#9
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0009'+"\r\n")
czong.write('名称：检查是否配置console口超时'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('console超时未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置console口超时'+"\r\n")
czong.write('Router(config)#line console 0 '+"\r\n")
czong.write('Router(config-line)#exec-timeout <mins> ')				
#10
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0010'+"\r\n")
czong.write('名称：检查是否配置AUX口超时'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('aux超时未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置aux口超时'+"\r\n")
czong.write('Switch(config)#line aux 0 '+"\r\n")
czong.write('Switch(config-line)#exec-timeout <mins> ')	
#11			
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0011'+"\r\n")
czong.write('名称：检查是否配置远程认证服务器审计功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未配置设备远程审计功能',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置远程认证服务器审计功能'+"\r\n")
czong.write('Router(config)#aaa accounting system default start-stop group <server> '+"\r\n")
czong.write('Router(config)#aaa accounting exec default start-stop group <server> '+"\r\n")
czong.write('Router(config)#aaa accounting commands <level> default start-stop group <server> '+"\r\n")
czong.write('Router(config)#aaa accounting network default start-stop group <server> ')		
#12
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0012'+"\r\n")
czong.write('名称：检查是否配置AAA认证'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('AAA认证未启用',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置AAA认证'+"\r\n")
czong.write('Router(config)#aaa new-model '+"\r\n")
czong.write('Router(config)#aaa authentication login default local <server> ')
#13
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0013'+"\r\n")
czong.write('名称：检查是否配置RADIUS认证服务器'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('RADIUS服务器未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置RADIUS认证服务器'+"\r\n")
czong.write('Router(config)#radius-server key ******* '+"\r\n")
czong.write('Router(config)#radius-server host 192.168.1.100 ')
#14
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0014'+"\r\n")
czong.write('名称：检查是否配置TACACS认证服务器'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('TACACS服务器未配置',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置TACACS认证服务器'+"\r\n")
czong.write('Router(config)#tacacs-server key ******** '+"\r\n")
czong.write('Router(config)#radius-server host 192.168.1.100 ')
#15
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0015'+"\r\n")
czong.write('名称：检查是否配置启用SNMPv3'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('SNMPv3未启用',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用SNMPv3'+"\r\n")
czong.write('Router(config)#snmp-server host <ip> version 3 auth <username> '+"\r\n")
czong.write('其中<ip>表示IP，<username>表示用户名')
#16	
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0016'+"\r\n")
czong.write('名称：检查是否配置SNMP的community权限为RO'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('SNMP的community权限未设置为RO',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置SNMP的community权限为RO'+"\r\n")
czong.write('Router(config)#snmp-server community <name> <RO> [<tag>] '+"\r\n")
czong.write('其中<name>表示community名称，<RO/RW>表示分配的权限，<tag>表示access-list标号。')		
#17			
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0017'+"\r\n")
czong.write('名称：检查是否配置统一的日志源地址'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未配置统一的日志源地址',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置统一的日志源地址'+"\r\n")
czong.write('Switch(config)#logging source-interface loopback0 ')		
#18			
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0018'+"\r\n")
czong.write('名称：检查是否配置远程日志功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('未配置远程日志功能',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置远程日志功能'+"\r\n")
czong.write('Switch(config)#logging <ip> '+"\r\n")
czong.write('其中<ip>表示远程日志服务器，需要先配置日志服务器。')		
#19
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0019'+"\r\n")
czong.write('名称：检查是否配置启用VRRP的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('VRRP未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用VRRP的协议认证功能'+"\r\n")
czong.write('Router(config)#interface <InterfaceName> '+"\r\n")
czong.write('Router(config-if)#vrrp 1 authentication md5 key-string <key> ')
#20
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0020'+"\r\n")
czong.write('名称：检查是否配置启用HSRP的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('HSRP未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用HSRP的协议认证功能'+"\r\n")
czong.write('Router(config)#interface <InterfaceName> '+"\r\n")
czong.write('Router(config-if)#standby 1 authentication md5 key-string <key> ')
#21
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0021'+"\r\n")
czong.write('名称：检查是否配置启用ISIS的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('ISIS未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用ISIS的协议认证功能'+"\r\n")
czong.write('Router(config)#router isis'+"\r\n")
czong.write('Router(config-router)#authentication mod md5 level-1 ')
#22
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0022'+"\r\n")
czong.write('名称：检查是否配置启用EIGRP的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('EIGRP未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用EIGRP的协议认证功能'+"\r\n")
czong.write('Router(config-if)#ip authentication mode eigrp * md5 ')
#23
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0023'+"\r\n")
czong.write('名称：检查是否配置启用OSPF的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('OSPF未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用OSPF的协议认证功能'+"\r\n")
czong.write('Router(config-if)#ip ospf message-digest-key 1 md5 *** ')
#24
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0024'+"\r\n")
czong.write('名称：检查是否配置启用RIP的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('RIP未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用RIP的协议认证功能'+"\r\n")
czong.write('Router(config-if)ip rip authentication mod md5 ')
#25
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0025'+"\r\n")
czong.write('名称：检查是否配置启用BGP的协议认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('BGP未启用协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用BGP的协议认证功能'+"\r\n")
czong.write('Router(config)#router bgp [as_num] '+"\r\n")
czong.write('Router(config-router)#neighbor [neighbor_addr] remote-as [remote_as_num] '+"\r\n")
czong.write('Router(config-router)#neighbor [neighbor_addr] password ****')
#26
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0026'+"\r\n")
czong.write('名称：检查是否配置启用BGP防路由风暴功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('BGP未启用防路由风暴功能',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置启用BGP防路由风暴功能'+"\r\n")
czong.write('Router(config-router)#bgp dampening ')
#27
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0027'+"\r\n")
czong.write('名称：检查是否配置BGP对路由更新信息过滤'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('BGP未对路由更新进行过滤',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置BGP对路由更新信息过滤'+"\r\n")
czong.write('Router(config-router)#neighbor <ip> prefix-list <listname> out ')
#28
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0028'+"\r\n")
czong.write('名称：检查是否配置NTP时间同步'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('NTP未启用',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置NTP时间同步'+"\r\n")
czong.write('Router(config)#ntp server <ip> '+"\r\n")
czong.write('其中<ip>表示NTP服务器IP')					
#29
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0029'+"\r\n")
czong.write('名称：检查是否配置启用NTP协议的认证功能'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('NTP未配置协议加密',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('启用NTP协议的加密功能'+"\r\n")
czong.write('Router(config)#ntp authenticate '+"\r\n")
czong.write('Router(config)#ntp trusted-key key_id '+"\r\n")
czong.write('Router(config)#ntp authentication-key key_id md5 *** '+"\r\n")
czong.write('Router(config)#ntp server X.X.X.X key key_id ')
#30
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0030'+"\r\n")
czong.write('名称：检查是否开启保持激活服务'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('保持激活服务未开启',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('开启保持激活服务'+"\r\n")
czong.write('Router(config)#service tcp-keepalives-in '+"\r\n")
czong.write('Router(config)#service tcp-keepalives-out ')
#31	
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0031'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-CDP'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('CDP未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭CDP'+"\r\n")
czong.write('Router(config)#no cdp run')			
#32		
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0032'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-PAD'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('PAD未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭PAD'+"\r\n")
czong.write('Router(config)#no service pad')				
#33
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0033'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-BOOTP'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('BOOTP未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭BOOTP'+"\r\n")
czong.write('Router(config)#no ip bootp server')				
#34	
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0034'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-源路由转发'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('源路由转发未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭源路由转发'+"\r\n")
czong.write('Switch(config)#no ip source-route')		
#35	
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0035'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-HTTP'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('HTTP未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭HTTP服务'+"\r\n")
czong.write('Router(config)#no ip http server')
#36
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0036'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-small'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('small未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭small服务'+"\r\n")
czong.write('Router(config)#no service udp-small-servers'+"\r\n" )
czong.write('Router(config)#no service tcp-small-servers ')		
#37
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0037'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-finger'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('finger未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭finger服务'+"\r\n")
czong.write('Router(config)#no ip finger')		
#38
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0038'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-ARP代理'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('ARP代理未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭ARP代理'+"\r\n")
czong.write('Router(config-if)no ip proxy-arp ')		
#39
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0039'+"\r\n")
czong.write('名称：检查是否关闭不必要的功能-IP重定向'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	crq = crp[x].split(':')
	if re.findall('IP重定向由未关闭',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('关闭IP重定向'+"\r\n")
czong.write('Router(config-if)#no ip redirects ')	
#40
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")
czong.write('编号：Cisco-0040'+"\r\n")
czong.write('名称：检查是否配置网络风暴防护'+"\r\n")
czong.write('说明：'+"\r\n")
czong.write('检查方法：手工检查show running-config命令的输出结果'+"\r\n")
czong.write('不合规设备：')
for x in range(0,len(crp)):
	csq = crp[x].split('*')
	if re.findall('未配置网络风暴防护',crp[x]):
		czong.write(crq[1]+',')
	else:
		pass
czong.write("\r\n"+'修复方法（参考）：'+"\r\n")
czong.write('配置网络风暴防护'+"\r\n")
czong.write('Switch(config)#interface <InterfaceName> '+"\r\n")
czong.write('Switch(config-if)#storm-control broadcast level <threshold> '+"\r\n")
czong.write('Switch(config-if)#storm-control unicast level <threshold> '+"\r\n")
czong.write('Switch(config-if)#storm-control multicast level <threshold> ')


	
czong.write("\r\n"+'+---------------------------------------------------------------------------------+'+"\r\n")								
czong.close()
print 'All is OK!'





'''
详细配置检查项：
#1，检查口令加密存放-enable密码-aa1
#2，检查口令加密存放-用户密码-aa2
#3，检查是否已配置console接口密码-bb1-bb2
#4，检查是否使用加密协议进行远程管理-cc1
#5，检查是否限制可远程登录管理的IP地址-dd1
#6，检查是否配置vty登录认证-ee1
#7，检查是否已配置超时登出时间-ssh-ff1
#8，检查是否已配置超时登出时间-vty-ff2
#9，检查是否已配置超时登出时间-con-ff3
#10，检查是否已配置超时登出时间-aux-ff4

#11，检查是否配置远程认证服务器审计功能-gg1
#12，检查是否启用AAA认证服务器-hh1
#13，检查是否配置radius认证服务器-ii1
#14，检查是否开启tacacs认证服务器-ii2
#15，检查是否启用SNMPv3-jj1
#16，检查是否SNMP community 权限是否仅为RO-jj2

#17，检查是否配置统一设备的系统日志源地址-kk1
#18，检查是否已开启远程日志功能-kk2

#19，检查路由协议是否启用协议加密功能-vrrp-ll1-ll2
#20，检查路由协议是否启用协议加密功能-hsrp-ll3-ll4
#21，检查路由协议是否启用协议加密功能-isis-ll5-ll6
#22，检查路由协议是否启用协议加密功能-eigrp-ll7-ll8
#23，检查路由协议是否启用协议加密功能-ospf-ll9-ll10
#24，检查路由协议是否启用协议加密功能-rip-ll11-ll12
#25，检查路由协议是否启用协议加密功能-bgp-ll13-ll14
#26，检查是否启用BGP防广播风暴功能-mm1-mm2
#27，过滤路由更新-mm1-mm3

#28，是否配置NTP-nn1
#29，检查NTP协议是否启用协议加密功能-nn2
#30，检查是否开启连接保持-oo1-oo2
#31，是否关闭不必要的协议-cdp-pp1
#32，是否关闭不必要的协议-pad-pp2
#33，是否关闭不必要的协议-bootp-pp3
#34，是否关闭不必要的协议-source-route-pp4
#35，是否关闭不必要的协议-http-pp5
#36，是否关闭不必要的协议-small-pp6
#37，是否关闭不必要的协议-finger-pp7
#38，检查是否关闭不必要的功能-arp代理-pp8
#39，检查是否关闭不必要的功能重定向-pp9
#40，检查是否配置全面的网络风暴防护（交换机独有）

以上为本脚本所有的检查项目，是一个比较复杂的版本。
下面是一些比较的检查项目，适用于农信银行这一类配置文件不允许信息泄露的重要客户：
一,用户安全
(1)帐号按需分配，无关账号删除
(2)口令复杂度，密文存储口令
(3)远程使用SSH，登录IP限制，超时登出
二,日志审计
(1)日志完整完备
(2)远程日志存储
三,功能安全
(1),自身的安全性配置
(2),关闭不必要的端口和功能
'''
