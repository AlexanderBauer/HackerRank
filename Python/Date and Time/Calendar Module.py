import calendar
month, day, year    =   input().split()
output              =   calendar.day_name[calendar.weekday(int(year), int(month), int(day))].upper()
print(output)