from datetime import datetime, date, time

today = date.today()  # gets current date
print(today)

tomorrow = date(2024, 1, 17)  # iso format
print(tomorrow)

next_week = date.fromisoformat("2024-01-22")  # build date using string
print(next_week)

right_now = datetime.now()  # gets current date and time
print(right_now)

print(right_now.timestamp())  # number of seconds from January 1st 1970

my_date = datetime.fromtimestamp(1500000000)
print(my_date)


