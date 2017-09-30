
#!/usr/bin/env python
#coding=utf-8

from BeautifulSoup import BeautifulSoup

import os,urllib,urllib2,pdb
import cookielib
import httplib
import csv,re

GDATA_URL = '/accounts/ClientLogin'

class MailContactError(Exception):
    pass

class MailContact:
    def __init__(self,username,password):
        pass
    def login(self):
        pass
    def get_contacts(self):
        pass
    def get_contact_page(self):
        pass
   
class GMailContact(MailContact):
    """
    A class to retrieve a users contacts from their Google Account.
   
    Dependencies:
    -------------
    * BeautifulSoup.
    * That's it. :-)

    Usage:
    ------
    >>> g = GMailContact('email@example.org', 'password')
    >>> g.login()
    (200, 'OK')
    >>> g.get_contacts()
    >>> g.contacts
    [(u'Persons Name', 'name@person.com'), ...]


    """
    def __init__(self, username='test@gmail.com', password='test', service='cp'):
        self.mail_type="@gmail.com"
        self.username = username + self.mail_type
        self.password = password
        self.account_type = 'HOSTED_OR_GOOGLE'  # Allow both Google Domain and Gmail accounts
        self.service = service                  # Defaults to cp (contacts)
        self.source = 'google-data-import'      # Our application name
        self.code = ''                          # Empty by default, populated by self.login()
        self.contacts = []                      # Empty list by default, populated by self.get_contacts()
   
    def login(self):
        """
        Login to Google. No arguments.
        """
        data = urllib.urlencode({
            'accountType': self.account_type,
            'Email': self.username,
            'Passwd': self.password,
            'service': self.service,
            'source': self.source
        })
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain'
        }
       
        conn = httplib.HTTPSConnection('google.com')
        conn.request('POST', GDATA_URL, data, headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise GdataError("Couldn't log in. HTTP Code: %s, %s" % (response.status, response.reason))
           
        d = response.read()
       
        self.code = d.split("\n")[2].replace('Auth=', '')
        conn.close()
        return response.status, response.reason
   
    def _request(self, max_results=200):
        """
        Base function for requesting the contacts. We'll allow other methods eventually
        """
        url = '/m8/feeds/contacts/%s/base/?max-results=%d' % (self.username, max_results)
       
        headers = {'Authorization': 'GoogleLogin auth=%s' % self.code}
       
        conn = httplib.HTTPConnection('www.google.com')
        conn.request('GET', url, headers=headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't log in. HTTP Code: %s, %s" % (response.status, response.reason))
       
        page = response.read()
        conn.close()
        return page
   
    def get_contacts(self, max_results=200):
        """ Parses the contacts (using BeautifulSoup) from self._request, and then populates self.contacts
        """
        soup = BeautifulSoup(self._request(max_results))
        self.contacts = []
        for entry in soup.findAll('title'):
            if len(entry.parent.findAll(['gd:email', 'title'])) == 2:
                s = entry.parent.findAll(['gd:email', 'title'])
                self.contacts.append((s[0].string, s[1].get('address')))
       
        return

class M126Contact(MailContact):
    def __init__(self,username,password):
        self.mail_type="@126.com"
        self.username = username
        self.password = password       
        self.login_host = 'entry.mail.126.com'
        self.login_url = '/cgi/login?redirTempName=https.htm&hid=10010102&lightweight=1&verifycookie=1&language=0&style=-1'
        self.login_data = urllib.urlencode({
            'domain':'126.com',
            'language':0,
            'bCookie':'',
            'user':self.username,
            'pass':self.password,
            'style':-1,
            'remUser':'',
            'secure':'',
            'enter.x':'%B5%C7+%C2%BC'
        })
        self.login_headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/xml,text/plain',
            'Refer':'http://www.126.com/'
     
1c42
   }
        self.contact_host = 'g2a10.mail.126.com'
        self.contact_url = '/coremail/fcg/ldvcapp?funcid=prtsearchres&sid=%(sid)s&listnum=200&tempname=address%%2faddress.htm'
       

    def login(self):
        conn = httplib.HTTPSConnection(self.login_host)
        conn.request('POST', self.login_url,self.login_data,self.login_headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't log in. HTTP Code: %s, %s" % (response.status, response.reason))
        #sc="Coremail=aaYgsaQsvSmKa%MBgzxnddkKzjPJUTbMddRUIgVwfeiBUd; path=/; domain=.126.com"
        #sid="MBgzxnddkKzjPJUTbMddRUIgVwfeiBUd"
        sc = response.getheader('Set-Cookie')
        if not sc or sc.find("Coremail") == -1:
            #用户密码不正确
            raise MailContactError("Email user %s%s password %s not correct!" % (self.username,self.mail_type,self.password))
        cookie=sc.split()[0]
        coremail = cookie[cookie.find('=')+1:cookie.find(';')]
        sid = coremail[coremail.find('%')+1:]
        self.contact_url = self.contact_url % {'sid':sid}
        self.contact_headers={
        'Cookie':'MAIL126_SSN=%(user)s; NETEASE_SSN=%(user)s; nts_mail_user=%(user)s; logType=df; ntes_mail_firstpage=normal; \
        Coremail=%(coremail)s;mail_host=g2a14.mail.126.com; mail_sid=%(sid)s; mail_uid=%(user)s@126.com; \
        mail_style=dm3; oulink_h=520; ntes_mail_noremember=true' % {'user':self.username,'coremail':coremail,'sid':sid}
        }
        conn.close()

#www.iplaypy.com       
    def get_contact_page(self):
        conn = httplib.HTTPConnection(self.contact_host)
        conn.request('GET',self.contact_url,headers=self.contact_headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't getc contact page. HTTP Code: %s, %s" % (response.status, response.reason))
        page = response.read()
        conn.close()
        return page
       
    def get_contacts(self):
        page = self.get_contact_page()
        self.contacts = []
        soup = BeautifulSoup(page)
        xmps = soup.findAll('xmp')
        for x in xmps:
            if x['id'].startswith('t'):
                self.contacts.append((x.contents[0],x.space.string))

class M163Contact(MailContact):
    def __init__(self,username,password):
        self.mail_type="@163.com"
        self.username = username
        self.password = password     
        self.contacts = [] 
        self.login_host = 'reg.163.com'       
        self.login_url = '/logins.jsp?type=1&url=http://fm163.163.com/coremail/fcg/ntesdoor2?lightweight=1&verifycookie=1&language=-1&style=-1'
       
        self.login_data = urllib.urlencode({
            'verifycookie':1,
            'style':-1,
            'product':'mail163',
            'username':self.username,
            'password':self.password,
            'selType':-1,
            'remUser':'',
            'secure':'on'
        })
        self.login_headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/xml,text/plain',
            'Refer':'http://mail.163.com/'
        }
        self.contact_host = 'g2a10.mail.163.com'
       

    def login(self):
        conn = httplib.HTTPSConnection(self.login_host)
        conn.request('POST', self.login_url,self.login_data,self.login_headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't log in. HTTP Code: %s, %s" % (response.status, response.reason))
       
        sc1 = response.getheader('Set-Cookie')
        '''
            Set-Cookie: NTES_SESS=ohAWkiyj.OCjHdh1BK4ToxPcUvFX2fSLaN3FaU0cRInzLoieELdifjyqnBdk4C8qWIZkirZ7.JF.IPFDuR7BcAtKL; domain=.163.com; path=/
            Set-Cookie: NETEASE_SSN=weafriend; domain=.163.com; path=/; expires=Mon, 08-Jun-2009 10:42:26 GMT
            Set-Cookie: NETEASE_ADV=11&24&1212921746999; domain=.163.com; path=/; expires=Mon, 08-Jun-2009 10:42:26 GMT
        '''
        ntes_sess,ntes_adv = None,None
        for s in sc1.split():
            if s.startswith('NTES_SESS'):
                ntes_sess=s[s.find('=')+1:s.find(';')]
            elif s.startswith('NETEASE_ADV'):
                ntes_adv=s[s.find('=')+1:s.find(';')]
        if not ntes_sess or not ntes_adv:
            #用户密码不正确
            raise MailContactError("Email user %s%s password %s not correct!" % (self.username,self.mail_type,self.password))
       
        url = '/coremail/fcg/ntesdoor2?lightweight=1&verifycookie=1&language=-1&style=-1&username=weafriend'
        headers = {'cookie':sc1}
        conn = httplib.HTTPConnection('fm163.163.com')
        conn.request('GET',url,{},headers)
        response = conn.getresponse()
        sc2 = response.getheader('Set-Cookie')
        coremail = sc2[sc2.find('=')+1:sc2.find(';')]
        sid = coremail[coremail.find('%')+1:]
        self.contact_url = '/coremail/fcg/ldvcapp?funcid=prtsearchres&sid=' + sid +'&listnum=200&tempname=address%2faddress.htm'
       
       
        self.contact_headers = {
        'Cookie':'MAIL163_SSN=%(user)s; vjlast=1212911118; vjuids=-99d7a91f6.1156a6ea3cd.0.9e6d0e6f029e78; \
        _ntes_nuid=7118c6a1c9d16ee59a045a2e66186af8;  NTES_adMenuNum=3; \
        _ntes_nnid=7118c6a1c9d16ee59a045a2e66186af8,0|www|urs|163mail|news|ent|sports|digi|lady|tech|stock|travel|music|2008|;\
        NTES_UFC=9110001100010000000000000000000000100000000000000002331026300000; logType=-1; nts_mail_user=weafriend:-1:1; \
        Province=010; _ntes_nvst=1212911122953,|www|urs|; Coremail=%(coremail)s; \
        wmsvr_domain=g1a109.mail.163.com; ntes_mail_truename=; ntes_mail_province=; ntes_mail_sex=; mail_style=js3; \
        mail_host=g1a109.mail.163.com; mail_sid=%(sid)s; USERTRACK=58.31.69.214.1212911333143304; \
        ntes_mail_firstpage=normal; NTES_SESS=%(ntes_sess)s; \
        NETEASE_SSN=%(user)s; NETEASE_ADV=%(ntes_adv)s' % {'user':self.username,'coremail':coremail,'sid':sid,'ntes_sess':ntes_sess,'ntes_adv':ntes_adv}
        }
        return True
       
       
       
    def get_contact_page(self):
        conn = httplib.HTTPConnection(self.contact_host)
        conn.request('GET',self.contact_url,headers=self.contact_headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't getc contact page. HTTP Code: %s, %s" % (response.status, response.reason))
        page = response.read()
        conn.close()
        return page
       
    def get_contacts(self):
        page = self.get_contact_page()
        soup = BeautifulSoup(page)
        xmps = soup.findAll('xmp')
        for x in xmps:
            if x['id'].startswith('t'):
                self.contacts.append((x.contents[0],x.space.string))




class SohuContact(MailContact):
    def __init__(self,username,password):
        self.mail_type="@sohu.com"
        self.username = username
 
14b6
       self.password = password     
        self.contacts = [] 
        self.login_host = 'passport.sohu.com'       
        self.login_url = 'http://passport.sohu.com/login.jsp'
        self.login_data = urllib.urlencode({
            'loginid':self.username+self.mail_type,
            'passwd':self.password,
            'sg':'5175b065623bb194e85903f5e8c43386',
            'eru':'http://login.mail.sohu.com/login.php',
            'ru':'http://login.mail.sohu.com/login_comm.php',   
            'appid':1000,
            'fl':'1',
            'ct':1126084880,
            'vr':'1|1'       
        })
        self.login_headers = {
            'User-agent':'Opera/9.23',
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/xml,text/plain'           
        }
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        urllib2.install_opener(opener)
        self.contact_host = 'www50.mail.sohu.com'
        self.contact_url = '/webapp/contact'

    def login(self):
        req = urllib2.Request(self.login_url,self.login_data)
        conn = urllib2.urlopen(req)
        self.contact_url = os.path.dirname(conn.geturl())+'/contact'
       
    def get_contacts(self):
        req = urllib2.Request(self.contact_url)
        conn = urllib2.urlopen(req)
        buf = conn.readlines()
        import simplejson
        info = simplejson.loads(buf[0])
        for i in info['listString']:
            self.contacts.append((i['name'],i['email']))

class HotmailContact(MailContact):
    def __init__(self,username,password):
        self.mail_type="@hotmail.com"
        self.username = username
        self.password = password     
        self.contacts = [] 
        self.login_host = 'login.live.com'       
        self.login_url = '/ppsecure/post.srf?id=2'
        self.login_data = urllib.urlencode({
            'login':self.username+self.mail_type,
            'passwd':self.password,
            'PPSX':'Pass',
            'LoginOption':2,
            'PwdPad':'IfYouAreReadingThisYouHaveTooMuchFreeTime'[0:-len(self.password)],
            'PPFT':'B1S2dWnsGTFLpX9h8fxfE*ym5OABStpt0fjo%21YICXQOy1b%21xP4dRx8F1h1w6tR8ZyLP4h3TYGS8gSZGku3j7CxQ4poqr'
        })
        self.login_headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/xml,text/plain',
            'Cookie': 'CkTst=G1213457870062; MobileProf=2AV3mTOwJEE8smIfIyq69wbCn08y6UX7910BtLhqTto2MYrNSBW5hhlEuGlMJdMwwGq1WcxtENCAI1JSyTNfrS23ArFLxDjBNk!xtbIj0iglbu8DQVg9TnSTPtHj975deR; MUID=C2DC0F9324AA47DCB05CE14B989D89C2; ANON=A=E81AEA51F927860B07BBA712FFFFFFFF&E=69f&W=2; s_lastvisit=1213455335875; MH=MSFT; wlidperf=throughput=2087.201125175809&latency=1.422; MSPRequ=lt=1213455763&co=1&id=2; MSPOK=uuid-d75c4c53-1b6e-433c-af95-c3c0175a48cd; CkTst=G1213455761093; MSPPre=fenyon@hotmail.com; MSPCID=0f45e10de2ad38c9; NAP=V=1.7&E=6b4&C=bKkGf4IbC96JLFhsoKyccKm1Kf7jjhX5I3C1ofjvyMoY3iI9j0b6gg&W=2; MSPSoftVis=@:@; BrowserSense=Win=1&Downlevel=0&WinIEOnly=0&Firefox=1&FirefoxVersion=2.0; mktstate=U=&E=en-us; mkt1=norm=en-us; s_cc=true; s_sq=%5B%5BB%5D%5D; MSPP3RD=3688532421',
            'Referer': 'https://login.live.com/ppsecure/post.srf?id=2&bk=1213455763'
        }

        self.contact_host = 'by120w.bay120.mail.live.com'
        self.contact_url = '/mail/GetContacts.aspx'
   
    def getInputValue(self,name,content):
        pass
    def login(self):
        #登录过程见http://blog.jiexoo.com/2008/05/21/%e7%94%a8httpclient%e8%8e%b7%e5%8f%96hotmail%e8%81%94%e7%b3%bb%e4%ba%ba%e5%88%97%e8%a1%a8/
        conn = httplib.HTTPSConnection(self.login_host)
        conn.request('GET','login.srf?id=2')
        response = conn.getresponse()
       
        conn = httplib.HTTPSConnection(self.login_host)
        conn.request('POST', self.login_url,self.login_data,self.login_headers)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't getc contact page. HTTP Code: %s, %s" % (response.status, response.reason))
        page = response.read()
        print page
       
       
    def get_contacts(self):
        conn = httplib.HTTPConnection(self.contact_host)
        conn.request('GET',self.contact_url)
        response = conn.getresponse()
        if not str(response.status) == '200':
            raise MailContactError("Couldn't getc contact page. HTTP Code: %s, %s" % (response.status, response.reason))
        page = response.read()
        conn.close()
        print page

class SinaContact(MailContact):
    pass



class YahooContact(MailContact):
    pass

class MsnContact(MailContact):
    pass

def get_mailcontact(user,password,mailtype):
    if mailtype == "126.com":
        g = M126Contact(user,password)
    elif mailtype == "163.com":
            g = M163Contact(user,password)
    elif mailtype == "sohu.com":
            g = SohuContact(user,password)
    elif mailtype == "hotmail.com":
            g = HotmailContact(user,password)
    elif mailtype == "sina.com":
            g = SinaContact(user,password)   
    elif 
f08
mailtype == "gmail.com":
        g = GMailContact(user,password)
    try:
        g.login()
        g.get_contacts()
        return g.contacts
    except:
        return []
       
       



def get_csvcontact(iter):
    contact,name = [],None
    reader = csv.reader(iter)
    for r in reader:
        for c in r:
            if not c or not len(c.strip()):
                continue
            m=re.search('\w+@\w+(?:\.\w+)+',c)
            if m:
                print name,m.group(0)
                contact.append((name,m.group(0)))
                break
            else:
                name = c
    return contact

def get_imcontact(iter):
    contact = []
    reader = csv.reader(iter)
    for r in reader:
        for c in r:
            m=re.search('\w+@\w+(?:\.\w+)+',c)
            if m:
                print m
                contact.append((m))
    return contact

if __name__=='__main__':
    pdb.set_trace()
    httplib.HTTPSConnection.debuglevel=1
    httplib.HTTPConnection.debuglevel=1   
    g = GMailContact('***', '***')
    g.login()
    g.get_contacts()
    print g.contacts
   
    g = M163ContactContact('***', '***')
    g.login()
    g.get_contacts()
    print g.contacts