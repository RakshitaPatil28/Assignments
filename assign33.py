#finding largest of three numbers
a=int(input("Enter a value to A:"))
b=int(input("Enter a value to B:"))
c=int(input("Enter a value to C:"))
if a> b:
    if a>c:
        print("C is largest")
    else:
        print("A is largest")
else:
    if b>c:
        print("B is largest")
    else:
        print("C is largest")
