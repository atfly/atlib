
# -*- coding: utf-8 -*-
import numpy
import Image
import os
import sys

def encodeChinese(msg):
	type = sys.getfilesystemencoding()
	return msg.decode('UTF-8').encode(type)

rootdir = r'c:\users\mingl_wang\desktop\test2'
targetdir = r'c:\users\mingl_wang\desktop\test3'

#www.iplaypy.com
for parent,dirnames,filenames in os.walk(rootdir):
	for filename in filenames:
		fName = filename;
		print fName
		filename = rootdir + os.sep + filename
		fn,fPostfix = os.path.splitext(filename)
		if(fPostfix == '.jpg'):
			print fName + encodeChinese('  请按照红绿蓝顺序依次输入背景色参数,\
我们将按照您输入的数值进行裁剪:') + '\n'
			try:
				print encodeChinese('红色的参数(0~255): ')
				red = int(raw_input())
			except:
				print encodeChinese('您输入的不是数字,请重新输入红色参数(0~255): ')
				red = int(raw_input())
			try:
				print encodeChinese('绿色的参数(0~255): ')
				green = int(raw_input())
			except:
				print encodeChinese('您输入的不是数字,请重新输入绿色参数(0~255): ')
				green = int(raw_input())
			try:
				print encodeChinese('蓝色的参数(0~255): ')
				bule = int(raw_input())
			except:
				print encodeChinese('您输入的不是数字,请重新输入蓝色参数(0~255): ')
				bule = int(raw_input())
			item = list() 
			item.append((red,green,bule))
			print item[0][0]
			print item[0][1]
			print item[0][2]
			print 'item: ' + str(item) + '\n'
			img = Image.open(filename)
			#img = img.convert('RGBA')
			newImg = Image.new('RGBA',img.size)
			print 'newImg.mode: ' + str(newImg.mode)
			imgData = img.getdata()
			newData = list()
			for newItem in imgData:
				if(newItem[0] == item[0][0] and newItem[1] == item[0][1] and newItem[2] == item[0][2]):
					newData.append((newItem[0],newItem[1],newItem[2],0))
				else:
					newData.append((newItem[0],newItem[1],newItem[2],255))
					#print encodeChinese('不相等的情况: ') + str(newItem) + '\n'
			print 'hello'
			newImg.putdata(newData)
			fName,fpost = fName.split('.')
			print 'fName ' + str(fName)
			fpost =fName + '.png'
			print 'fpost :' + str(fpost)
			newImg.save(targetdir + os.sep + fpost)