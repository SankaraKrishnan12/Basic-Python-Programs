import calendar
year = int(input("Enter Year : "))
month = int(input("Enter Month : "))
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_str = cal.formatmonth(year, month)
print(cal_str)
