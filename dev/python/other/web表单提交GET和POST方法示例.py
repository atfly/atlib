
#!/usr/bin/env python
#--coding = UTF-8--

import sys,urllib2,urllib

zipcode = sys.argv[1]


def GET():
    def addGETdata(url,data):
    """
    Adds data to url.Data should be a list or tuple consisting of
    2_item lists or tuples of the form: (key,value).

    Item that have no key should have key set to None.

    A given key may occur more than once.
    """
        return url + '?' + urllib.urlencode(data)
    
    url = addGETdata("你的url地址",[("你要访问的网页"，zipcode)])
    #example:url = addGETdata("http://www.xxxxxx.com/xxx/",(["query",zipcode]))

    print "Using URL",url
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)

    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        sys.stdout.write(data)

#www.iplaypy.com
def POST():
    url = "你的url地址"#example:url = "http://www.xxxxxx.com/xxx/"
    data = urllib2.urlencode([("你要访问的网页",zipcode)])
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req,data)

    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        sys.stdout.write(data)
