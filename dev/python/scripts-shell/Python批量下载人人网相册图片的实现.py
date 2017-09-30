
# coding utf-8

import sys
import os
import re
import urllib
import urllib2
import cookielib
import cmd
import json
import getpass

# import simplejson as json   # < 2.6

class RRAD():
    def __init__(self):
        # initialize the download dir.
        self.download_dir = 'albums'
        if not os.path.isdir(self.download_dir):
            os.mkdir(self.download_dir)

        # build the session
        self.session = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        
    # sign into renren.com
    def signin(self):
        username = raw_input('username: ')
        password = getpass.getpass('password: ')
        data = (
            ('email', username),
            ('password',password),
            ('origURL',"http://www.renren.com/Home.do"),
            ('domain',"renren.com"))
        page = self.session.open('http://www.renren.com/PLogin.do', urllib.urlencode(data))
        page.close()

    def signout(self):
        self.session.open('http://www.renren.com/Logout.do')

#www.iplaypy.com

    # fetch source code by post
    def do_post(self, url):
        return self.session.open(url, {}).read()

    # fetch source code by get
    def do_get(self, url):
        return self.session.open(url).read()

    # get the album's photo links
    def get_album_info(self, album_url):
        photo_links = [] # photo links in all pages
        album_name = album_url.split('/')[-1]
        # fetching links page by page
        content = self.do_get(album_url)
        links = re.findall(r'<a.*href="(.*)" class="picture">', content)
        if links:
            photo_links.extend([re.sub(r'\?.*$', '', link) for link in links])
        return { 'album_name': album_name, 'photos': photo_links }
    
    def get_photo_file(self, photo_url):
        content = self.do_get(photo_url + '/large?xtype=album')
        open('c:/c.txt', 'w').write(content)
        match = re.search(r'<div id="large-con"(.*?)src="(?P<src>.*?)" class="photo"', content, 
                flags=re.MULTILINE|re.DOTALL|re.IGNORECASE)
        return match and match.group('src')

    # download the photo into the given album directory 
    def save_photo_file(self, album_dir, photo_file):
        try:
            
2000
filename = photo_file.split('/')[-1]
            f = open(os.path.join(album_dir, filename), 'wb')
            f.write(self.session.open(photo_file).read())
            f.close()
            return True
        except Exception, e:
            return False
    
    # download the album
    def save_album(self, url):
        album_url = re.sub(r'[\?\#].*$', '', url)
        
        album_info = self.get_album_info(album_url)

        # create the album directory if not exists
        album_dir = os.path.join(self.download_dir, album_info['album_name'])
        if not os.path.isdir(album_dir): os.mkdir(album_dir)
        
        # download each photo into the album directory
        print 'saving album to', album_dir
        for i, link in enumerate(album_info['photos']):
            print '(%d/%d) %s' % (i + 1, len(album_info['photos']), link), 
            try:
                photo_file = self.get_photo_file(link)
                self.save_photo_file(album_dir, photo_file)
                print 'saved.' 
            except:
                print 'failed.'
        print 'all downloads completed.'

class RRADCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = '''


Renren Album Downloader V0.1
=========================================
'''
        self.prompt = '> '
        self.rrad = RRAD()
        
    def help_signin(self):
        print '''Sign into renren.com
        signin username password'''

    def do_signin(self, null):
        self.rrad.signin()

    def help_save(self):
        print '''Save the given album.

        Example:
            save http://photo.renren.com/photo/253423487/album-396516481'''
    def do_save(self, album_url):
        self.rrad.save_album(album_url)

    def help_exit(self):
        print 'Quit the application.'

    def do_exit(self, null):
        sys.exit(0)
    
if __name__ == '__main__':
    rrad_cmd = RRADCmd()
    rrad_cmd.cmdloop()
