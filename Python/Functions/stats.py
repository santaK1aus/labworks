#9.28
def statistics(n):
    avg=(n+1)/2
    if n%2==0:
        print('Medians are',n/2,',',n/2+1)
    else:
        print('Median is',n//2+1)
    print('Modes are :')
    for i in range(1,n+1):
        print(i,end=' ')
    return avg

print(statistics(25))