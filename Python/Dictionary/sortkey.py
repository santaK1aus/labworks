#8.10,11
d1={'A':6,'C':67,'E':5,'B':2,'D':-1}
d2={}
for k in sorted(d1.keys()):
    d2[k]=d1[k]
print(d2)
print('Is empty :',len(d2)==0)