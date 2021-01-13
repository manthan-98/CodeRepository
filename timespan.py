# Calculating timespan
import datetime as dt
year = int(input('year = '))
month = int(input('Month = '))
day = int(input('date = '))
any_day = dt.date(year, month, day)
today = dt.date.today()
no_of_days = today-any_day
print(no_of_days)