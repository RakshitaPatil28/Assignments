#sum of digits of a number
n=int(input("Enter a number:\n"))
digit=add=0
while n>0:
    digit=n%10
    add+=digit
    n=n//10
print("Sum of digits of number is ",add)
               
