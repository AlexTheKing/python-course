import datetime

print("Now:", datetime.datetime.now())
print("Date, that was 5 days ago:", datetime.date.today() - datetime.timedelta(days=-5))

year = datetime.timedelta(days=365)
print("Timedelta 365 days:", year)
ten_years = year * 10
print("Timedelta 3650 years:", ten_years)

d = datetime.date(2019, 7, 14)
print("Date:", d)
t = datetime.time(12, 30)
print('Time:', t)
print("Combine date and time:", datetime.datetime.combine(d, t))