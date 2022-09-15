#9.17
def isLeap(n):
    return (n%400==0) or (n%4==0 and n%100!=0)

print(isLeap(1700))