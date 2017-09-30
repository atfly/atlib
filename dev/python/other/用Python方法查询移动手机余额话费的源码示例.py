
#!/usr/bin/env python
#encoding=utf-8
 
import Image
import sys
import urllib, urllib2, cookielib
import cmd
import re
import StringIO  

class Mobile(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro= """
        请输入 help 查看帮助 
        """
        self.prompt = "Yidong> "
        self.form = {
            'submitMode':'2',
            'ErrorUrl':'../briefLogon.do',
            'ReturnURL':'www.sd.10086.cn/newecare/common/prior.jsp',
            'FieldID':'1',
            'entrance':'IndexBrief',
            'mobileNum':'',
            'logonMode':'1',
            'servicePWD':'',
            'randCode':'',
            'smsRandomCode':''
        }
        self.formAction = 'http://www.sd.10086.cn//portal/servlet/LoginServlet'
        self.mobilePage = 'http://www.sd.10086.cn/newecare/common/prior.jsp'
        #www.iplaypy.com

        cookie = cookielib.CookieJar()

        cookie.clear()

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

        opener.addheaders = [
            ('User-agent',  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.91 Safari/534.30'),
            ('Referer',  'http://www.sd.10086.cn/portal/briefLogon.do'),
            ('Accept-Language',  'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),
            ('Accept-Encoding',  'gzip, deflate'),
            ('Host',  'www.sd.10086.cn'),
        ]
        urllib2.install_opener(opener)	
        
    def _getCode(self):
        urlImg = 'http://sd.10086.cn/portal/sms/briefValidateCode.jsp'
        imgs = (
            (0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1
23be
,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,),
            (0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,),
            (0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,)
        )
        fp = StringIO.StringIO(urllib2.urlopen(urllib2.Request(urlImg)).read())
        im = Image.open(fp)
        im = im.crop((8,5,52,20)) 
        code=''

        for i in range(4):
            im_new = im.crop((11*i,0,11*(i+1),15))
            width, height = im_new.size
            l = []

            for i in range(width):
                for j in range(height):
                    c1, c2, c3 = im_new.getpixel((i, j))
                    if (c1 < 40) and  (c2 < 40) and (c2 < 40) :
                        l.append(1)
                    else:
                        l.append(0)
            n=0

            for img in imgs:
                same=0

                for i in range(165):
                    if img[i] == l[i]:
                        same += 1
                if same > 150:
                    code += str(n)
                    break
                n += 1
        return code
    
    def do_ye(self, info):
        '''
        查询话费： Yidong>ye 手机号码 服务密码
        Yidong> ye 15153006103 888888
        '''
    
        arg = info.split(' ')
        if len(arg) <> 2:
            print 'error 89!'
            return 0
            
        print 'waiting ... ',
        sys.stdout.flush()
        
        self.form['mobileNum']  = arg[0]
        self.form['servicePWD'] = arg[1]
        self.form['randCode']   = self._getCode()
        req = urllib2.Request(self.formAction, urllib.urlencode(self.form))
        doc = urllib2.urlopen(req).read()
        reU = re.compile('(www.sd.10086.cn/newecare/common/prior.jsp;ssojsessionid=\S+)"', re.S)
        result = reU.findall(doc)
        try:
            doc = urllib2.urlopen(urllib2.Request('http://'+result[0])).read()
            doc = urllib2.urlopen(urllib2.Request('http://www.sd.10086.cn/portal/servlet/CookieServlet?FieldID=2')).read()
        except:
            print 'error: 98!'
            return 0
        reA = re.compile("'(\S+)'", re.S)
        result = reA.findall(doc)
        url = 'http://www.sd.10086.cn/newecare/loginAttritd.do?Attritd=%s&randnum=6010.6788671377135&menuID=null' % (result[0])
        urllib2.urlopen(urllib2.Request(url))
       
        doc = urllib2.urlopen(urllib2.Request('http://www.sd.10086.cn/newecare/loginSuccess.jsp')).read()
        reYE = re.compile("您的余额：(\S+)元", re.S)
        result = reYE.findall(doc)
        try:
            print result[0]+"元"
        except:
            print 'error: 109!'
        
def main():
    mobile = Mobile()
    try:
        mobile.cmdloop()
    except KeyboardInterrupt:
        print "bye"
    
if __name__ == "__main__":
    main()
