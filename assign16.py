#checking student name in list
lst=["Ashwini","Kratika","Rakshita","Srushti"]
name=input("Enter the student name:\n")
if name in lst:
    print("Student name exists in Attendance list!!")
if name not in lst:
    print("Student name not exists in Attendance list!!")


#verifying product availability
stock=('Book','Pen','Laptop','Mobile','Table Lamp','Pencil')
prod=input("Enter the product name:\n")
if prod in stock:
    print("Product is available in inventory.")
else:
    print("Sorry!! Product is out of stock.")
