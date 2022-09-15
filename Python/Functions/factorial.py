#9.1

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def factn(n):
    sum=1
    for i in range(n,0,-1):
        sum*=i
    return sum

def main():
    inp=int(input('Enter a number : '))
    print('Factorial is :',factn(inp))

if __name__=="__main__":
    main()