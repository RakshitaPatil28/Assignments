#factorial
n=int(input("Enter a number:\n"))
num=1
if n > 0:
   for i in range(1,n+1):
    num=num*i
print(f"Factorial of {n} is ",num) 

