#10.12
from datetime import date

yr=int(input('Enter year : '))
i=1
day=date(yr,1,i)
while day.isoweekday()!=1:
    i+=1
    day=date(yr,1,i)
print('First monday is on',day)