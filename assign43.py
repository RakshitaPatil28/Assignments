#reverse a number
n=int(input("Enter a number:\n"))
rev=0
for i in range(len(str(n))):
#while n!=0:
    rev= rev * 10 + (n % 10)
    n= n//10
print(f"Reverse of the number is {rev}")
