#9.25
from math import sqrt
def area(a,b,c):
    s=(a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

print(area(3,4,5))