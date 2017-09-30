
#python3 www.iplaypy.com
#格式化当天日期
import datetime
now=datetime.datetime.now()#获得当天时间
print(now)
today=now.strftime("%y%m%d")#格式化日期
print(today)

'''
output:
>>> 
2015-10-25 17:50:18.534627
151025
'''
