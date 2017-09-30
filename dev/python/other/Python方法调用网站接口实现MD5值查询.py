
#-*-coding:utf-8-*-
'''
注：如不带命令参数，则本程序只会进行HASH值的扫描查询，不会将查询到的结果保存到本地数据库中。
'''

import os
import sys
import stat
import json
import time
import getopt
import hashlib
import urllib2
import sqlite3

class MD5_Search(object):
        
    def __init__(self):
        
        self.db_name = []
        self.state = ('Unknow', 'Safe', 'Virus')
        self.url = "http://xxx.xxx.com/index.php?x=xzj&y=lzsd"

        
    def report(self):
        
        info = ''
        info += "=====================================================================\n"
        info += "@Author: xuzhijian17 2011 LZSD command line scanner \n"
        info += "Copyright (c) 1990 - 2011 Qianyun Technologies\n"
        info += "Program version 10.0.1388, engine 10.0.1516\n"
        info += "Version 1516/3730 %s\n" % time.strftime("%Y-%m-%d %H:%M:%S")
        info += "---------------------------------------------------------------------\n"
        
        return info
    
    def del_file(self, file_path):
        
        try:
            os.chmod(file_path, stat.S_IWRITE)
            os.remove(file_path)
        except WindowsError:
            print "File already delete or does not exist."
                    
    def file_md5(self, file_name):

        with open(file_name, 'rb') as fb:
            md5 = hashlib.md5(fb.read()).hexdigest()            
        return md5
    
    def scan_files(self, folder):
        
        dct = {}
        for x, y, z in os.walk(folder):
            for i in z:
                file_name = os.path.join(x, i)
                if os.path.isfile(file_name):
                    md5 = self.file_md5(file_name)
                    dct[md5] = file_name 
                else:
                    self.del_file(file_name)
        return dct
            
    def db(self, name):
        
        db_name = os.path.join(os.path.dirname(__file__), name)
        if os.path.isfile(db_name):
            db_size = os.path.getsize(db_name)
            if db_size < 10485760: #判断数据库文件是否大于10M
                self.db_name.append(db_name)
            else:
                db_name = os.path.join(os.getcwd(), 'xzj_' + name)
                self.Create_db(db_name)
                self.db_name.append(db_name)
        else:
            self.Create_db(db_name)
            self.db_name.append(db_name)
            
    def Create_db(self, db_name):
        
        conn = sqlite3.connect(db_name)
        cu = conn.cursor()
        cu.execute('''create table if not exists hashQuery(id integer primary key autoincrement,md5 varchar(128)UNIQUE,state varchar(128),date varchar(128))''')
        conn.commit()
        cu.close()
        
    def LocalInquire(self, folder):
        
        dct = {}
        for db_name in self.db_name:
            try:
                conn = sqlite3.connect(db_name)
                cu = conn.cursor()
                for file_md5, file_path in self.scan_files(folder).items():
                    cu.execute("select * from hashQuery where md5=?", (file_md5,))
                    dct[file_path] = cu.fetchone()
            except sqlite3.IntegrityError:
                pass
            finally:
                conn.commit()
                cu.close()

        return dct

    def hashQuery(self, md5):
                
        try:
            req = urllib2.Request(self.url, 'hashs=%s' % md5, headers={'User-Agent':'SucopAnalyze/1.0'})
            page = urllib2.urlopen(req, timeout=10)
            content = page.read()
            page.close()
            for md5, stat in json.loads(content)['data'].items():
                if stat['stat'] == 0: #stat = 0 是未知
                    return 0
                elif stat['stat'] == "1": #stat = 1 是安全
                    return 1
                elif stat['stat'] == "2": #stat = 2 是危险
                    return 2
            
        except urllib2.HTTPError, e:
            print e.code
            print e.msg
            print e.headers
            print e.fp.read()
            
 
2000
#www.iplaypy.com
 
      except urllib2.URLError, e:
            print e
            
    def run(self, db_name, folder, arge1, arge2, arge3, log_path):

        self.db(db_name) 
        
        date = time.ctime()
        conn = sqlite3.connect(self.db_name[-1])
        cu = conn.cursor()

        with open(log_path, 'w') as fp:
            fp.write(self.report())
            try:
                print "Start local scaning......"
                for file_path, database in self.LocalInquire(folder).items():
                    if database:
                        if database[2] == self.state[1]:
                            safe = "%s %s\t%s" % (date, file_path, self.state[1])
                            print safe
                            if arge1:
                                self.del_file(file_path)
                                print file_path + "\t...Delete Succeed"
                            fp.write(safe + '\n')
                        elif database[2] == self.state[2]:
                            malive = "%s %s\t%s" % (date, file_path, self.state[2])
                            print malive
                            if arge2:
                                self.del_file(file_path)
                                print file_path + "\t...Delete Succeed"
                            fp.write(malive + '\n')
                        
                if arge3:
                    print "Start cloud scaning....."
                    for file_md5, file_path in self.scan_files(folder).items():
                        if self.hashQuery(file_md5) == 0:
                            unknow = "%s %s\t%s" % (date, file_path, self.state[0])
                            print unknow
                            fp.write(unknow + '\n')
                        elif self.hashQuery(file_md5) == 1:
                            safe = "%s %s\t%s" % (date, file_path, self.state[1])
                            print safe
                            if arge1:
                                self.del_file(file_path)
                                print file_path + "\t...Delete Succeed"
                                cu.execute("insert into hashQuery(md5,state,date) values('%s','%s','%s')" % (file_md5, self.state[1], date))
                            fp.write(safe + '\n')
                        elif self.hashQuery(file_md5) == 2:
                            malive = "%s %s\t%s" % (date, file_path, self.state[2])
                            print malive
                            if arge2:
                                self.del_file(file_path)
                                print file_path + "\t...Delete Succeed"
                                cu.execute("insert into hashQuery(md5,state,date) values('%s','%s','%s')" % (file_md5, self.state[2], date))
                            fp.write(malive + '\n')
            finally:
                conn.commit()
                cu.close()
    
def main():     

    if len(sys.argv) < 2:
        print __doc__
        sys.exit()

    try:                                
        opts, args = getopt.getopt(sys.argv[1:], "hsmc", ["help", "file=", "log="])
    except getopt.GetoptError:
        print "parameter input error! please type -h or --help."
        sys.exit()
        
    arge1 = None
    arge2 = None
    arge3 = None
    folder = None
    db_name = 'hashQuery.db'
    log_path = os.path.join(os.path.dirname(__file__), 'hashQuery.log')
    
    ms = MD5_Search()
    for opt, arg in opts:               
        if opt in ("-h", "--help"):     
            print __doc__                     
            sys.exit()
        elif opt == "-s":
            arge1 = opt
        elif opt == "-m":
            arge2 = opt
        elif opt == "-c":
            arge3 = opt
        elif opt == "--file":
            folder = arg
        elif opt == "--log":
            log_path = arg
          
    if folder:        
        ms.run(db_name, folder, arge1, arge2, arge3, log_path)

if __name__ == '__main__':
    
    main()       
