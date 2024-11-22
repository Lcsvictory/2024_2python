
'''
module: datetime
class:  datetime
        date
        time
        timedelta
'''
import datetime
from datetime import datetime as dt

d1 = datetime.datetime.now()
print(type(d1), d1)

d2 = dt.now()
print(type(d2), d2)

print(d2.year)
print(d2.month)
print(d2.day)

print(d2.hour)
print(d2.minute)
print(d2.second)
print(d2.microsecond)

print(d2.weekday())
print(d2.date(), type(d2.date()))
print(d2.time(), type(d2.time()))









