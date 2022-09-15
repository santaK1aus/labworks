#9.9
res=0

def add(m,n):
    return m+n

def sub(m,n):
    return m-n

def mul(m,n):
    return m*n

def div(m,n):
    return m/n

def exp(m,n):
    return m**n

fs={'+':add,'-':sub,'*':mul,'/':div,'^':exp}
ch=0
print('Add : +\nSub : -\nMultiply : *\nDivide : /\nExponent : ^')
ch=int(input('Enter value(-999 to exit) : '))
while(ch!=-999):
    op=input('Enter op:')
    res=fs[op](res,ch)
    print(' ==',res)
    ch=int(input('Enter value : '))