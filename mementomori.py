#!/bin/python3

from datetime import *
from calendar import monthrange
from dateutil.relativedelta import relativedelta
import time
from random import randint

r = randint(0,1)
if r == 0:
    birth = date(1999,3,6)
    person = "E"
elif r == 1:
    birth = date(1960,3,10)
    person = "P"

eightybday=birth + relativedelta(years=80)

def diff_month(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

now = date.today()
months_lived= (diff_month(birth, now))
months_till80=(diff_month(birth, eightybday))
diff=months_lived/months_till80
months_remaining=(diff_month(now, eightybday))
diff="{:.1%}".format(diff)
print(person + " " + str(months_lived) + " (" + str(diff) +")")
