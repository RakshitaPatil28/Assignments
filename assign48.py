#largest of three numbers using function
def large(a,b,c):
    if a> b:
        if a>c:
            print("A is largest")
        else:
            print("C is largest")
    else:
        if b>c:
            print("B is largest")
        else:
            print("C is largest")
a=int(input("Enter a value to A:"))
b=int(input("Enter a value to B:"))
c=int(input("Enter a value to C:"))
large(a,b,c)

