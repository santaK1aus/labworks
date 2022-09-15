#9.8
def gcd(m,n):
    if m%n==0:
        return n
    return gcd(n,m%n)

def gcdarr(li):
    lc=li[0]
    for i in range(1,len(li)):
        lc=gcd(lc,li[i])
    return lc

n=int(input('Enter number of elements : '))
l1=[]
while(n):
    n-=1
    l1.append(int(input('Enter number : ')))

print('Collective GCD is : ',gcdarr(l1))