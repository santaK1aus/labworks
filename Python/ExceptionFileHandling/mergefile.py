#11.18
fr1=open('file1.txt','r')
fr2=open('file2.txt','r')
fw=open('file3.txt','w')
fw.write(fr1.read()+'\n'+fr2.read())
fr1.close()
fr2.close()
fw.close()