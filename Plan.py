# -*- coding: utf-8 -*-
"""
Migration model M3 to M12 payment model
Created on Thu Jul 26 09:45:02 2018

@author: CP339977
"""

#morning before 3PM and after 3pm is noon

def workplanner(day,date,time):
    if day == "Monday" and time >= 15 and (date >= 14 or date <= 4) :
        return "Capout related admin"
    if day == "Monday" and time <= 15 and (date <= 14 or date >= 4) :
        return "FTC tracking related admin"
    elif day in ("Tuesday", "Wednesday", "Thursday") and time <= 15 and (date >= 14 or date <= 4):
        return "Capout code"
    elif day in ("Tuesday", "Wednesday", "Thursday") and  time >= 15 and (date >= 14 or date <= 4):
        return "Migration model to azure"
    elif day in ("Tuesday", "Wednesday", "Thursday") and time <= 15 and (date <= 14 or date >= 4):
        return "FTC Tracking"
    elif day in ("Tuesday", "Wednesday", "Thursday") and time >= 15 and (date <= 14 or date >= 4):
        return "MM variable report"
    elif day == "Friday" and time <= 15 and (date >= 14 or date <= 4) :
        return "Capout related admin"
    elif day == "Friday" and time <= 15 and (date <= 14 or date >= 4) :
        return "FTC tracking related admin"
    else:
         return "Research/Learning/Data camp"
     
        
import datetime
import calendar
from datetime import date

now = datetime.datetime.now()

my_date = date.today()

a = calendar.day_name[my_date.weekday()]

print(workplanner(a, now.day,now.hour))
