#7.1.a,b,c,d
t=(1,2,3)
print(t)
del t
t1=(1,2,3)
t2=(4,5,6)
t1=t1+t2
print(*t1,sep=' ')
t1=(1,)
t1=t1*5
print(t1)
print(list(t1))
t1=(1,2,3,4,5)
print(max(t1),min(t1))