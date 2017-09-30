
# 导入两个最基础的Python模块 www.iplaypy.com
import urllib.request
import re

# 拿到百度首页的内容
content = urllib.request.urlopen("http://www.baidu.com")
x = str(content.info())
match = re.search('charset=(?P<fuck>\\w*)', x, re.IGNORECASE)

if match:
    temp = x.decode(match.group('fuck'))