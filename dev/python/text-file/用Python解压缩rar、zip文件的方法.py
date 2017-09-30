
import os
import sys

src=sys.argv[1]
dst=sys.argv[2]

format=['rar','zip','7z','ace','arj','bz2','cab','gz','iso','jar','lzh','tar','uue','z']
os.chdir(sys.argv[1])

for file in os.listdir('.'):
if os.path.isfile(file) and (os.path.splitext(file)[1][1:].lower() in format)==True:

#cmd='winrar x -ibck "'+file+'" "'+dst+'\\'+os.path.splitext(file)[0]+'\\"'
cmd='winrar x -ibck "'+file+'" "'+dst+'\\"'

os.system(cmd)

os.remove(file)

print('done '+file) 

#www.iplaypy.com第一个版本的改进

#rardecmp.py
#decompress with winrar
#arguments :filename directory opt
# opt='mkdir' to create directory with the correspond filename
# opt='direct' to decompress rar files in current directory
# opt='mk&del' to mkdir and delete rar file

import os
import sys

if len(sys.argv)!=3:

print ('wrong arguments\n')

print ('rar.py directory opt\n')

print ('opt=\'mkdir\' to create directory with the correspond filename\n')

print ('opt=\'direct\' to decompress rar files in current directory\n')

print ('opt=\'diredel\' to decompress rar files in current directory and delete files\n')

print ('opt=\'mkdel\' to mkdir and delete rar file\n')

exit(0)

#-ibck ,minimized when running
opt=sys.argv[2]
os.chdir(sys.argv[1])

format=['rar','zip','7z','ace','arj','bz2','cab','gz','iso','jar','lzh','tar','uue','z']

for file in os.listdir('.'):
if os.path.isfile(file) and (os.path.splitext(file)[1][1:].lower() in format)==True:
if opt=='mkdir':

cmd='winrar x -ibck "'+file+'"'+' "'+os.path.splitext(file)[0]+'"\\'

os.system(cmd)

elif opt=='direct':
cmd='winrar x -ibck "'+file+'"'

os.system(cmd)

