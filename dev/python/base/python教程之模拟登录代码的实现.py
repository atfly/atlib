
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import getpass

logintimes = 0
while logintimes < 3:
    name=raw_input("Please input your username:")
    pwd=getpass.getpass("Please input your password:")
    if name=='wxy' and pwd=='123':
        #正确后允许进入并退出循环
        print "Welcome,login succeed!"
        break
    else:
        #错误时，出错计数加1
        print "Error,login again:"
        logintimes+=1
else:
    #错误达到三次后,结束此循环
    print "Sorry,account has been locked!"
#!/usr/bin/env python 
#! -*- coding: utf-8 -*-

for i in range(3):  # 设定循环次数
	name = raw_input("请输入用户名：")
	pwd = raw_input("请输入密码：")
	if name == "wxy" and pwd == "123":
		print "登录成功，欢迎！"
		# 用户信息认证成功，跳出循环
		break    	
	else:
		print "用户信息错误，请重新输入！"
else:
	# 用户信息输错三次后，账号锁定
	print "很抱歉，用户已锁定！"