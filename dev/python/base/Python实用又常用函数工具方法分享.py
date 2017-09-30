
# -*- coding: utf-8 -*-
import numpy
import Image
import os
import sys

def encodeChinese(msg):
	type = sys.getfilesystemencoding()
	return msg.decode('UTF-8').encode(type)
def check_imgMode(filedir):
	try:
		img = Image.open(filedir)
		return img.mode
	except:
		errInfo = encodeChinese('这不是图片: ') + str(filedir) + '\n'
		print errInfo
		return errInfo
def check_fileMode(filedir):
	fPostfix = os.path.splitext(filedir)[1]
	return fPostfix
def open_imgFile(filedir):
	im = Image.open(filedir)
	im.load()
	return im
def input_rootdir():
	print encodeChinese('请输入要检测的文件夹路径: ')
	rootdir = raw_input()
	print rootdir
	return rootdir
def input_logdir():
	print encodeChinese('请输入错误日志路径: ')
	logdir = raw_input()
	print logdir
	return logdir
def input_targetdir():
	print encodeChinese('请输入处理完成后文件保存路径: ')
	targetdir = raw_input()
	return targetdir
def check_fileSize(filedir):#www.iplaypy.com
	try:
		f = open(filedir,'rb')
		f.seek(0,2)
		fSize = f.tell()
		#print 'fSize: ' + str(type(fSize))
		#f.close()
		return f.tell()
	except:
		print encodeChinese('获取文件大小时发生错误')
def check_png_alpha(rootdir,errLogDir):
	errFile = open(errLogDir,'w')
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			fName = filename
			filename = rootdir + os.sep + filename
			if check_fileMode(filename) == '.png':
				if check_imgMode(filename) == 'RGBA':
					print filename
					try:
						img = open_imgFile(filename)
					except:
						filename = parent + os.sep + fName
						print encodeChinese('这不是图片: ') + str(filename) +'\n'
						errFile.write(encodeChinese('这不是图片: ') + '\n')
						errFile.write(str(filename) + '\n')
						errFile.write('\n')
					alpha = img.split()[3]
					arr = numpy.asarray(alpha)
					count = 0
					fo
2966
r i in range(0,img.size[0]-1):
						for j in range(0,img.size[1]-1):
							if arr[j][i] < 128:
								count += 1
								if count > 10:
									break
					if count > 10:
						filename = parent + os.sep + fName
						print str(filename) + ' is have alpha,count = ' + str(count)
					else:
						filename = parent + os.sep + fName
						errFile.write(encodeChinese('这张图片约等于没有alpha通道: ') + '\n')
						errFile.write(str(filename) + '\n')
						errFile.write('\n')
				else:
					filename = parent + os.sep +fName
					errFile.write(encodeChinese('虽然这是一张png图片,但是它没有alpha通道: ') + '\n')
					errFile.write(str(filename) + '\n')
					errFile.write('\n')
			else:
				filename = parent + os.sep +fName
				errFile.write(encodeChinese('这不是png格式的文件: ') + '\n')
				errFile.write(str(filename) + '\n')
				errFile.write('\n')
	errFile.close()
def check_texture(rootdir,errLogDir):
	errFile = open(errLogDir,'w')
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			fName = filename
			filename = rootdir + os.sep + filename
			if (check_fileMode(filename) == '.jpg' or check_fileMode(filename) == '.png'):
				fSize = check_fileSize(filename)
				if(fSize / 1024 > 1024):
					filename = parent + os.sep + fName
					print rootdir
					errFile.write(filename+'\n')
					err_sizeFile=encodeChinese('文件大小超过1024')
					errFile.write(err_sizeFile + ': ' + str(check_fileSize(filename)/1024) +'\n')
					errFile.write('\n')
				elif(fSize / 1024 <= 1024):
					img = open_imgFile(filename)
					imgSize = img.size
					if(imgSize[0] % 64 != 0 or imgSize[1] % 64 != 0):
						print parent
						print filename
						print img.size
						value=parent+os.sep+fName
						errSize=img.size
						errFile.write(value+'\n')
						err_bigFile=encodeChinese('文件分辨率错误')
						errFile.write(err_bigFile)#'the image so big: ')
						errFile.write(str(errSize)+'\n')
						errFile.write('\n')
			else:
				outPath=parent+os.sep+fName
				errFile.write(outPath+'\n')
				err_File=encodeChinese('文件格式不正确')
				errFile.write(err_File)#'the File err')
				errFile.write('\n')
				print fName
	errFile.close()
