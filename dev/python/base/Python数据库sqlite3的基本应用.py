
import sqlite3
import time

conn=sqlite3.connect(r'D:\Exercise\Python\DB\example.db')

c=conn.cursor()
c.execute("Create table if not exists stocks (date text, trans text, symbol text, qty real, price real)")

flag=raw_input("Do you wanna clean the table?(y/n):")

if flag=='y':
	c.execute("delete from stocks")
c.execute("Insert into stocks values('"+time.strftime('%Y-%m-%d %H:%m:%S')+"', 'Buy','Rhatd',1000,23.14)")
conn.commit()
c.execute('select * from stocks')

res=c.fetchall()

count=0

print res

print '-'*60

for line in res:
	for f in line:
		count=count+1
		print count,f,
	print

print '-'*60
print '-'*60
print 'There are %d records!'  %count
c.close()
conn.close()
#www.iplaypy.com