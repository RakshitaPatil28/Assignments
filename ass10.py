#Employee Bonus Evaluation System
Emp_name=input("Enter the name of the employee:\n")
salary=float(input("Enter the salary of the employee:\n"))
rate=int(input("Enter the performance rating of the Employee (1 - 5):\n "))
if rate == 5:
    bonus= salary*0.2
elif rate == 4:
    bonus= salary*0.15
elif rate == 3:
    bonus= salary*0.1
else:
    bonus=0
final_salary= salary+bonus
print("Employee Name is:",Emp_name)
print("Employee performance rating is:",rate)
print("Bonus offered to Employee is:",bonus)
print("Final Salary of the Employee is:",final_salary)

