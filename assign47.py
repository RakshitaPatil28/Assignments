#factorial of number
def fact(n):
    if n>0:
        num=1
        for i in range(1,n+1):
            num=num*i
    print("Factorial of number is ",num)
n=int(input("Enter the number:\n"))
fact(n)


        
