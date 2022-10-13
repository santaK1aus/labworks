#10.6
import calendar

a=int(input('Enter lower bound of years :'))
b=int(input('Enter upper bound of years :'))
print('Leap years in given range : ')
for yr in range(a,b+1):
    if(calendar.isleap(yr)):
        print(yr,end=', ')