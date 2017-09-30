
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import time
import types
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')


class BaiduMap:
    """
    """
    def __init__(self, keyword):
        self.keyword = keyword
        self.query = [
                ('b', '(-1599062.039999999,811604.75;24779177.96,8168020.75)'),
                ('c', '1'),
                ('from', 'webmap'),
                ('ie', 'utf-8'),
                ('l', '4'),
                ('newmap', '1'),
                ('qt', 's'),
                ('src', '0'),
                ('sug', '0'),
                ('t', time.time().__int__()),
                ('tn', 'B_NORMAL_MAP'),
                ('wd', keyword),
                ('wd2', '')
                 ]
        self.mapurl = 'http://map.baidu.com/'
        self.file = open('%s.txt' % keyword, 'w')
        self.count = 0
        self.count_c = 0
        self.total_num = 0

        self._get_city()

    def _fetch(self, query=None, json=True):
        data = urllib.urlencode(query)
        url = self.mapurl + '?' + data
        opener = urllib.FancyURLopener()
        data = opener.open(url).read()

        if json:
            return self._tojson(data)
        else:
            return data

    def _tojson(self, data):
        try:
            js = json.loads(data, 'utf-8')
        except:
            js = None

        return js

    def _get_city(self):
        data = self._fetch(self.query)

        if type(data['content']) is not types.ListType:
            print 'keyworld error.'
            sys.exit()

        self.city = data['content']

        if data.has_key('more_city'):
            for c in data['more_city']:
                self.city.extend(c['city'])

        for city in self.city:
            self.total_num += city['num']

    def _get_data(self, city, page=0):
        query = [
                ('addr', '0'),
                ('b', '(%s)' % city['geo'].split('|')[1]),
                ('c', city['code']),
                ('db', '0'),
                ('gr', '3'),
                ('ie', 'utf-8'),
                ('l', '9'),
                ('newmap', '1'),
                ('on_gel', '1'),
                ('pn', page),
                ('qt', 'con'),
                ('src', '7'),
                ('sug', '0'),
                ('t', time.time().__int__()),
                ('tn', 'B_NORMAL_MAP'),
                ('wd', self.keyword),
                ('wd2', ''),
                 ]
        data = self._fetch(query)
        return data

    def _save(self, content, city):
        for c in content:
            self.count += 1
            self.count_c += 1
            if c.has_key('tel'):
                tel = c['tel']
            else:
                tel = ''

            _data = '%s\t%s\t%s\t%
2000
s\n' % (city['name'], c['name'], c['addr'], tel)
            self.file.write(_data)
            print '(%s/%s) %s[%s/%s]' % (self.count, self.total_num, city['name'], self.count_c, city['num'])

    def get(self, city):
        self.count_c = 0
        pages = abs(-city['num'] / 10)
        for page in range(0, pages):
            data = self._get_data(city, page)
            if data.has_key('content'):
                self._save(data['content'], city)

    def get_all(self):
        for city in self.city:
            self.get(city)

        self.file.close()

#www.iplaypy.com--------------

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        keyword = sys.argv[1]
    else:
        keyword = '钻石'

    baidumap = BaiduMap(keyword)
    print '_' * 20
    print 'CITY: %s' % baidumap.city.__len__()
    print 'DATA: %s' % baidumap.total_num
    baidumap.get_all()

