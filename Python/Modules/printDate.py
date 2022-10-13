#10.8
from datetime import datetime

day=datetime(int(input('Enter year and month and day :')),int(input()),int(input()))
print(day.strftime('%d/%m/%Y'))