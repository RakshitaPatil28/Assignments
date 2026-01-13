#prime number with function
def prime_num(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        a="Prime Number"
    else:
        a="Composite Number"
    return a
n=int(input("Enter the number:\n"))
print(prime_num(n))
