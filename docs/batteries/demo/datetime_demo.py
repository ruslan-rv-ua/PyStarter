from datetime import date, time, datetime, timedelta

d = date(2025, 2, 28)
# d = datetime(2025, 2, 29)
print(d, d.day)

d=date.today()

#######################

t = time(23, 59, 59)
print(t)
print(t.hour)

###############

d = datetime.now()

s = datetime.strftime(d, '%Y/%m/%d')
print(s)
print(f'{d:%Y/%m/%d}')

s='2025/10-03'
d = datetime.strptime(s, '%Y/%m-%d')

##############

d = datetime(2022, 2, 24)
now = datetime.now()

r = now > d

td = now - d
#print(f'{td.days}-й день війни.')
print(td.days)

#####################

import datetime as dt
from zoneinfo import ZoneInfo

n = dt.datetime.now()
r = n.tzinfo
# n = dt.datetime.now(tz=ZoneInfo('Europe/Kyiv'))
r = n.tzinfo
# n = dt.datetime.now(tz=dt.UTC)
r = n.tzinfo


o = dt.datetime.utcoffset(n)#.seconds / 3600
