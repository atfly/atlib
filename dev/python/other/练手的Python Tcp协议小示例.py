

#------------------服务端代码server.py---------------------------
#coding:utf-8

import socket
import datetime

"""
定义基本的信息
"""
HOST = ""            #主机
PORT = 23151         #端口
ADD = (HOST, PORT)
BUFFERSIZE = 1024    #缓冲区大小

"""
建立socket，绑定地址和开始监听
"""
TcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #创建socket
TcpSerSock.bind(ADD)       #绑定地址和端口
TcpSerSock.listen(10)      #开始监听，监听数目同时间不超过10个

"""
socekt建好后，开始进行连接和数据的传输
"""
print "服务器等待连接......"
TcpCliSock, addr = TcpSerSock.accept()  #开始连接
while True:
	date = TcpCliSock.recv(BUFFERSIZE)   #接受数据
	if date:     #如果接受到了数据
		curTime = datetime.datetime.now()  #获得当前时间 格式是：datetime.datetime(2012, 3, 13, 1, 29, 51, 872000)
		curTime = curTime.strftime('%Y-%m-%m %H:%M:%S')     #转换格式
		print "%s  %s" % (addr, curTime) 
		print date
		#发数据
		sendDate = raw_input("input:")
		TcpCliSock.send('%s' % (sendDate))   #发数据	
		if date == '88':
			break	

#www.iplaypy.com	
"""
连接完毕，关闭套接字
"""
print "server close"
TcpCliSock.close()
TcpSerSock.close()

#--------------客户端代码 client.py------------------
#coding:utf-8

import socket
import datetime

"""
定义基本的信息: 主机和端口要和服务器一致
"""
HOST = "localhost"  #服务其地址
PORT = 23151       #服务器端口
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

"""
建立套接字,开始连接
"""
TCPClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPClient.connect(ADDR) #连接服务器

"""
开始进行数据的传输
"""
while True:
	senddate = raw_input("input:")
	if senddate:
		TCPClient.send('%s' % (senddate))  #发送数据
		
	recvdate = TCPClient.recv(BUFFERSIZE)    #接受数据
	curTime = datetime.datetime.now()  #获得当前时间 格式是：datetime.datetime(2012, 3, 13, 1, 29, 51, 872000)
	curTime = curTime.strftime('%Y-%m-%m %H:%M:%S')     #转换格式
	print "%s  %s" % (HOST, curTime)
	print  recvdate
	if recvdate == '88':
			break	
	
"""
传输完毕，关闭套接字
"""
print "client close"
TCPClient.close()
