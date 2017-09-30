
#!/bin/env python
from xmlrpclib import *

#下面是解析osc的xml时，需要特殊处理的地方
#osc的xml类型中,int有这个样子 "ex:i4","ex:i8",唉 。
Unmarshaller.dispatch["ex:i4"] = Unmarshaller.end_int
Unmarshaller.dispatch["ex:i8"] = Unmarshaller.end_int
Unmarshaller.dispatch["ex:nil"] = Unmarshaller.end_nil

#verbose=1 是debug模式
server = ServerProxy("http://my.oschina.net/action/xmlrpc",verbose = 1)

#通过用Wireshark监控 live Writer发出的报文发现 osc 用的是 blogger的 xmlrpc
#试了试 metaWeblog,貌似也可以。
#鄙视 @红薯 没有放出 xmlrpc的api说明
mw_api = server.metaWeblog

#获取blog信息
#mw_api.getPost(postid, self.username, self.password)
res = mw_api.getPost( '118931', 'user','password')
for i in res:
    print i,res[i]

#其他的api还有：
#getRecentPosts(blogid, self.username, self.password, numposts)
#new_post(cblogid, self.username, self.password, content, publish)
#deletePost(self.appkey, postid, self.username, self.password, publish)
#getUsersBlogs(self.appkey, self.username, self.password)
#newMediaObject(blogid, self.username, self.password, new_object)
#其他的请问度娘...
