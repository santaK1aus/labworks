#8.16,17
d1={i:i**3 for i in range(1,10,2)}
print(d1)
d2={v:k for k,v in d1.items()}
print(d2)