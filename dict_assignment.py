#dictionary Assignment
stud={}
def add_detail():
    n=int(input("Enter the number of students:"))
    for i in range(n):
        name=input("Enter the name of the student:")
        marks=int(input("Enter the marks of the student:"))
        stud[name]=marks
    print("Student Details Added Successfully!!")
    def update_details():
        name=input("Enter the student name:")
        if name in stud:
            marks=int(input("Enter the marks:"))
            stud[name]=marks
            print("Student Marks Updated Successfully!!")
        else:
            print("Student Name Not Found!!")
    
    def report():
        if not stud:
            print("Student Details Not Found!")
        else:
            for name,marks in stud.items():
                print(name,":",marks)
    update_details()
    report()
add_detail()
#update_details()
#report()
