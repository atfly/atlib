
#!/bin/env python
#coding:utf-8
#统计nginx的访问ip和流量
#具有时间段分析功能
import sys
import ip_location
import time
import re
reload(sys)
sys.setdefaultencoding('utf-8')
#time_start=sys.argv[1]
#time_start=sys.argv[2]
ipflow={}
ipnum={}
#nginx日志
log_file="/data/logs/lolo.log"
#时间的正则和格式
re_time='\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}'
str_time='%d/%b/%Y:%H:%M:%S'

#"时间段"
class TimeParser(object):
    def __init__(self,re_time,str_time):
        self.re_time=re.compile(re_time)
        self.str_time=str_time
    def get(self,line):
        t=re.search(self.re_time,line).group(0)
        return time.mktime(time.strptime(t,self.str_time))
    def inPeriod(self,line):
        t=self.get(line)
        return (t>time.mktime(time.strptime(start_time,self.str_time)) and t<time.mktime(time.strptime(end_time,self.str_time)))
#处理函数
class ParseLog(object):
    def __init__(self,file_name):
        self.file_name=file_name
        self.re_time=re.compile(re_time)
        self.srt_time=str_time
    def show(self):
        fd=open(self.file_name,"r")
        contens=fd.readlines()
        fd.close()
        Time=TimeParser(self.re_time,self.srt_time)
        for line in contens:
            if Time.inPeriod(line):
                ip=line.split()[1]
                flow=line.split()[10]
                #采用集合
                if ip in set(k.lower() for k in ipflow):
                    ipnum[ip]+=1
                    ipflow[ip]=int(ipflow[ip])+int(flow)
                else:
                    ipnum[ip]=1
                    ipflow[ip]=int(flow)
        for k in ipnum:
            name=ip_location.ip_location(k)
            print "访问IP:%s 访问次数:%d 访问流量%.3fK 归属地:%s" %(k,int(ipnum[k]),ipflow[k],name)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "输入的参数错误"
        sys.exit()
    start_time=sys.argv[1]
    end_time=sys.argv[2]
    p=ParseLog(log_file)
    p.show()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the script is used to query the location of every ip
#淘宝库ip地址查询
import urllib
import json
import sys
#淘宝ip库接口
url = "http://ip.taobao.com/service/getIpInfo.php?ip="
def ip_location(ip):
        data = urllib.urlopen(url + ip).read()
        datadict=json.loads(data)
        for oneinfo in datadict:
                if "code" == oneinfo:
                        if datadict[oneinfo] == 0:
                                return datadict["data"]["country"] + datadict["data"]["region"] + datadict["data"]["city"] + "\t\t" + datadict["data"]["isp"]

if __name__ ==  "__main__":
        ip=sys.argv[1]
        name=ip_location(ip) 
        print name