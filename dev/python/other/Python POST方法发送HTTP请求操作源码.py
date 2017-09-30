
>>> import httplib, urllib  
>>> params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})  
>>> headers = {"Content-type": "application/x-www-form-urlencoded",  
...            "Accept": "text/plain"}  
>>> conn = httplib.HTTPConnection("musi-cal.mojam.com:80")  
>>> conn.request("POST", "/cgi-bin/query", params, headers)  
>>> response = conn.getresponse()  
>>> print response.status, response.reason  
200 OK  
>>> data = response.read()  
>>> conn.close() 
#www.iplaypy.com