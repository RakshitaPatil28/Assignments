#calculating grade
marks=int(input("Enter the Marks of the student:\n"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>50 and marks<=74:
    print("C")
else:
    print("Fail")
