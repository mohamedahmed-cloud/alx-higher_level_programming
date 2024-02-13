#!/usr/bin/env python3
import pytz
import datetime
d = datetime.date(2017,8,9)
today = datetime.date.today()

print(d)
print(today)
print(today.weekday())
print(today.isoweekday())
print(today.year)
print(today.month)
print(today.day)

print("#" * 80)
# Time Delta
tday = datetime.date.today()
time_delta = datetime.timedelta(days=6)
print(time_delta.days)
print(time_delta.total_seconds())
date = tday + time_delta
print(date)

print("#" * 80)

# date time
# we will work with hours, minutes, seconds, microseconds
# datetime.time(hours, minutes, seconds, microseconds)
t = datetime.time(9, 33, 23, 12)
print(t)
print(t.hour)
print(t.minute)

# datetime.date
print("#" * 80)
# t = datetime.date() # access on year, month, day
# t = datetime.time() # access on hour, minutes, seconds
# t = datetime.datetime() # access on any thing.
# datetime(year, month, day, hour, minutes, second, milliseconds)
t = datetime.datetime(2023, 10, 4, 12, 40, 12, 1200)
print(t)
print(t.time())
print(t.date())
print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.minute)

tdelta = datetime.timedelta(hours=4)
print(t)
print(t + tdelta)
print("#" * 80)
# time zone
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

# pytz lib
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
# to convert from utc to Africa/Cairo 
# you can convert from any time zone to another.
# but to convert must time converted have a time zone.
dt_me = dt_utcnow.astimezone(pytz.timezone("Africa/Cairo"))
print(dt_me)
# for tz in pytz.all_timezones:
# 	print(tz, end = " - ")


# best time foramt is isoformat
print(dt_me.isoformat())

# specific format for 
# strftime - convert datetime to string
# strptime - convert string to datetime
print(dt_me.strftime("%B %d, %Y"))
d_str = "October 18, 2023"
print(datetime.datetime.strptime(d_str, "%B %d, %Y"))