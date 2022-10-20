#11.3
af=open('file1.txt','a+') #Append mode
af.write('\nAppending 3rd line from another script')
af.seek(0)
print(af.read())
af.close()