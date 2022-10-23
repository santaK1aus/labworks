#11.12
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

n=int(input('Enter a number : '))
if(n<0): raise Exception('Cannot find square root of negative number')
else: print('Square root is ',sqrt(n,0,n))