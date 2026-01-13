#fibonacci series of first N numbers
def fib(n):
    a=0
    b=1
    print("Fibonacci Series:")
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c
n = int(input("Enter N: "))
fib(n)
