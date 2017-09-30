
#!/usr/local/bin/python3.2
import urllib.request,io,os,sys

req = urllib.request.Request("http://www.google.com")

f = urllib.request.urlopen(req)

s = f.read()

s = s.decode('gbk','ignore')

mdir = sys.path[0]+'/'

file = open(mdir+'admin6.txt','a',1,'gbk')

file.write(s)
file.close()

#www.iplaypy.com