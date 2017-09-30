
import os,time,sys,re,threading
import urllib

DOWNLOAD_BASEDIR = os.path.join(os.path.dirname(__file__), 'download')

DOWNLOAD_BASEURL = './download/'

os.mkdir(DOWNLOAD_BASEDIR)

def md5sum(s):
    try:
        import hashlib
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()
    except:
        import md5
        m = md5.new()
        m.update(s)
        return m.hexdigest()
    
class Download(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
##      print "downloading %s " % self.url
        f = urllib.urlopen(self.url)
        content_type,extention = f.headers.get('content-type','image/jpeg').split('/')
        if extention in ('jpeg','html'):
            extention = 'jpg'
        basename = "%s.%s" %( md5sum(self.url) , extention)
        self.filename = os.path.join(DOWNLOAD_BASEDIR, basename)
        self.local_url = DOWNLOAD_BASEURL + basename
        file(self.filename, 'wb').write(f.read())

content = file(os.path.join(os.path.dirname(__file__), 'content.html')).read()

pt=re.compile(r"""src=['"]?(http://.*?)[ '"]""")

urls = []

for url in pt.findall(content):
    urls.append(url)
print time.ctime()

#www.iplaypy.com

thread_pools = []

for url in urls:
    current = Download(url)
    thread_pools.append(current)
    current.start()

result_text = content    

for result in thread_pools:
    print "%s threads running" % threading.activeCount() 
    result.join(5)
    if not result.isAlive():
##        print "url %s saved to %s" % (result.url, result.filename)
        result_text = result_text.replace(result.url, result.local_url)

file(os.path.join(os.path.dirname(__file__), 'result.html'), 'wb').write(result_text)
print "%s threads running" % threading.activeCount()

if threading.activeCount():
    print "Can not stop"
print time.ctime()

