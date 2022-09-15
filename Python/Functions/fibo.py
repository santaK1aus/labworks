#9.5
def fibor(n):
    if n==1 or n==2:
        return 1
    return fibor(n-1)+fibor(n-2)

def fibos(n):
    a=0
    b=1
    for i in range(0,n):
        c=a+b
        a=b
        b=c
    return a

print('9th fibonacci number is :',fibos(9))