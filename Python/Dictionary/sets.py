#8.12
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

odds={i for i in range(1,21,2)}
prime={2}
c=0
i=3
while c<9 :
    if isPrime2(i):
        prime.add(i)
        c+=1
    i+=1

print('Odd set :',odds)
print('Prime set :',prime)
print('Union :',odds.union(prime))
print('Intersection :',odds.intersection(prime))
print('Difference :',odds.difference(prime))
print('Symmetric difference :',odds.symmetric_difference(prime))