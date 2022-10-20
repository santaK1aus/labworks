#11.2
wf=open('file1.txt','w')
wf.write('Writing in file1.txt\n')
wf.write('Writing in 2nd Line')
wf.close()

rf=open('file1.txt','r')
rfdata=rf.read()
print(rfdata)
rf.seek(0) #resets file read cursor to start

for i in range(2):
    print(rf.readline()) #reads 1 character at a time
rf.seek(0)

for i in range(5):
    print(rf.read(1)) #reads 1 character at a time
rf.seek(0)

while(True):
    ch=rf.read(1) #ch returns '' at EOF
    if ch!='': print(ch,end='')
    else: break

#convert string to raw string
#a='\t ab'
#a.encode('unicode_escape').decode()
#a becomes - '\\t ab'