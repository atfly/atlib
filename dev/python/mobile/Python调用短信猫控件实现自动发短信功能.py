
#! /usr/bin/env python
#coding=gbk

import sys
import win32com.client

ocxname='ShouYan_SmsGate61.Smsgate'
axocx=win32com.client.Dispatch(ocxname)
axocx.CommPort=8#设置COM端口号
axocx.SmsService='+8613800100500'#设置短信服务号码
axocx.Settings='9600,n,8,1'#设置com端口速度
axocx.sn='loyin'

#www.iplaypy.com

c=axocx.Connect(1)#连接短信猫或手机

print '连接情况',axocx.Link()

axocx.SendSms('python确实是很好的','15101021000',0)#发送短信
