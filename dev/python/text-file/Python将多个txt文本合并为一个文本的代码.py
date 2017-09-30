
#coding=gbk

import os
import sys
import glob

def dirTxtToLargeTxt(dir,outputFileName):
    '''从dir目录下读入所有的TXT文件,将它们写到outputFileName里去'''
    #如果dir不是目录返回错误

    if not os.path.isdir(dir):
        print "传入的参数有错%s不是一个目录" %dir
        return False
    #list all txt files in dir
    outputFile = open(outputFileName,"a")

    for txtFile in glob.glob(os.path.join(dir,"*.txt")):
        print txtFile
        inputFile = open(txtFile,"rb")

        for line in inputFile:
            outputFile.write(line)
    return True

#www.iplaypy.com

if __name__ =="__main__":
    if len(sys.argv) < 3:
        print "Usage:%s dir outputFileName" %sys.argv[0]
        sys.exit()
    dirTxtToLargeTxt(sys.argv[1],sys.argv[2])
    