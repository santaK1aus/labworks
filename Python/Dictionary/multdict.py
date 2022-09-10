#8.8,9
dict1={'A':6,'B':2,'C':67,'D':-1,'E':5}
mult=1
sum=0
for v in dict1.values():
    mult*=v
    sum+=v
print('Sum :',sum)
print('Net :',mult)