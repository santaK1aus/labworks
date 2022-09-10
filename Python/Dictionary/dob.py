#8.21
dobs={'Amar':'2001/08/15','Akbar':'2002/01/08','Anthony':'2001/12/30'}
for v in sorted(dobs.values()):
    print(list(dobs.keys())[list(dobs.values()).index(v)],v)
inp=input('Enter name : ')
if inp in dobs:
    print('DOB :',dobs[inp])
else:
    dobs[inp]=input('DOB not found, enter DOB (YYYY/MM/DD) : ')
    print(dobs)