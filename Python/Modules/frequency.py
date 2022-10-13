#10.14
import random

freq={1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(0,6000):
    y=random.randrange(1,7)
    freq[y]+=1

for k,v in freq.items():
    print(k,'->',v)