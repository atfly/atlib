
#-*- encoding=utf-8 -*-
import io   
import sys   
import hashlib   
import string   
import os

def calMd5(afile):   
   m = hashlib.md5()   
   file = io.FileIO(afile,'r')   
   bytes = file.read(1024)   
   while(bytes != b''):   
      m.update(bytes)   
      bytes = file.read(1024)    
   file.close()    
   md5value = m.hexdigest()   
   return  md5value
   
def visitor(args, directoryName,filesInDirectory):     # called for each dir 
   print "\t"*(args-1),directoryName
   for fname in filesInDirectory:                   
      fpath = os.path.join(directoryName, fname)    
      if not os.path.isdir(fpath):                   
         print "\t"*args,fname,"\t",calMd5(fpath)

def calDirMd5(startdir, level):
   os.path.walk(startdir, visitor, level+1)
    
if __name__ == '__main__':
   root=raw_input("type root directory:")
   calDirMd5(root,0)
