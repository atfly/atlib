
#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from Baidu import getImageUrlList, search, nextPage, searchResult
from Downloader import downloadFromQueue
from FileHelper import getFilenameFromURL, addExtension, makedir
from Queue import Queue
from thread import start_new_thread
from  Config import Config
from NetworkPrepare import prepare
import os, sys

def baseURL():
  if Config.site == 'baidu':
    return search(Config.keyword, Config.addtional)
  if Config.site == 'jandan':
    return 'http://jandan.net/ooxx'

def main():
  # 开始准备
  prepare()
  while_n = 0 # 循环计数器
  imglist = []
  makedir(Config.directory)
  print 'Generate search url'
  URL = baseURL()
  # 下载 #############
  # 获取搜索结果数量并与_count比较取其较小值
  count = min(searchResult(URL), Config.count)
  # 没有搜索结果时退出
  if not count:
    print "No search result at current condition."
    sys.exit(1)
  # 获得指定数量的url, 存放于list  
  print 'Fetching page',
  while len(imglist) < count:
    print while_n,
    while_n += 1
    tmplist = getImageUrlList(URL)
    imglist = imglist + tmplist
    URL = nextPage(URL, len(tmplist))
  print '' # 换行
  count = len(imglist)
  print "There're %d files to download" % count
  # 将已有文件从imglist中去除
  imglist = [url for url in imglist
             if not getFilenameFromURL(url) in os.listdir(Config.directory)]
  print "There's %d files already downloaded." % (count - len(imglist))
  # 下载该list 
  print 'Fetching list of %d files' % len(imglist)
  queue = Queue()
  for url in imglist:
    queue.put(url)
  failure = []
  for i in range(Config.thre
3b8
ad_count):
    start_new_thread(downloadFromQueue, (
                                         queue, failure, Config.directory, Config.timeout))
  queue.join()
  print "%d failed to fetch." % len(failure)

def clean():
  # 清理
  # 1.添加后缀
  print 'Adding extension ...'
  for fname in os.listdir(Config.directory):
    addExtension(Config.directory + os.sep + fname, '.jpg')
  print 'done.'
  # 2.保存cookie
  Config.cj.save()

if __name__ == "__main__":
  main()
  clean()

#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from Downloader import getStream
from MyParser import MyParser
from String import longestString, cutTo, cutBegin, getCodingContent
from urllib import urlencode
import json
import re

def getImageUrlFromScript(script):
  pattern = re.compile(r'(?<="objURL":").*?(?=")')
  groups = pattern.findall(script)
  new_group = [amatch.strip() for amatch in groups] # 更Pythonic的方式
  return new_group

def getImageUrlList(url):
  imglist = []
  for i in _getJsonList(url):
    imglist.append(i['objURL'].strip())
  return imglist

def _getJsonList(url):
  stream = getStream(url)
  data = getCodingContent(stream)
  pattern = re.compile(r'(?<=var imgdata =).*?(?=;v)')
  block = pattern.findall(data)[0]
  jsonlist = json.loads(block)
  return jsonlist['data'][:-1]

def nextPage(url, pn):
  url_pn = cutBegin(url, '&pn=')
  if not url_pn:
    url_pn = 0
  url_pn = int(url_pn) + pn
  return cutTo(url, '&pn') + '&pn=' + str(url_pn)

def search(keyword, addtionParams={}):
  """Generate a search url by the given keyword.
  params keyword: utf8 string"""
  url = 'http://image.baidu.com/i?'
  parser = MyParser()
  params = _getParams('http://image.baidu.com', parser)
  params.update(addtionParams)
  params.update({'word':keyword.decode('utf8').encode('gbk')})
  return url + urlencode(params)

def searchResult(url):
  parser = MyParser()
  parser.feed(getCodingContent(getStream(url)))
  block = longestString(parser.scriptList)
  parser.close()
  pattern = re.compile('(?<="listNum":)\d*(?=,)')
  count = pattern.findall(block)
  if count:
    count = int(count[0])
    return count
  return 0

def _getParams(url, parser):
  """Get a dict contained the url params"""
  stream = getStream(url)
  data = getCodingContent(stream)
  parser.feed(data)
  return parser.formParams

def _appendParams(adict):
  """Generate a url with params in adict."""
  p = [key + '=' + adict[key] for key in adict]
  return '&'.join(p)

#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from cookielib import LWPCookieJar
class Config:
  keyword = '美女' # 要搜索的关键字 注意不要改变文件编码
  addtional = {'width':'1920', 'height':'1200'} # 宽度和高度 可以为空 {}
  directory = r'image'  # 存放的位置
  count = 30     # 要下载的数量，自动进到20的倍数
  thread_count = 15 # 线程数
  timeout = 20 # 下载超时限制 使用超时20 10好像小了点
  # 代理设置
  proxy = 'http://localhost:7001'
  use_proxy = False
  proxy_user = 'user_name'
  proxy_pass = 'password'
  proxy_auth = False
  cookies = 'cookies.txt'
  use_cookies = True
  cj = LWPCookieJar(cookies)
  site = 'baidu'  #site='jandan'

#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from FileHelper import getFilenameFromURL, writeBinFile
import urllib2

def getStream(url, timeout=10):
  # 返回一个url流或者False
  request = urllib2.Request(url)
  request.add_header('User-Agent', UserAgent.Mozilla)
  try:
    stream = urllib2.urlopen(request, timeout=timeout)
  except (Exception, SystemExit): # catch SystemExit to keep running
    print "URL open error. Probably timed out."
    return False
  return stream

