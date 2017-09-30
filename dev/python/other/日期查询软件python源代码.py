
#coding:utf-8
import os, sys, calendar

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '''usage:
        python yacalendar.py yyyy mm'''

#www.iplaypy.com

    else:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        print calendar.month(year, month)
