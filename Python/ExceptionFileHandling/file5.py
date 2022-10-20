#11.7
fr=open('file1.txt','r')
for word in fr.readline().split():
    print(word)
fr.close()