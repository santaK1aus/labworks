#9.4
def facts(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            print(i,'is a factor')
            f+=1
    print(n,'has',f,'factor'+('','s')[f>1])

inp=int(input('Enter a value : '))
facts(inp)