
#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
解数独
'''
#import sys,os

def scan(temp,i):
	heng=temp[(i/9*9):(i/9*9+9)]
	shu=[]
	for i0 in range(0,73,9):
		shu.append(temp[i%9+i0])
	kuai=[]
	row=i%9/3*3
	line=i/27*3
	for i0 in range(0,3):
		kuai.append(temp[line*9+row+i0])
		kuai.append(temp[(line+1)*9+row+i0])
		kuai.append(temp[(line+2)*9+row+i0])
	hsk=heng+shu+kuai
	hsk=list(set(hsk))
	data=[0,1,2,3,4,5,6,7,8,9]
	map(data.remove,hsk)
	return data

def myprint(temp):
	if not temp:
		print 'None'
	else:
		for i in range(0,73,9):
			print temp[i:i+9]

#www.iplaypy.com