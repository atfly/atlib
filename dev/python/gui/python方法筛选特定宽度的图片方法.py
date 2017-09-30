
import sys
import os

sys.path.append('PIL')

from PIL import Image as im

path = '/home/hualun/桌面/img/'

new_path = '/home/hualun/桌面/img2/'

#www.iplaypy.com

for x in os.listdir(path):

    if x.endswith('.jpg'):
        file = im.open(path+x)

        width = file.size[0]

        if width > 300:
            os.rename(path+x, new_path+x)

            print "%s 移动完成.." % x