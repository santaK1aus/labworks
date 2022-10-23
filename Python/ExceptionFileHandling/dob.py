#11.11
from datetime import datetime

try:
    dobin=input('Enter date of birth YYYY/MM/DD : ').split('/')
    dob=datetime(int(dobin[0]),int(dobin[1]),int(dobin[2]))
    name=input('Enter name : ')
    gender=input('Enter gender : ')
    print('Name :',name,'\nGender :',gender,'\nDate of Birth :',dob.strftime('%d/%m/%Y'))
except ValueError:
    print('Wrong input')