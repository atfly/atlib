
#!/usr/bin/python

import MySQLdb
import getopt
import sys
from datetime import datetime

conf_host = '127.0.0.1'
conf_port = 3306
conf_user = 'root'
conf_pass = ''
conf_db = 'information_schema'
conf_bind_db = 'mydns'

def main():

    db_bind = MySQLdb.connect(host = conf_host, port = conf_port, user = conf_user, passwd = conf_pass, db = conf_bind_db)
    cursor_bind = db_bind.cursor()
    db = MySQLdb.connect(host = conf_host, port = conf_port, user = conf_user, passwd = conf_pass, db = conf_db)
    cursor = db.cursor()
    file = open("output.txt","w")
    cursor.execute("select table_name from tables where table_name regexp'rg_' and table_schema ='" + conf_bind_db + "';")
    #www.iplaypy.com

    for row in cursor.fetchall():
        print row[0]
        sql = "select zone,host,type,data,ttl from  " + row[0] + " where zone regexp'(cnc|ct|edu|ov).centos.com' and data='originboss.centos.com.' and type='cname';"
        cursor_bind.execute(sql)
        result = cursor_bind.fetchall()
        for row in result:
	            print row[0],row[1],row[2],row[3],row[4]        
    cursor.close()
    db.close()    
    
    cursor_bind.close()
    db_bind.close()
    
if __name__ == '__main__':
    main()