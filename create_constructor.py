#Creating a class Employee with Constructor
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employee_details(self):
        print("Name of the Employee is ",self.name)
        print("Age of the Employee is ",self.age)
        print("Salary of the Employee is ",self.salary)
        print("Gender of the Employee is ",self.gender)
emp=Employee("Rakshita",21,25000,"Female")
emp.employee_details()
                
