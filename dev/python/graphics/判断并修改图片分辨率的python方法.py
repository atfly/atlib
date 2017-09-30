
# -*- coding: utf-8 -*-

import os,sys,Image

rootDir = r'c:\images'
targetDir = r'c:\imagesover'

def encodeChinese(msg):
	type = sys.getfilesystemencoding()
	return msg.decode('UTF-8').encode(type)

errFile = open(r'c:\errFile.txt','w')

def judgeSize(im):
	#判断图片分辨率,如果最大边超过1024返回False,如果不超过返回True
        mySize = im.size
	maxValue = max(mySize)
        minValue = min(mySize)
	if(maxValue > 1024):
		return False
	else:
		return True

#www.iplaypy.com
def returnSize(im):
	#返回图片大小,返回两个值,第一个返回值总为最大
	max,min = im.size
	if max > min:
		return max,min
	else:
		return min,max

def changeSize(im,max,min):
	value = max/1024
	min = min/value
	newimg = im.resize((1024,min),Image.ANTIALIAS)
	return newimg

def main():
	for parent,dirnames,filenames in os.walk(rootDir):
		for filename in filenames:
			fName = filename
			filename = parent + os.sep + filename
			fPostfix = os.path.splitext(filename)[1]
			try:
				img = Image.open(filename)
			except:
				print filename
				print encodeChinese('打开这个文件出错')
				continue
			#img.load()
			print filename
			print fPostfix
			if(fPostfix !='.jpg' and fPostfix !='.png' and fPostfix != '.JPG' and fPostfix != '.PNG'):
				errFile.write(str(filename) + '\n')
				errFile.write(encodeChinese('上面这个文件不是图片,请检查...') + '\n')
				errFile.write('\n')
			else:
				print 'juageSize()'	
				if(judgeSize(img) == False):
					print 'judgeSize == False'
					max,min = returnSize(img)
					newimg = changeSize(img,max,min)
					newimg.save(targetDir + os.sep + fName)
					print str(targetDir + os.sep + fName) 
					print encodeChinese('保存完毕')
	print encodeChinese('处理完毕')
	errFile.close()

main()