def downloadFromQueue(queue, failure, directory='.', timeout=10):
  """Get files from 
3c48
a list of urls.
  return : list, contained the failure fetch"""
  while not queue.empty():
    url = queue.get()
    stream = getStream(url, timeout=timeout)
    file_name = getFilenameFromURL(url)
    if stream and writeBinFile(stream, file_name, directory):
      queue.task_done()
      print "Fetching", url, 'done.'
      continue
    failure.append(url)
    queue.task_done()
  return failure

class UserAgent:
  Mozilla = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'

#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import re, os
def getFilenameFromURL(url):
  # 在 Downloader 中使用
  pos = url.rfind('/')
  shorted = url[pos + 1:]
  pattern = re.compile(r'\w*[\.\w]*')
  f_name = pattern.findall(shorted)[0]
  return f_name

def addExtension(fname, ext):
  # 在 App 中使用，添加扩展名
  # 没有后缀才添加
  if '.' not in fname:
    rename(fname, ext)
def rename(old, ext):
  # ext='.jpg'
  if os.path.isfile(old + ext):
    ext = '2' + ext
    rename(old, ext)
    return None
  print 'rename', old, old + ext
  os.rename(old, old + ext)

def makedir(directory):
  if not os.path.isdir(directory):
    os.mkdir(directory) # 不捕获_directory是文件时的异常，让程序自己退出

def writeBinFile(stream, file_name, directory='.', mode='wb'):
  """Read from the given url and write to file_name."""
  file_name = directory + os.sep + file_name
  if os.path.isfile(file_name):
    print 'File %s exist.' % file_name
    return False
  CHUNCK_SIZE = 1024
  with open(file_name, mode) as fp:
    while True:
      try:
        chunck = stream.read(CHUNCK_SIZE)
      except (Exception, SystemExit):
        print 'Fetching error. Probably timed out.'
        fp.close()
        os.remove(file_name)
        return False
      if not chunck:break
      fp.write(chunck)
  return True
#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import HTMLParser

class MyParser(HTMLParser.HTMLParser):
  def __init__(self):
    HTMLParser.HTMLParser.__init__(self)
    self.toggle_script_parse = False
    self.toggle_form_parse = False
    self.scriptList = []
    self.formParams = {}
    self.result = 0

  def handle_starttag(self, tag, attrs):
    HTMLParser.HTMLParser.handle_starttag(self, tag, attrs)
    attrs = dict(attrs)
    if tag == 'script':
      self.toggle_script_parse = True
    # parse start parse form to get attrs in input tag
    if tag == 'form' and attrs.has_key('name') and attrs['name'] == 'f1':
      self.toggle_form_parse = True
    if tag == 'input' and self.toggle_form_parse:
      if attrs.has_key('type') and attrs['type'] == 'hidden':
        key = attrs['name'];value = attrs['value']
        self.formParams[key] = value

  def handle_endtag(self, tag):
    HTMLParser.HTMLParser.handle_endtag(self, tag)
    if tag == 'form' and self.toggle_form_parse:
      self.toggle_form_parse = False

  def handle_data(self, data):
    HTMLParser.HTMLParser.handle_data(self, data)
    if self.toggle_script_parse:
      self.scriptList.append(data)
      self.toggle_script_parse = False

  def reset(self):
    HTMLParser.HTMLParser.reset(self)
    self.toggle_script_parse = False
    self.toggle_form_parse = False
    self.scriptList = []
    self.formParams = {}
    self.result = 0

#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import urllib2
from Config import Config

def proxy_handler(proxy, use_proxy, proxy_auth=False, puser='', ppass=''):
  if use_proxy:
    return urllib2.ProxyHandler({"http" : proxy})
  return urllib2.ProxyHandler({})

def cookie_handler(cj):
  try:
    cj.revert(cj)
  except Exception:
    pass
  cj.clear_expired_cookies()
  return urllib2.HTTPCookieProcessor(cj)

def prepare():
  ch = cookie_handler(Config.cj)
  ph = proxy_handler(Config.proxy, Config.use_proxy)
  if Config.proxy_auth:
    pm = urllib2.HTTPPasswordMgrWithDefaultRealm()
    pm.add_password(None, Config.proxy, Config.proxy_user, Config.proxy_pass)
    urllib2.install_opener(urllib2.build_opener(ch, ph, urllib2.ProxyBasicAuthHandler(pm)))
    return
  urllib2.install_opener(urllib2.build_opener(ch, ph))

#!/usr/bin/env python2
# -*- coding:utf-8 -*-
def determinCoding(content, header):
  """Determin a coding of a given url content and it's header.
  params headers : HTMLHeader instance"""
  content_type = header['Content-Type']
  tag = 'charset='
  if content_type:
    if tag in content_type:
      pos = content_type.index(tag)
      pos += 8
      return content_type[pos:]
  content = content.lower()
  if tag in content:
    startpos = content.index(tag)
    endpos = content[startpos:].index('"')
    return content[startpos:endpos][startpos + 8:]

def getCodingContent(stream):
  # 获取stream的编码
  """Return a string in which is the content of given url.
  return - content : unicode string"""
  content = stream.read()
  coding = determinCoding(content, stream.headers)
  stream.close()
  return content.decode(coding)

def longestString(alist):
  """Return the longest string of a list of strings."""
  a_new_list = [len(a_str) for a_str in alist]
  pos = a_new_list.index(max(a_new_list))
  return alist[pos]

def cutTo(str_1, str_2):
  """Cut str_1 to the position just befor str_2."""
  # 不包含 str_2
  if not str_2 in str_1 :
    return str_1
  pos = str_1.index(str_2)
  return str_1[0:pos]

def cutBegin(str_1, str_2):
  # 在MyParser中使用
  if not str_2 in str_1:
    return None
  pos = str_1.index(str_2) + len(str_2)
  return str_1[pos:]
