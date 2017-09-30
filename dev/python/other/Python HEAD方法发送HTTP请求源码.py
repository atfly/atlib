
>>> import httplib  
>>> conn = httplib.HTTPConnection("www.python.org")  
>>> conn.request("HEAD","/index.html")  
>>> res = conn.getresponse()  
>>> print res.status, res.reason  
200 OK  
>>> data = res.read()  
>>> print len(data)  
0 
>>> data == ''  
True 
#www.iplaypy.com