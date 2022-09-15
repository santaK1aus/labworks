#9.2
d=0.00001

def sqrt(n,i,j):
    mid=(i+j)/2
    sq=mid*mid
    if(sq == n or abs(sq-n)<d):
        return mid
    elif(sq<n):
        return sqrt(n,mid,j)
    else:
        return sqrt(n,i,mid)

inp=int(input('Enter a number : '))
print(sqrt(inp,0,inp))