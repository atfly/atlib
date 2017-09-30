
#!/usr/bin/python
#coding=utf-8

import urllib
import sys
#import xml.dom.minidom
import re

#是否输出例句
eg=True

def main():
    if len(sys.argv) == 2:
        word = sys.argv[1]
        xmls = urllib.urlopen('http://dict.cn/ws.php?utf8=true&q=' + urllib.quote(word)).read()
        print re.search(r'<def>(?P<test>.*?)</def>', xmls, re.M|re.I|re.S|re.U).group('test')

        if eg:#www.iplaypy.com
            print
            origs=re.findall(r'<orig>(?P<orig>.*?)</orig>', xmls, re.M|re.I|re.S|re.U)
            trans=re.findall(r'<trans>(?P<trans>.*?)</trans>', xmls, re.M|re.I|re.S|re.U)

            for i in range(len(origs)):
                print "%d. %s"%(i+1,origs[i])
                print "%s  %s"%(' '*((i+1)/10+1),trans[i])
    else:
        help()

def help():
    print 'usage:dict.py [word]'

if __name__ == '__main__':
    main()

