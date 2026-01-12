#sum of first n natural numbers
n=int(input("Enter a number:\n"))
sum=0
for i in range(1,n+1):
    sum+=i
    print(sum) 
print ("Sum of n natural number is ",sum)
