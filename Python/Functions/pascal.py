#9.6
def pascalt(n):
    l1=[1]
    for i in range(1,n+1):
        l2=list(l1)
        print(' '*(n-i),end='')
        print(' '.join([str(s) for s in l1]))
        for i in range(1,len(l2)):
            l1[i]=l2[i]+l2[i-1]
        l1.append(1)

pascalt(6)