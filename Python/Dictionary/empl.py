#8.19
employees={'Amar':{'Age':25,'Addr':'Kolkata','Salary':25000},'Akbar':{'Age':27,'Addr':'Mumbai','Salary':29000}}
for key in employees.keys():
    print('Name :',key)
    for info in employees[key]:
        print(info,':',employees[key][info])
    print()