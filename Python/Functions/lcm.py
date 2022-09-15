#9.3
def gcd(m,n):
    if m%n==0:
        return n
    return gcd(n,m%n)

def lcmarr(li):
    lc=li[0]
    for i in range(1,len(li)):
        lc=(lc*li[i])/gcd(lc,li[i])
    return lc

n=int(input('Enter number of elements : '))
l1=[]
while(n):
    n-=1
    l1.append(int(input('Enter number : ')))

print('Collective LCM is : ',lcmarr(l1))