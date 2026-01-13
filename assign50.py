#palindrome
def pal(n):
    temp=n
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if temp==rev:
        print("Number is Palindrome")
    else:
        print("Number not is Palindrome")
n=int(input("Enter a number:\n"))
pal(n)
        
