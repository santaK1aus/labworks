#10.10,11
import calendar

print('Months : ')
for i in range(1,13):
    print(calendar.month_name[i],end=' ')

print('\nDays : ')
for i in range(7):
    print(calendar.day_name[i],end=' ')