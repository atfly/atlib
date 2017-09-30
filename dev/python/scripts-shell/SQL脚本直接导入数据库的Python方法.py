
#!/usr/bin/python
#coding=utf-8

import os
from datetime import datetime

path = "/Users/Demos/Desktop/ss/"
id = 0

#历遍指定文件夹
for x in os.listdir(path):

    #只获取文件夹里面的JPG文件
    if x.endswith(".jpg") or x.endswith(".JPG"):
        id += 1 #自增加ID
        title = x[:-4] #获取文件名作为标题
        #根据ID位数在前面补0，小于10 补两个，大于10补一个

        filename = {1:"00" + str(id), 2:"0" + str(id), 3:str(id)}[len(str(id))]

        times = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

        os.rename(path + x, path + filename + '.jpg') 
        #重命名文件 www.iplaypy.com

        print "INSERT INTO `jtbc_superstar` VALUES(%d, '%s', 'common/upload/xphoto/%s.jpg', 
              'common/upload/photo/%s.jpg', '', 0, '%s', '|0|,|8|', 8, 0, 0, 0, 0);
              " % (id, title, filename, filename, times)
