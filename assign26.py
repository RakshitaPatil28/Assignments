dict={"Asha": "Python", "Ravi": "Data Analytics", "Neha": "AI"}
print("Student Names are:",dict.keys())
print("Enrolled courses are:",dict.values())
name=input("Enter the student name:\n")
if name in dict.keys():
    print("Student name exists")
else:
    print("Student Name not exists")
