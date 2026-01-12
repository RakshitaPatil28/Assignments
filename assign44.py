#fibonacci series
n=int(input("Enter a number:\n"))
if n<0:
    print("You have entered invalid number!!")
if n>0:
    a=0
    b=1
    print("Fibonacci Series is")
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c

