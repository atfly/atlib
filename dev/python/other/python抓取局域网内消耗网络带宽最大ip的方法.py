
import re
import urllib

url = 'http://admin:netcenter@192.168.0.1/analyze.cgi?page=1&px=3&sf=1'

a = urllib.urlopen(url).read()

#www.iplaypy.com

ip = re.findall(r'192\.168\.\d+\.\d+', a, re.M)

ip1 = ip[0]
ip2 = ip[1]
ip3 = ip[2]

print "当前消耗网络带宽最大的前三个ip是"+ip1+" "+ip2+" "+ip3