def autoCutImage(rootdir,targetDir):
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			fName = filename
			filename = rootdir+os.sep+filename
			fPostfix = check_fileMode(filename)
			value_r = 0
			value_g = 0
			value_b = 0
			count = 0
			if(fPostfix =='.png'):
				#os.chmod(filename,stat.S_IWRITE)
				img = open_imgFile(filename)
				if img.mode == 'RGBA':
					rgba = encodeChinese('这张是RGBA图片')
					print rgba
					img.load()
					data = img.getdata()
					data_a = list()
					for item in data:
						if(item[3] < 128):
							data_a.append((item[0],item[1],item[2],0))
						else:
							data_a.append((item[0],item[1],item[2],255))
					for item in data:
						if(item[3])== 255:
							count += 1
							value_r += item[0]
							value_g += item[1]
							value_b += item[2]
					value_r = value_r / count
					value_g = value_g / count
					value_b = value_b / count
					print value_r
					print value_g
					print value_b
					print count
					newdata = list()
					for item in data_a:
						if item[3] == 0:
							newdata.append((value_r,value_g,value_b,item[3]))
							#print newdata[0]
						elif item[3] == 255:
							newdata.append((item[0],item[1],item[2],item[3]))
							#print newdata[0]
							#print data_a
					print len(newdata)
					img.putdata(newdata)
					try:
						img.save(targetDir + os.sep+fName);
					except:
						print encodeChinese('保存文件出现错误,请检查被保存的文件夹是否存在,亦或是其它引起的错误')
					print str(fName) + ' save'
			 #如果它没有alpha通道
				elif img.mode == 'RGB':
					print 'RGB'
					img.load()
					#转换出一个alpha通道
					img = img.convert('RGBA')
					datas = img.getdata()
					mydata = list()
					newdata = list()
					for item in data:
						if item[0] == 0 and item[1] == 0 and item[2] == 0:
							mydata.append((item[0],item[1],item[2],0))
						else:
							mydata.append((item[0],item[1],item[2],255))
					for item in data:
						if item[3] == 255:
							count += 1
							value_r += item[0]
							value_g += item[1]
							value_b += item[2]
					value_r = value_r / count
					value_g = value_g / count
					value_b = value_b / count
					for item in mydata:
						newdata.append((value_r,value_g,value_b,item[3]))
					img.putdata(newdata)
					try:
						img.save(targetDir + os.sep + fName)
					except:
						print encodeChinese('保存文件出错,请检查被保存文件夹路径是否正确,亦或是其他原因导致')
		  #如果它不是png格式
			elif(fPostfix == '.jpg'):
				print '\n'
				print fName + encodeChinese(' 是一张JPG图片,请用工具4进行裁剪')
			else:
					not_png = encodeChinese('这张贴图既不是png也不是jpg,这张贴图的名字是: ')
					print not_png + fName
def jpgCutImage(rootdir,targetDir):
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			fName = filename;
			print fName
			filename = rootdir + os.sep + filename
			fPostfix = check_fileMode(filename)
			#fn,fPostfix = os.path.splitext(filename)
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
				newImg.save(targetDir + os.sep + fpost)
				try:
					alpha = newImg.split()[3]
					print 'alpha'
				except:
					print 'err'
def select_tools():
	select = raw_input()
	if select == '1':
		rootdir = input_rootdir()
		errLogDir = input_logdir()
		check_png_alpha(rootdir,errLogDir)
	elif select == '2':
		rootdir = input_rootdir()
		errLogDir = input_logdir()
		check_texture(rootdir,errLogDir)
	elif select == '3':
		rootdir = input_rootdir ()
		targetDir = input_targetdir()
		autoCutImage(rootdir,targetDir)
	elif select =='4':
		rootdir = input_rootdir()
		targetDir = input_targetdir()
		jpgCutImage(rootdir,targetDir)
	elif select =='5':
		print encodeChinese('谢谢您的使用^_^')
		exit()
	else:
		print encodeChinese('您输入的数字有误,请您重新启动程序....')
def menuDisplay():
	print encodeChinese('按照数字选择工具,并根据提示输入相应参数: ')
	print encodeChinese('1.检测图片alpha通道')
	print encodeChinese('2.检测图片格式')
	print encodeChinese('3.根据alpha通道裁剪贴图')
	print encodeChinese('4.裁剪JPG图片贴图')
	print encodeChinese('5.退出')
	select_tools()

def main():
	print '\n'
	print encodeChinese('#################################################################')
	print encodeChinese('#####################欢迎使用图片处理工具########################')
	print encodeChinese('#################################################################')
	print '\n'
	menuDisplay()

main()
