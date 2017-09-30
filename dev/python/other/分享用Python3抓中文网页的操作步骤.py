
#! /usr/bin/python3.2

import sys
import urllib.request

req = urllib.request.Request('http://www.baidu.com')

response = urllib.request.urlopen(req)

the_page = response.read()

type = sys.getfilesystemencoding() 
#注意：转换成本地系统编码

print(the_page.decode(type))
#www.iplaypy.com