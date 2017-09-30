
#coding=utf-8

import socket
import sys
import select
import threading

host='192.168.99.100'
port=80
#www.iplaypy.com

class Thread(threading.Thread):
    def __init__(self,buf,sockfd):
        threading.Thread.__init__(self)
        self.buf=buf
        self.sockfd=sockfd

    def run(self):
      if len(self.buf)!=0:

        if 'GET' in self.buf :    #判断是否是浏览器提交的数据如果是则将提交的数据转发至本地环回地址的80端口
          s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s2.connect(('127.0.0.1',80))
          s2.send(self.buf)
          bufer=''

          while 1:
            recv_data=s2.recv(1024)
            bufer+=recv_data

            if len(recv_data)==0:
              break

          print bufer,len(bufer) 

          if len(bufer)==0:
            pass           

          self.sockfd.send(bufer)    #将服务器发送的数据发回客户端
          s2.close
          self.sockfd.close 
          sys.exit()

        else:
          'ps:connect to ssh'  #如果数据不是浏览器提交则将其转发至本地的22端口
          s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s2.connect(('127.0.0.1',22))
          s2.send(self.buf)
          recv_data=s2.recv(4096)
          conn.send(recv_data)
          self.sockfd.close
          s2.close 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )  #端口复用的关键点
s.bind((host,port))
s.listen(10)

while 1:
  infds,outfds,errfds=select.select([s,],[],[],5)  #使用select函数进行非阻塞操作

  if len(infds)!=0:
    conn,(addr,port)=s.accept()

    print 'connected by',addr,port

    data=conn.recv(1024)
    t=Thread(data,conn)
    t.start()

s.close