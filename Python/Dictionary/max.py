#8.5,6,7
dict1={'A':6,'B':2,'C':67,'D':-1,'E':5}
print('Max :',max(dict1.values()))
print('Min :',min(dict1.values()))
d2={'F':45,'G':43,'H':89,'A':25}
d3=dict1
for k,v in d2.items(): #concatenating 2 dicts
    if k in d3:
        if type(d3[k]) is not list:
            d3[k]=[d3[k]]+[v]
        else:
            d3[k].append(v)
    else:
        d3[k]=v
print(d3)