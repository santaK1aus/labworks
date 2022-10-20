#11.10
fr=open('file1.txt','r')
max=''
for line in fr.readlines():
    for word in line.split():
        if len(word)>len(max):
            max=word

print('Longest word is ',max)