
# -*- coding: utf-8 -*-
__author__ = 'poppy'
'''
dakele bbs sigin
'''
import sys
import urllib2
import urllib
import requests
import cookielib
import json
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG)
reload(sys)
sys.setdefaultencoding("utf8")
class Dakele(object):

    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
    
    def _getHeaders(self):
        headers = {}
        headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        #headers['Host']='www.dakele.com'
        headers['Connection']='keep-alive'
        headers['Cache-Control']='max-age=0'
        headers['Accept-Language']='zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
        #headers['Accept-Encoding']='gzip, deflate, sdch'
        headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        return headers
    
    def login(self):
        '''登录网站'''
        logging.debug(u'正在登陆 username : %s password : %s' %(self.name,self.password))
        logging.debug(u'headers is : %s' % self._getHeaders())
        loginparams = {'product': 'bbs','surl': r'http://bbs.dakele.com/','username': self.name,'password':self.password,'remember':'0'}
        logging.debug(u'loginparams is : %s' % loginparams)
        req = urllib2.Request( r'http://passport.dakele.com/logon.do', urllib.urlencode(loginparams), headers=self._getHeaders())
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        result = json.loads(thePage)
        return result['redirect']

    def login_bbs(self,url):
        '''登录bbs网站'''
        logging.debug( 'start bbs login : %s ' % url)
        req = urllib2.Request(url,headers=self._getHeaders())
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        #print  thePage
    def _say(self,html):
        soup = BeautifulSoup(html)
        try:
            qd_form = soup.find_all(id="qiandao")[0]
            s_action = qd_form['action']
            print 's_action is : %s' %s_action
            inputes = soup.find_all("input")
            s_formhash = ''
            s_qdxq = 'kx'
            s_qdmode = '1'
            for input in inputes:
                if input['name']=='formhash':
                    s_formhash = input['value']
                    break
            
            loginparams = {'formhash':s_formhash,'qdxq':s_qdxq,'qdmode': s_qdmode,'todaysay':u'可乐社区是我家，我们大家都爱Ta...'}
            req = urllib2.Request( r'http://bbs.dakele.com/'+s_action, urllib.urlencode(loginparams), headers=self._getHeaders())
            response = urllib2.urlopen(req)
            self.operate = self.opener.open(req)
            thePage = response.read()
            result_soup = BeautifulSoup(thePage)
            for c in result_soup.find_all("div",class_="c"):
                logging.info(t_text())
        except IndexError:
            logging.info(u'今天已经签到过...')
        #         with open('d:/result.html','w') as fw :
        #             fw.write(thePage)
        #soup_qdform = BeautifulSoup(qd_form.html)
        #print qd_form.action
        #         d = pq(html)
        #         s_action =  d("#qiandao").attr("action")
        #         if s_action:
        #             s_formhash = d("#qiandao input[name=formhash]").attr("value")
        #             s_qdxq = d("#qiandao input[name=qdxq]").attr("value")
        #             s_qdmode = '1'
        #             loginparams = {'formhash':s_formhash,'qdxq':s_qdxq,'qdmode': s_qdmode,'todaysay':u'可乐社区是我家，我们大家都爱Ta...'}
        #             req = urllib2.Request( r'http://bbs.dakele.com/'+s_action, urllib.urlencode(loginparams), headers=self._getHeaders())
        #             response = urllib2.urlopen(req)
        #             self.operate = self.opener.open(req)
        #             thePage = response.read()
        #         else:
        #             logging.deb
2000
ug( u'今天已经签到过...')
            
    def sign(self,url):
        logging.debug( 'start bbs sign : %s' % url)
        req = urllib2.Request(url,headers=self._getHeaders())
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        self._say(thePage)
    
if __name__ == '__main__':
    userlogin = Dakele('XXX','XXX')
    bbs_loginurl = userlogin.login()
    userlogin.login_bbs(bbs_loginurl)
    userlogin.sign('http://bbs.dakele.com/dsu_paulsign-sign.html');
