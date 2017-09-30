

#!/usr/bin/env python
#coding:utf-8

import os
import base64
import sys

def baseurl(argv):
    if len(argv) == 2:
        url = argv[1]
    else:
        print "Input Error!\n usage: %s 'url'"%(argv [0])
        sys.exit(1)

    if url.startswith('thunder://'):
        url = url[10:]+'\n'
        url = base64.decodestring(url)
        url = url[2:-2]
    elif url.startswith('flashget://'):
        url = url[11:url.find('&')]+'\n'
        url = base64.decodestring(url)
        url = url[10:-10]
    elif url.startswith('qqdl://'):
        url = url[7:]+'\n'
        url = base64.decodestring(url)
    else:
        print '\n It is not a available url!!'
    return url

#www.iplaypy.com

def test():
    url = 'thunder://QUFodHRwOi8veDEwMi51dW5pYW8uY29tOjEwMS9kYXRhL2Jicy51dW5pYW8uY29tJUU2JTgyJUEwJUU2JTgyJUEwJUU5JUI4JTlGLyVFNyU5QiU5NyVFNiVBMiVBNiVFNyVBOSVCQSVFOSU5NyVCNC0lRTYlODIlQTAlRTYlODIlQTAlRTklQjglOUYlRTQlQjglQUQlRTYlOTYlODclRTUlQUQlOTclRTUlQjklOTUucm12Ylpa'
    p = baseurl(sys.argv)
    print '\n============请将下面地址复制到你的下载器中=============\n'
    print p

if __name__ == '__main__':
    test()

