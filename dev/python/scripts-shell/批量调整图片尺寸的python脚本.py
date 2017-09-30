
#coding:utf-8
#author:solu

import sys, os
from PIL import Image
from optparse import OptionParser

#遍历指定目录下的JPG图片，返回list
def walk_dir(dir):
	image_list = []
	for root, dirs, files in os.walk(dir):
		for name in files:
			ext = os.path.splitext(name)[1][1:]
			if (ext.lower() == 'jpg'):
				path = root + os.sep + name
				image_list.append(path)
	return image_list

#保存图片,默认保存在图片目录下的thumb
def resize_save(im, width, path):
	image_name = im.filename.split(os.sep)[-1]
	save_name = path + os.sep + image_name
	size = auto_resize(im, width)
	new_im = im.resize(size)
	print save_name
	new_im.save(save_name)

#调整宽高
def auto_resize(im, width):
	size = im.size
	height = int(float(width) / size[0] * size[1])
	return (int(width), height)

if __name__ == '__main__':
	usage_msg = 'usage: %prog -p <image_path> -w <image_width>'
	parser = OptionParser(usage_msg)
	parser.add_option("-p","--path", dest = "image_path", help = u"存放相片的路径")
	parser.add_option("-w","--width", dest = "image_width", help = u"调整后的图片宽度(高度会自等比例缩放)")
	options, args = parser.parse_args()
	if not options.image_path or not options.image_width:
		parser.print_help()
		sys.exit(1)
	
	try:
		image_path = unicode(options.image_path, 'gbk')
		width = options.image_width
		#创建文件夹
		save_path = image_path + os.sep + 'thumb'
		if (not os.path.exists(save_path)):
			os.mkdir(save_path)
		
		image_list = walk_dir(image_path)
		for path in image_list:
			im = Image.open(path)
			resize_save(im, width, save_path)
	except Exception,e:
		print('Error:',e)
#www.iplaypy.com