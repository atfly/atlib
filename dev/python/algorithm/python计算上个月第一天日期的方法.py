
#导入方法
from datetime import datetime
from datetime import timedelta
import calendar

def getFirstDayOfLastMonth():
    d = datetime.now()
    c = calendar.Calendar()
    
    year = d.year
    month = d.month
    
    if month == 1 :
        month = 12
        year -= 1
    else :
        month -= 1
    return datetime(year,month,1).strftime('%Y-%m-%d %X')  
#www.iplaypy.com