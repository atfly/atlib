
#coding=utf-8
import time,sched,os

s = sched.scheduler(time.time,time.sleep)

def event_func():
    print "Current Time:",time.time()

def perform(inc):
    s.enter(inc,0,perform,(inc,))
    event_func()
   
def mymain(inc=60):
    s.enter(0,0,perform,(inc,))
    s.run()

# if __name__ == "__main__":
    # mymain() 