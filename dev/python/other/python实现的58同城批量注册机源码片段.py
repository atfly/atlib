
#coding=utf-8
import urllib2 as request,urllib as parse,cookielib,random
import os,random,re,time
import json.encoder as json_encode,json.decoder as json_decode
class Api_connect:
        #API CONNECT QQ SOCKET
    __headers = {
        'User-Agent':'Mozilla/6.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.9 Safari/534.30',\
        'Referer':'http://www.58.com'\
    }
    __data = {
        'cookiepath':'cookie.txt'
    } #登陆以后存放数据
    __http = {} #http进程信息
    __version__ = '1.0'
    def __init__(self,proxy={}):
        self.__proxy = proxy
        self.__httpproess()
    def __httpproess(self):
        #初始化模拟进程
        proxy_support = request.ProxyHandler(self.__proxy)
        self.__http['cj'] = cookielib.MozillaCookieJar(self.__data['cookiepath'])
        self.__http['opener'] = request.build_opener(proxy_support,request.HTTPCookieProcessor(self.__http['cj']))
        pass
    def urlopen(self,url,method='GET',data={},savecookie=False):
        try:
            if (method).upper() == 'POST':
                data = parse.urlencode(data).encode('utf-8')
                self.__http['req'] = request.Request(url,data,self.__headers)
            else:
                self.__http['req'] = request.Request(url=url,headers=self.__headers)
            fp = self.__http['opener'].open(fullurl=self.__http['req'],timeout=5)
            t= fp.read()
            try:
                str = t.decode('utf-8')
            except UnicodeDecodeError:
                str = t
            if savecookie == True:
                self.__http['cj'].save(ignore_discard=True,ignore_expires=True)
            fp.close()
            return str
        except Exception as e:
            return '{}'
    def getForm(self,str):
        if str.find(u'58同城') != -1:
            r = str.index('<form')
            o = str.index('</form>')
            return str[r:o]
        return None
    def getFormValue(self,name,str):
        str2 = re.findall(r'\<input.+name\=\"'+ name +'\".+value=\".+\"\/\>',str)
        findstr = 'value="'
        u1 = str2[0].find(findstr)
        u2 = str2[0].find('"/>')
        return str2[0][u1+len(findstr):u2]
        pass
    def __del__(self):
        pass

class reg(object):
    reg = {'reg_page':'http://passport.58.com/reg/','post_page':'http://passport.58.com/save/','check_page':'http://passport.58.com/regok?regok=1'}
    proxy ={}
    def __init__(self):
        self.regfile = file('reg.txt','wb')
    def setproxy(self,list):
        fp = open(list,'rb')
        self.proxy = fp.readlines()
        self.proxy = [i.rstrip() for i in self.proxy]
        fp.close()
    def getproxy(self):
        return {"http":"http://"+self.proxy[random.randint(0,len(self.proxy)-1)]}
    def setinfo(self,info = []):
        self.info = info
        pass
    def setfile(self,file):
        fp = open(file,'rb')
        self.info = fp.readlines()
        fp.close()
    def reg_load(self,username,password,email):
        if len(self.proxy) != 0:
            ip = self.getproxy()
        else:
            ip ={}
        self.t = Api_connect(ip)
        str = self.t.urlopen(url=self.reg['reg_page'],savecookie=True)
        if str == '{}':
            print u'代理ip错误',ip
            ip = self.getproxy()
            self.t = Api_connect(ip)
            str = self.t.urlopen(url=self.reg['reg_page'],savecookie=True)
        form = self.t.getForm(str)
        if form == None:
            print u'表单错误，太频繁胃'
            return
        postdata = {'nickName':'%s'%username,'txtemail':'%s'%email,'password':'%s'%password,'cpassword':'%s'%password,'cd':self.t.getFormValue('cd',form),'ptk':self.t.getFormValue('ptk',form)}
        self.t.urlopen(url=self.reg['post_page'],method='POST',data=postdata,savecookie=True)
        str = self.t.urlopen(url=self.reg['check_page'],savecookie=True)
        info="用户名：{0},密码：{1},邮箱：{2}".format(username,password,email)
        uinfo = u"用户名：{0},密码：{1},邮箱：{2}".format(username,password,email)
        if str.find(u'注册成功') != -1:
            print >> self.regfile,info
            print uinfo,u',注册成功!'
        else:
            print uinfo,u',注册失败!'
        del self.t
    def reg_start(self):
        for i in self.info:
            self.reg_load(*i.rstrip().sp
2000
lit(" "))

#www.iplaypy.com
            
if __name__ == "__main__":
    reg =reg()
    reg.setfile('user.txt')
    reg.setproxy('Proxies.txt')
    reg.reg_start()