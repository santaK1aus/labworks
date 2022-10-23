#11.16
fr=open('file1.txt','r')
fw=open('file2.txt','w')
while 1:
    ch=fr.read(1)
    if ch!='': fw.write(ch)
    else: break
fr.close()
fw.close()