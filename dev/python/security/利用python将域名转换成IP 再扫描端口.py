
#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
# python www.iplaypy.com
# python 域名转IP 在查看制定端口是否开放
#  刚学写的不好请大家见谅
####################################################################

import socket
#获取域名的IP地址
def www_ip(name):  #域名转IP
    try:
        result = socket.getaddrinfo(name, None)
        return result[0][4][0]
    except:
        return 0

def ip_port(ip):  #查看IP端口是否开放
    port=21
    s=socket.socket()
    #address="127.0.0.1"
    try:
        s.connect((ip,port))
        #print 'IP:',ip,"port:",port,"以开放"
        return 1
    except socket.error,e:
        #print 'IP:',ip,"port:",port,"未开放"
        return 0

if __name__=='__main__':
    www= "www.iplaypy.com"
    IP=www_ip(www)
    if IP:
        print www,"ip地址：",IP
        if ip_port(IP):
            print IP,"开放21端口"
        else:
            print IP,"未开21放端口"
    else:
        print www,"域名转IP失败" 
