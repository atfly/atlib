
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import datetime
import traceback
import logging
import os
# 测试用例执行函数
def work(browser):
    url = "http://yourdomain.com"
    browser.get(url)
    try:
        # 输入账号和密码
        browser.find_element_by_name("username").send_keys(u"用户名")
        browser.find_element_by_name("password").send_keys("123456")
        time.sleep(2)

        #点击按钮提交登录表单
        browser.find_element_by_class_name("btn").click()
        time.sleep(5)

        # 验证登录成功的url
        currUrl = browser.current_url
        if currUrl == "http://yourdomain.com/cate/index":
            print u"success"
        else:
            print u"failure"
            writeLog()
    except:
        print u"failure"
        writeLog()

# 写错误日志并截图
def writeLog():
    # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
    basename = os.path.splitext(os.path.basename(__file__))[0]
    logFile = basename+"-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".log"
    logging.basicConfig(filename=logFile)
    s = traceback.format_exc()
    logging.error(s)
    browser.get_screenshot_as_file("./"+logFile+"-screenshot_error.png")

if __name__ == "__main__":
    browser = webdriver.Firefox()
    work(browser)
    browser.quit()