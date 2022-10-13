#10.4
from datetime import datetime

now=datetime.now()
datestr=now.strftime('%d/%m/%Y %H:%M:%S')
print(datestr)