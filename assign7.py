#Employee salary calculation system
employee_name= input ("Enter Employee Name\n")
employee_id = input ("Enter Employee ID\n")
basic_salary=float(input("Enter Employee Basic Salary\n"))
if basic_salary>0:
    HRA=basic_salary*0.2
    DA= basic_salary*0.1
    PF=basic_salary*0.12
    print("Basic salary of Employee",basic_salary)
    print("House Rent Allowance of Employee is ",HRA)
    print("Dearness Allowance of Employee is ", DA)
    print("Provident Fund of the Employee is ",PF)
    net_salary=basic_salary+HRA+DA-PF
    print("Net salary of the Employee is ",net_salary)
else:
    print1("Enter valid basic salary and basic salary must be greater than zero")
    
