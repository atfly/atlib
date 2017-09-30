
# -*- coding: cp936 -*-

import hashlib

src = 'My test string'

myMd5 = hashlib.md5()
myMd5.update(src)   
myMd5_Digest = myMd5.hexdigest()
  
mySha1 = hashlib.sha1()
mySha1.update(src)
mySha1_Digest = mySha1.hexdigest()
  
print 'source string: ', src
print '-------www.iplaypy.com----------------------------'
print 'MD5: ', myMd5_Digest
print 'SHA1: ', mySha1_Digest

