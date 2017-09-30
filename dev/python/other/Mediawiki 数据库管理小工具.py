
#!/usr/bin/env python
# encoding: utf-8

import sys
import MySQLdb

# 设置默认编码为UTF-8，否则从数据库
# 读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

def MySQLconn():
 db_host = "localhost"
 db_user = "root"
 db_passwd = "0000000"
 charset = "UTF8"

 try:
  conn = MySQLdb.Connection(host=db_host, user=db_user, passwd=db_passwd, charset=charset)
  return conn
 except Exception,e:
  print "Could not connect to MySQL Server"


#连接数据库www.iplaypy.com

def old_page():
    try:
     conn=MySQLconn()
     conn.select_db('atyu30')
     cursor = conn.cursor(MySQLdb.cursors.DictCursor)
     cursor.execute("set NAMES utf8")
     cursor.execute(sql)

     for row in cursor.fetchall():
        old_id = row["page_id"]
        return old_id

     cursor.close()
     conn.close()

    except conn.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

def new_page():
    try:
     conn=MySQLconn()
     conn.select_db('atyu30')
     cursor = conn.cursor(MySQLdb.cursors.DictCursor)
     cursor.execute("set NAMES utf8")
     #print sqlupdate
     cursor.execute(sqlupdate)
     cursor.close()
     conn.commit()
     conn.close()

    except conn.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

if __name__=='__main__':
    nTITLE = raw_input("旧标题:")
    sql = "select page_id,page_title from page where page_title =  '%s'" % (nTITLE)

    old_id=old_page()
    nTITLES = raw_input("新标题:")
    sqlupdate = "update page set page_title = '%s'  where page_id=%s" % (nTITLES,old_id)
    new_page()