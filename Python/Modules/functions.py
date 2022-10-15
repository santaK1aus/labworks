#10.15

def fact(n):
    if n==0: return 1
    return fact(n-1)*n

def funca(x,y):#a
    if y<=x:
        return funca(x-y,y)+1
    else:
        return 0

def funcb(n,r):#b
    if n==0 or r==0:
        return 1
    return funcb(n-1,r)+funcb(n-1,r-1)

def funcc(n):#c
    if n<=1:
        return 0
    return funcc(n/2)+1

def funcd(M,N):#d
    if M==0 or M>=N>=1:
        return 1
    return funcd(M-1,N)+funcd(M-1,N-1)

def funce(m,x):#e
    if x==0:
        return 1
    elif m>x:
        return fact(m)/(fact(x)*fact(m-x))
    return funce(m,x-1)*((m-x+1)/x)

print(funca(6,2))
print(funcb(6,2))
print(funcc(6))
print(funcd(2,6))
print(funce(6,2))