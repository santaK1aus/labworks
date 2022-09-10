#8.22
menu={'Sandwich':13,'Chicken':15,'Tea':5,'Coffee':10,'Boiled Egg':10,'Omlette':16}
for k,v in menu.items():
    print(k,'\t',v)

net=0
ch=input('Enter order(-1 to exit) : ')
while(ch!='-1'):
    if ch in menu:
        print('Ordered',ch)
        net+=menu[ch]
    else:
        print('Please order from menu!')
    ch=input('Enter order : ')

print('Net Bill : ',net)