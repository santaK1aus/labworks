#10.16
def pattA(n):
    for i in range(1,n+1):
        print('*'*i)

def pattB(n):
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        print('* '*i)

def pattC(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()

def pattD(n):
    k=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(k,end=' ')
            k+=1
        print()

pattA(6)
pattB(6)
pattC(6)
pattD(6)