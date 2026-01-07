#intern data validation system
name= input("Enter your name\n")
age= int(input("Enter your age\n"))
emailid =input("Enter your email-id\n")
contact=input("Enter your contact number\n")
graduation=float(input("Enter your graduation percentage\n"))
if age>=18:
    if graduation>=60:
        if len(contact)==10:
            print("Intern Eligible for Internship")
        else:
            print("Contact must contain 10 digits")
    else:
        print("Graduation percentage should be more than 60")
else:
    print("Age must be greater than 18")

