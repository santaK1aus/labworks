#9.18
def mmin(a,b,c):
    max=a
    min=a
    if b>max and b>=c:
        max=b
    elif c>max:
        max=c
    if b<min and b<=c:
        min=b
    elif c<min:
        min=c
    print('Max is',max)
    print('Min is',min)

mmin(1,2,3)