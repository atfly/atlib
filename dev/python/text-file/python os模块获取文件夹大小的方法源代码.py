
import os
from os.path import join, getsize

def getdirsize(dir):
   size = 0L
   for root, dirs, files in os.walk(dir):
      size += sum([getsize(join(root, name)) for name in files])
   return size

#www.iplaypy.com

if '__name__' == '__main__':
   filesize = getdirsize(r'c:\windows')
   print 'There are %.3f' % (size/1024/1024), 'Mbytes in c:\\windows'
