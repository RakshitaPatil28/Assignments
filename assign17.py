#identity operator
a=int(input("Enter a number:\n"))
b=int(input("Enter another number:\n"))
c=a
d=a is b
print("Result using is operator is :",d)
e=a is not b
print("Result using is not operator is :",e)
f=c is a
print("Result of 'c is a' is: ",f)
