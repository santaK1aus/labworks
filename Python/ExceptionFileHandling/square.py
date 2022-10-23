#11.13

try:
    n=int(input('Enter a number : '))
    print(n,'^ 2','=',n**2)
except ValueError:
    print('Please enter numbers')