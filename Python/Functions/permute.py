#9.14,15
from factorial import fact

def permute(n,r):
    return fact(n)/fact(n-r)

def combi(n,r):
    return permute(n,r)/r

