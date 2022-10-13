#10.13
from datetime import date,datetime

today=date.today()
now=datetime.now()
print(now)
print('year:',today.strftime('%Y'))
print('month:',today.strftime('%m'))
print('day:',today.strftime('%d'))
print('time:',now.strftime('%H:%M:%S'))
print('date and time:',now.strftime('%d/%m/%Y, %H:%M:%S'))