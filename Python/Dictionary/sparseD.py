#8.15
li=[[0,0,1],[0,1,0],[1,0,0]]
print(li)
id={}
for r in range(len(li)):
    id[r]={}
    for c in range(len(li[r])):
        id[r][c]=li[r][c]

print(id)