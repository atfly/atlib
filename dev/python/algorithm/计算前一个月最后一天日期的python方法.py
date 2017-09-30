
from datetime import datetime
from datetime import timedelta
import calendar

def getLastDayOfLastMonth():
    d = datetime.now()
    c = calendar.Calendar()
    
    year = d.year
    month = d.month
    
    if month == 1 :
        month = 12
        year -= 1
    else :
        month -= 1
    days = calendar.monthrange(year, month)[1]   
    return (datetime(year,month,1)+timedelta(days= days)).strftime('%Y-%m-%d %X')  