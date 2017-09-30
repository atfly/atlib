
#!/usr/bin/env python
# -*- coding: gbk -*-
#www.iplaypy.com

import sys,re
import urllib,urllib2
from time import localtime,strftime

def http_send(u,url,employee='',order_id='',query=1):
    opener = urllib2.build_opener()
    if query == 1:
        postdata = urllib.urlencode({"u":u})
    else:
        postdata = urllib.urlencode({"u":u,"employee":employee,"order_id":order_id,"audit":1,"reason":""})

    request = urllib2.Request(url,postdata)

    body = opener.open(request).read()

    opener.close()
    
    return body

def gettime():
    date = strftime("%Y-%m-%d %H:%M:%S", localtime())

    return date
    
def main(argv=None):
    auditor = "username"

    url = "http://192.168.14.27/cgi-bin/cgi_audit_login"

    #url = "http://mage.xunlei.com/ret.html"

    patt = 'javascript:operation\((.*?)\)'

    ret = http_send(auditor,url)

    match = re.search(patt,ret,re.S|re.M)

    if match:

        data = match.group(1)

    else:
            print '%s:no data to audit!' % gettime()
            sys.exit()

    print data

    arrays = data.split(',')

    employee = arrays[1]

    employee = employee.replace("'","").strip()

    #print employee

    order_id = arrays[2]

    order_id = order_id.replace("'","").strip()

    #print order_id

    url2 = "http://192.168.14.27/cgi-bin/cgi_audit"

    result = http_send(auditor,url2,employee,order_id,0)

    print gettime()

    print result

    
if __name__ == "__main__":
    sys.exit(main())
