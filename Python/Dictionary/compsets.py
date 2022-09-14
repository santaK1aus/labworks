#8.13
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

even={i for i in range(2,11,2)}
comp=set()
for i in range(1,21):
    if not isPrime2(i):
        comp.add(i)

print(even,'\n',comp)
print('Is upper set :',comp.issuperset(even))
print('Is sub set :',comp.issubset(even))
print('Sum :',sum(comp))
print(all(even))