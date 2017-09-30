
#导入方法模块
import os, sys
from stat import *
import Image

PicPathNameList = []
PicWidthList = []
PicHeightList = []

def WalkTree(top, callback):

    for f in os.listdir(top):
        
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        
        if S_ISDIR(mode):
            WalkTree(pathname, callback)
        elif S_ISREG(mode):
            callback(pathname)
        else:
            print 'Skipping %s' % pathname

#www.iplaypy.com

def GetPicInfo(file):

    global PicPathNameList
    global PicWidthList
    global PicHeightList

    try:    
        image = Image.open(file)
        PicPathNameList.append(file)      
        PicWidthList.append(image.size[0])
        PicHeightList.append(image.size[1])
    except IOError:
        pass

if __name__ == '__main__':
    WalkTree(top, GetPicInfo)
    print "PicPathNameList Begin"
    print PicPathNameList
    print PicWidthList
    print PicHeightList
    print "PicPathNameList End"