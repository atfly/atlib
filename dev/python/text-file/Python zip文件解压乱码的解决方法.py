
#!/usr/bin/python

#coding=utf8

import zipfile
import sys

if len(sys.argv)<2:  #www.iplaypy.com
    print u'punzip zipfilename'

else:
    f=zipfile.ZipFile(sys.argv[1])
    nlist=f.namelist()

    for n in nlist:
        m=unicode(n,'gb2312').encode('utf8')
        file(m,'wb').write(f.read(n))

    f.close()

