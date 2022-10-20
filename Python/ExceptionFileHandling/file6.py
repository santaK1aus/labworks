#11.8,9
fr=open('file1.txt','r')
c=0
while len(fr.readline())>0:
    c+=1
print(c,'lines present')
fr.seek(0)

ch=fr.read(1)
c=0
while ch!='':
    if ch==' ' or ch == '\n': c+=1
    ch=fr.read(1)
print(c+1,'words present')

fr.close()