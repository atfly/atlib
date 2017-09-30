
#! /usr/bin/env python
#-*- coding: utf-8 -*-
 
import os,stat
 
def WalkDir(dir, file_callback=None):
	for root, dirs, files in os.walk(dir):
		for d in dirs:
			#print d
			if(not d[0] == "."):
				file_path = os.path.join(root, d)
				if file_callback: file_callback(file_path)

	for root, dirs, files in os.walk(dir):
		for f in files:
			#print f
			if(not f[0] == "."):
				file_path = os.path.join(root, f)
				if file_callback: file_callback(file_path)

def LogFile(file):
    try:
		fileStats = os.stat(file)
		#print file
		#print fileStats.st_mode
		#print oct(stat.S_IMODE(fileStats.st_mode))
		#print fileStats.st_uid
		#print fileStats.st_gid
		fileInfo = 'chmod ' +  oct(stat.S_IMODE(fileStats.st_mode)) + ' ' + file
		print fileInfo
    except:
        pass
 
if __name__ == "__main__":
    path = raw_input('')
    WalkDir(path, LogFile)

#! /usr/bin/env python
#-*- coding: utf-8 -*-
 
import os,stat
 
def WalkDir(dir, file_callback=None):
	for root, dirs, files in os.walk(dir):
		for d in dirs:
			#print d
			if(not d[0] == "."):
				file_path = os.path.join(root, d)
				if file_callback: file_callback(file_path)

	for root, dirs, files in os.walk(dir):
		for f in files:
			#print f
			if(not f[0] == "."):
				file_path = os.path.join(root, f)
				if file_callback: file_callback(file_path)

def LogFile(file):
    try:
		fileStats = os.stat(file)
		#print file
		#print fileStats.st_mode
		#print oct(stat.S_IMODE(fileStats.st_mode))
		#print fileStats.st_uid
		#print fileStats.st_gid
		fileInfo = 'chown ' +  str(fileStats.st_uid) +':' + str(fileStats.st_gid) + ' ' + file
		print fileInfo
    except:
        pass
 
if __name__ == "__main__":
    path = raw_input('')
    WalkDir(path, LogFile)
