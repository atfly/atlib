
#coding:utf-8

import datetime
import os,sys
import re
from threading import Thread
import time

def getNow():#2010-06-04 11:46:04.992000
    return datetime.datetime.now()
output = ""

class PING(Thread):
	count = 0
	global output
	def __init__(self,ip=None):
		Thread.__init__(self)
		self.ip=ip
		self.__class__.count = self.__class__.count + 1
	def run(self):
		time.sleep(1)
		self.dataoutput = self.ip +self.ip
	def __del__(self):
		global output
		self.__class__.count = self.__class__.count - 1
		output = ("%s %s -->%s %s \n" %(output,self.ip,self.dataoutput,getNow()))
		pass


#www.iplaypy.com

i = 0
nums = 10  

while True:
	if i >= count:
		break
	else:
		T_thread=[]
		for j in range(nums):
			if i >= count:
				break
			else:
				t=PING(i)
				T_thread.append(t)
				print("i == %s " % (i))
				i += 1
		for j in range(len(T_thread)):
			print("--> %s  " % (j))
			T_thread[j].start()
		time.sleep(2) 
		del T_thread
		del t
print(output)
'''
class test:
	def __init__(self,ip):
		self.ip=ip
	def print1(self):
		print(self.ip)
t=test(50)
t.print1()
t=test(60)
t.print1()
''