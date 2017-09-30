
from datetime import datetime
import calendar

def getMonths():
    d = datetime.now()
    c = calendar.Calendar()
    
    year = d.year
    month = d.month
    
    if month == 1 :
        month = 12
        year -= 1
    else :
        month -= 1
    months = calendar.monthrange(year, month)[1]    
    return months 

#www.iplaypy.com