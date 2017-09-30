

#encoding=utf-8

IP = '203.208.33.100'#This IP is : g.cn

IP1 = IP.split('.')[0]
IP2 = IP.split('.')[1]
IP3 = IP.split('.')[2]
IP4 = IP.split('.')[3]

print 'Your IP is : ' + IP
print '---------------www.iplaypy.com------------------'
print 'Your Decimal IP is : ' + \
        str(int(IP1)*256**3 + \
            int(IP2)*256**2 + \
            int(IP3)*256 + \
            int(IP4))

