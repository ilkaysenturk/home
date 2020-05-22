import datetime as dt
time=dt.datetime.now()
print(time.year)
print(time.strftime("%A"))

time=dt.datetime(2020, 6 ,6)
print(time)

print(time.strftime("%B"))
