#11.17
from curses.ascii import isupper


fr=open('file1.txt','r')
fw=open('file2.txt','w')
while 1:
    ch=fr.read(1)
    if ch=='': break
    if ch.isupper():
        fw.write(ch.lower())
    else: fw.write(ch.upper())
fr.close()
fw.close()