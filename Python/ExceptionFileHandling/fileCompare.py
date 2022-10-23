#11.15
fr1=open('file1.txt','r')
fr2=open('file2.txt','r')
print('Content is equal : ',fr1.read()==fr2.read())
fr1.close()
fr2.close()