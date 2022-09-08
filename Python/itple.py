#7.5
t=(1,2,3,4,5,6,7,8)
print(t)
inp=int(input('Enter value to search : '))
pos=t.index(inp) #raises ValueError if item not found
print('Found at',pos)
pos=t.index(inp,3,4) #start and stop index
str='Hello there'
li=list(str)
print(li)