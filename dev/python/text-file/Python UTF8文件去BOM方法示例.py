
#!/usr/bin/python
#coding=utf-8

import os
import sys
import codecs

class RemoveBom:  

    basePath = ''
    fileList = []
    trimExtList = []
    
    def showMessages(self):
	print 'the Path is [',self.basePath,']'
	n = ''
	for ext in self.trimExtList:
	    n+=ext
	    n+=' '
	print 'the Exts is [' ,n,']'

    def trimFile(self,name):
	file = open(name,'rb')
	content = file.read(3)
	if content != '\xEF\xBB\xBF':
	    return False
	content = file.read()
	file.close()
	file = open(name,'wb')
	file.write(content)
	file.close
	print 'convert ',name,' finish'
	return True

    def getFileList(self,path):
	if not path:
	    return False
	for root,dirs,files in os.walk(path):
	    for filename in files:
		if filename.split('.')[-1] in self.trimExtList:
			filepath=os.path.join(root,filename)
			self.trimFile(filepath)
			#print filepath

    def run(self,argv):
	self.basePath = os.path.normpath(argv[1])
        if len(argv) < 3:
            self.trimExtList.append('java')
        else:
	    for i in range(len(argv)-2):
                self.trimExtList.append(argv[2+i])
	self.showMessages()
	self.getFileList(argv[1])

#www.iplaypy.com
if __name__ == '__main__':
	if len(sys.argv) < 2:
            print 'USEAGE:python %s dirName [ext eg:java php cpp]' % __file__
            sys.exit(0)
	
	tObj = RemoveBom()
	tObj.run(sys.argv)
