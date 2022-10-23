#11.14
fr=open('file1.txt','r')
fw=open('file2.txt','w')
data=fr.read()
fw.write(data[::-1])
fr.close()
fw.close()
print(data[::-1])