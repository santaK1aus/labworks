#10.2
def add(*args):
    sum=0
    for arg in args:
        sum+=arg
    return sum

def sub(*args):
    sum=0
    for arg in args:
        sum-=arg
    return sum

def mul(*args):
    sum=1
    for arg in args:
        sum*=arg
    return sum

def div(*args):
    sum=args[0]
    for arg in args[1:]:
        sum/=arg
    return sum