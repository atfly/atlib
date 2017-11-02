
import time
#一.壁挂钟时间
#time
time.time()
1460599046.85416
#ctime()
#浮点数一般用于存储和比较日期，但是对人类不友好，要记录和打印时间，可以使用ctime()。
import time
time.ctime()


#二.处理器时钟时间
#clock()返回处理器时钟时间，它的返回值一般用于性能测试与基准测试。因此它们反映了程序的实际运行时间。
import time
time.clock()

#三.时间组成
#time模块定义了struct_time来维护时间和日期，其中分开存储各个组成部分，以便访问。
import time
def show_struct(s):
      print "tm_year:", s.tm_year
      print "tm_mon:", s.tm_mon
      print "tm_mday:", s.tm_mday
      print "tm_hour:", s.tm_hour
      print "tm_min:", s.tm_min
      print "tm_sec:", s.tm_sec
      print "tm_wday:", s.tm_wday
      print "tm_yday:", s.tm_yday
show_struct(time.gmtime()) #gmtime()#用于获取UTC时间
show_struct(time.localtime()) #localtime()用于获取当前时区的当前时间，UTC时间实际就是格林尼治时间，它与中国时间的时差为八个小时。

#四.处理时区
#1.获取时间差
import time
time.timezone/3600 #-8

#2.设置时区
import os
ZONES = ["GMT", "EUROPE/Amsterdam"]
for zone in ZONES:
      os.environ["TZ"] = zone
      time.tzset()

#五.解析和格式化时间
#time模块提供了两个函数strptime（）和strftime（），可以在struct_time和时间值字符串之间转换。
#1.strptime()

用于将字符串时间转换成struct_time格式：
now=time.ctime()
time.strptime(now)
time.struct_time(tm_year=2016, tm_mon=4, tm_mday=14, tm_hour=10, tm_min=48, tm_sec=40, tm_wday=3,tm_yday=105, tm_isdst=-1)

#2.strftime()
#用于时间的格式化输出
 from time import gmtime, strftime
 strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'

#3.mktime()
#于将struct_time转换成时间的浮点数表示
from time import mktime, gmtime
mktime(gmtime()) #1460573789.0

#六.sleep()
#sleep函数用于将当前线程交出，要求它等待系统将其再次唤醒，如果写程序只有一个线程，这实际上就会阻塞进程，什么也不做。
import time
def fucn(): #执行上面的代码，将等待5秒钟之后再输出信息。
      time.sleep(5)
      print "hello, world"
