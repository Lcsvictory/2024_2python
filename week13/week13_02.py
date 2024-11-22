
import datetime
from datetime import datetime as dt

# %Y-%m-%d %H:%M:%S.%f

datetime_format = "%Y-%m-%d %H:%M:%S"

d1 = dt.now()
#d2 = dt.strftime(d1, datetime_format) # datetiem -> str
d2 = d1.strftime(datetime_format)
d3 = dt.strptime(d2, datetime_format) # str -> datetime

print(type(d2), d2)
print(type(d3), d3)

print('-'*30)


d1 = datetime.datetime(2030, 10, 2, 18, 0, 2, 200) #시작
d2 = datetime.datetime(2031, 10, 3, 17, 3, 3, 202) #종료

td = d2 - d1
print(dir(td))
print(td.days, type(td))
print(td.seconds)
print(td.microseconds)
print(td.total_seconds())

d3 = d1 + datetime.timedelta(days=7)
d4 = d2 + datetime.timedelta(days=7)
print(d1,d3)
print(d2,d4)






















