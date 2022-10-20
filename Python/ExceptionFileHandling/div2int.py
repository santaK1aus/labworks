#11.1
try:
    a=int(input('Enter 2 values : '))
    b=int(input())
    c=a/b
    print(a,'/',b,'=',c)
except ValueError:
    print('Please Enter integer values')
except ZeroDivisionError:
    print('Division by Zero not possible')