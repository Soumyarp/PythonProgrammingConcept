from _datetime import datetime, timedelta
import sys
import datetime
import pytz
from pytz import timezone
# currenttime = datetime.now()
# print(currenttime)
# utc_actual= datetime.utcnow()
# print(utc_actual)
# utc_time = datetime.utcnow() - timedelta(seconds=10)
# print(utc_time)
# starttime = utc_time - timedelta(seconds=11)
# print(starttime)


x=2
y=5

if (not x%2) and y%5:
    print(1)
elif x==2:
    print(2)
else:
    print(3)


print(sys.path)



a= datetime.datetime(2024,7,31,15, 11, 3, 000)
b = a + datetime.timedelta(seconds=298)
print(a.time())
print(a.date())
print(b.time())
print(b.date())

# utc=pytz.utc
# print(utc)
# amsterdam = timezone('Europe/Amsterdam')
# print(amsterdam)


# Define the date format and the time delta for one week
date_format = "%Y-%m-%d-%H"
now = datetime.datetime.now()
one_week_ago = now - timedelta(weeks=1)
date_str = one_week_ago.strftime(date_format)

# print(date_str)