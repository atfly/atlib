
#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
  
__revision__ = '0.1'  
__author__ = 'lxd'  

import threading  
import time  
  
class TimeWorks(object):  
    def __init__(self):  
        self.wait_works = {}#等待工作列表，包括工作的所有细节  
        self.wait_times_threads = []#线程列表  
  
    def setTime(self, data, seconds):  
        """将data放入等待工作列表中，并将工作放入线程中等待 
        """  
        def sleep(seconds):  
            time.sleep(seconds)  

#www.iplaypy.com  

        atime = threading.Thread(target = sleep, args = (seconds, ))  
        atime.setDaemon(True)  
        atime.start()  
        self.wait_times_threads.append(atime)  
  
        self.wait_works.update({atime.name:data})  
  
    def checkTimeThread(self):  
        """获得时间已到的工作 
        """  
        for atime in self.wait_times_threads:  
            if not atime.isAlive():  
                self.wait_times_threads.remove(atime)  
                return self.wait_works.pop(atime.name)  
  
if __name__ == '__main__':  
    print 'start'  
    timeWorks = TimeWorks()  
  
    build = {'kind':'build', 'name':'build1', 'pos':(1, 2)}  
    timeWorks.setTime(build, 5)  
  
    farm = {'kind':'farm', 'name':'tom', 'pos':(3, 5)}  
    timeWorks.setTime(farm, 3)  
  
    def build_something(data):  
        print 'build_something', str(data)  
  
    def farm_something(data):  
        print 'farm_something', str(data)  
  
    i = 0  
    while True:  
        print 'do_something', i  
        i += 1  
        time.sleep(1)  
  
        data = timeWorks.checkTimeThread()  
        if data:  
            if data['kind'] == 'build':  
                build_something(data)  
            elif data['kind'] == 'farm':  
                farm_something(data)