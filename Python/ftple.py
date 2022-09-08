#7.4
li=[1,2,3,4,5,(8,9),6,7]
c=0
for i in li:
    if type(i) is tuple:
        break
    c+=1
print(li)
print('Count before tuple :',c)