#11.5
import os

name=input('Enter file name : ')
try:
    fr=open(name)
    print('File',name,'exists and is deleted')
    fr.close()
    os.remove(name)
except FileNotFoundError:
    print('File',name,'doesn\'t exist')