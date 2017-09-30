
#-*- coding:UTF-8 -*-
import urllib,urllib2,cookielib
import xml.etree.ElementTree as etree #xml解析类

class Login163:
   #伪装browser
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    username = ''
    passwd = ''
    cookie = None #cookie对象
    cookiefile = './cookies.dat' #cookie临时存放地
    user = ''
    
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
        #cookie设置
        self.cookie = cookielib.LWPCookieJar() #自定义cookie存放
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)

   #登陆    
    def login(self):       

        #请求参数设置
        postdata = {
            'username':self.username,
            'password':self.passwd,
            'type':1
            }
        postdata = urllib.urlencode(postdata)

        #发起请求
        req = urllib2.Request(
                url='http://reg.163.com/logins.jsp?type=1&product=mail163&url=http://entry.mail.163.com/coremail/fcg/ntesdoor2?lightweight%3D1%26verifycookie%3D1%26language%3D-1%26style%3D1',
                data= postdata,#请求数据
                headers = self.header #请求头
            )

        result = urllib2.urlopen(req).read()
        result = str(result)
        #print result
        self.user = self.username.split('@')[0]

        self.cookie.save(self.cookiefile)#保存cookie
        
        if '登录成功，正在跳转...' in result:
            #print("%s 你已成功登陆163邮箱。---------n" %(user))
            flag = True
        else:
            flag = '%s 登陆163邮箱失败。'%(self.user)
           
        return flag

   #获取通讯录
    def address_list(self):

        #获取认证sid
        auth = urllib2.Request(
                url='http://entry.mail.163.com/coremail/fcg/ntesdoor2?username='+self.user+'&lightweight=1&verifycookie=1&language=-1&style=1',
                headers = self.header
            )
        auth = urllib2.urlopen(auth).read()

        #authstr=str(auth)
        #print authstr
        
        for i,sid in enumerate(self.cookie):
            sid = str(sid)
            #print 'sid:%s' %sid
            if 'sid' in sid:
                sid = sid.split()[1].split('=')[1]
                break
        self.cookie.save(self.cookiefile)
        
        #请求地址
        url = 'http://twebmail.mail.163.com/js4/s?sid='+sid+'&func=global:sequential&showAd=false&userType=browser&uid='+self.username
        #参数设定(var 变量是必需要的,不然就只能看到:<code>S_OK</code><messages>这类信息)
        #这里参数也是在firebug下查看的。
        postdata = {
            'func':'global:sequential',
            'showAd':'false',
            'sid':'qACVwiwOfuumHPdcYqOOUTAjEXNbBeAr',
            'uid':self.username,
            'userType':'browser',
            'var':'<!--?xml version="1.0"?--><object><array name="items"><object><string name="func">pab:searchContacts</string><object name="var"><array name="order"><object><string name="field">FN</string><boolean name="desc">false</boolean><boolean name="ignoreCase">true</boolean></object></array></object></object><object><string name="func">pab:getAllGroups</string></object></array></object>'
            }
        postdata = urllib.urlencode(postdata)
        
        #组装请求
        req = urllib2.Request(
            url = url,
            data = postdata,
            headers = self.header
            )
        res = urllib2.urlopen(req).read()

        #print str(res)
        
        #解析XML，转换成json
        #说明：由于这样请求后163给出的是xml格式的数据，
        #为了返回的数据能方便使用最好是转为JSON
        json = []
        tree = etree.fromstring(res)

        
        
        obj
4000
 = None
        for child in tree:
            if child.tag == 'array':
                obj = child            
                break
        #这里多参考一下，etree元素的方法属性等，包括attrib,text,tag,getchildren()等
        obj = obj[0].getchildren().pop()
        for child in obj:
            for x in child:
                attr = x.attrib
                if attr['name']== 'EMAIL;PREF':
                    value = {'email':x.text}
                    json.append(value)
        return json
