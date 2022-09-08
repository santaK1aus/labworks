#8.1
dict1={'A':1,'B':2,'C':3,'D':4,'E':5}
print(dict1)
dict1['E']=6
print(dict1)
dict1['F']=7
print(dict1)
dict1.pop('E')
print(dict1)
dict1.pop(list(dict1)[0])
print(dict1)
dict1.clear()
print(dict1)
del dict1
dict1={'A':6,'B':2,'C':67,'D':-1,'E':5}
dict2={i:i**2 for i in range(1,11)}
print(dict2)
dict2={i:i**2 for i in range(1,11,2)}
print(dict2)
print('Length :',len(dict2))

#dict3={}
#for i in sorted(list(dict.values())):
#    dict3[list(dict1.keys())[list(dict.values()).index(i)]]=i

dict3=(dict1|dict2)
print(dict3)
dict3.pop('hi',None)

print(sorted(frozenset(list(dict3.values()))))