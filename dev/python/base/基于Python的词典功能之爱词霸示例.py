
# -*- coding: utf-8 -*-

import urllib2
import sys
import traceback
import re
from xml.etree.ElementTree import parse

def lookup(word):

    dict_url="http://dict-co.iciba.com/api/dictionary.php?w=%s"
    url = dict_url % word
    resXML = parse(urllib2.urlopen(url)).getroot()
    p = resXML.find("ps")
    pos = resXML.find("pos")
    d = resXML.find("acceptation")


    if  p == None:
        print "没找到这词"
    else:
        print "音:" ,p.text.encode('utf8')
        print "词性:" ,pos.text.encode('utf8')
        print "含义:" ,d.text.encode('utf8')
        print len(resXML.findall("sent"))
        
        for i,sent in enumerate(resXML.findall("sent")):
            print i,sent[0].text
            print "  " + sent[2].text.encode('utf8')

#www.iplaypy.com

if __name__ == "__main__":
    while(True):
        word = raw_input("\n输入您要查询的单词(88是退出)：")
        if word == "88":
            break
        elif re.search("^([a-zA-Z]*)$",word)==None:
            print "Does not support C to E"
            break
        else:
            try:
                lookup(word)
            except Exception,e:
                print traceback.format_exc()

