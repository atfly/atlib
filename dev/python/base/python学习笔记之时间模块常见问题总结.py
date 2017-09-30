
关于python时间模块问题
#:当前时间时间戳 1312181113.31
print(time.time())
#将字符串转成时间戳
ts = '2011-08-01 14:15:40'
b = time.mktime(time.strptime(ts,'%Y-%m-%d %H:%M:%S'))
print(b)
#返回指定时间的时间戳使用mktime
d = datetime.datetime(1997,12,29,15,59,59)
t = d.timetuple()#再转为元组
print(time.mktime(t)) #使用time的mktime方法返回时间戳

#将时间戳转成时间使用strftime()
u = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.mktime(t)))
print(u)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(b)))

#当前时间 2011-08-01 14:44:32.640000
print(datetime.datetime.now())
#或者:
print(time.strftime('%Y-%m-%d %H:%M:%S'))
