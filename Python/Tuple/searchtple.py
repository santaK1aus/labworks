#7.7
def lSearch(t1,val):
    for i in range(0,len(t1)):
        if t[i]==val:
            return i
    return -1

def bSearch(t1,val):
    lb=0
    ub=len(t1)-1
    while(lb<=ub):
        mid=(lb+ub)//2
        if(val<t1[mid]):
            ub=mid-1
        elif(val>t1[mid]):
            lb=mid+1
        else:
            return mid
    return -1

t=tuple(i for i in range(0,50,4))
print(t)
print('1.Linear Search\n2.Binary Search\nEnter choice and value')
ch=int(input())
val=int(input())
pos=-1
if(ch==1):
    pos=lSearch(t,val)
elif(ch==2):
    pos=bSearch(t,val)
else:
    print('Wrong Input')
    exit()
if(pos!=-1):
    print('Found at',pos+1)
else:
    print('Not Found')