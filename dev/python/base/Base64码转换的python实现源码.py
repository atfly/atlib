
#! /usr/bin/env python
#coding=utf-8
import base64

a = input("Enter string:")
b = base64.encodestring(a) # Encode for string
print b
print base64.decodestring(b) # Decode for string

f = open('temp.jpg','rb')
c = f.read()

x = base64.encodestring(c) # Encode for file
f.close()
print len(x)
print "".join(x.split())

base64.decodestring(x) # Decode for file
file1 = open('temp','wb')
file1.write(base64.decodestring(x))
#www.iplaypy.com