#获取收件箱www.iplaypy.com
    def minbox(self):
        #获取认证sid
        auth = urllib2.Request(
                url='http://entry.mail.163.com/coremail/fcg/ntesdoor2?username='+self.user+'&lightweight=1&verifycookie=1&language=-1&style=1',
                headers = self.header
            )
        auth = urllib2.urlopen(auth).read()

        #authstr=str(auth)
        #print authstr
        
        for i,sid in enumerate(self.cookie):
            sid = str(sid)
            #print 'sid:%s' %sid
            if 'sid' in sid:
                sid = sid.split()[1].split('=')[1]
                break
        self.cookie.save(self.cookiefile)
        
        
        url = 'http://twebmail.mail.163.com/js4/s?sid='+sid+'&func=mbox:listMessages&showAd=false&userType=browser&uid='+self.username
        
        postdata = {
            'func':'global:sequential',
            'showAd':'false',
            'sid':'qACVwiwOfuumHPdcYqOOUTAjEXNbBeAr',
            'uid':self.username,
            'userType':'browser',
            'var':'<!--?xml version="1.0"?--><object><int name="fid">1</int><string name="order">date</string><boolean name="desc">true</boolean><boolean name="topFirst">false</boolean><int name="start">0</int><int name="limit">20</int></object>'
            }
        postdata = urllib.urlencode(postdata)
        
        #组装请求
        req = urllib2.Request(
            url = url,
            data = postdata,
            headers = self.header
            )
        res = urllib2.urlopen(req).read()

        liststr=str(res).split('<object>')#用object进行分割
        inboxlistcount=len(liststr)-1#记录邮件封数
        inboxlistfile=open('inboxlistfile.txt','w')
        t=0  #记录当前第几封信
        for i in liststr:
            if 'xml' in i and ' version=' in i:
                inboxlistfile.write('inbox 共'+str(inboxlistcount)+'信')
                inboxlistfile.write('\n')
            if 'name="id"' in i:
                t=t+1
                inboxlistfile.write('第'+str(t)+'封：')
                inboxlistfile.write('\n')
                #写入from
                beginnum=i.find('name="from"')
                endnum=i.find('</string>',beginnum)
                inboxlistfile.write('From:'+i[beginnum+12:endnum])
                inboxlistfile.write('\n')
                #写入to
                beginnum=i.find('name="to"')
                endnum=i.find('</string>',beginnum)
                inboxlistfile.write('TO:'+i[beginnum+10:endnum])
                inboxlistfile.write('\n')
                #写入subject
                beginnum=i.find('name="subject"')
                endnum=i.find('</string>',beginnum)
                inboxlistfile.write('Subject:'+i[beginnum+15:endnum])
                inboxlistfile.write('\n')
                #写入date：
                beginnum=i.find('name="sentDate"')
                endnum=i.find('</date>',beginnum)
                inboxlistfile.write('Date:'+i[beginnum+16:endnum])
                inboxlistfile.write('\n')
                if 'name="read">true' in i:
                    inboxlistfile.write('邮件状态:已读')
                    inboxlistfile.write('\n')
                else:
                    inboxlistfile.write('邮件状态:未读')
                    inboxlistfile.write('\n')
                #写用邮件尺寸
                beginnum=i.find('name="size"')
                endnum=i.find('</int>',beginnum)
                inboxlistfile.write('邮件尺寸:'+i[beginnum+12:endnum])
                inboxlistfile.write('\n')
                #写入邮件编号，用于下载邮件
                beginnum=i.find('name="id"')
                endnum=i.find('</string>',beginnum)
                inboxlistfile.write('邮件编号:'+i[beginnum+10:endnum])
                inboxlistfile.write('\n\n')
                
        inboxlistfile.close()
                
        
        
if __name__=='__main__':
    print("XXX")
    login = Login163('XXXX@163.com','AAAAA')
    flag = login.login()
    if type(flag) is bool:
    
    #login.letterdown()
        print("登陆成功，正在下载列表和通讯录………………")
        login.minbox()
        res = login.address_list()
        addfile=open('addfile.txt','w')
        for x in res:
            addfile.write(x['email'])
        addfile.close()
        print("已完成")
    else:
        print(flag)