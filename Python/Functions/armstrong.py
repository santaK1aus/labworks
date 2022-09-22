#9.21
def isArmstrong(n):
    sum=0
    length=len(str(n))
    t=n
    while(t>0):
        d=t%10
        t=t//10
        sum+=d**length
    return (sum==n)

print(isArmstrong(153))