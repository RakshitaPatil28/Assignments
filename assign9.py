#Course Fee Billing System
course=input("Enter the course name (Python/Data Analytics/AI)\n")
if course== "python" :
    fee=5000   
elif course == "data_analytics":
    fee=8000    
elif course == "AI":
    fee=12000
else:
    print("Choose the specific course(Python/Data Analytics/AI )")
student=input("Are you a student?(yes/no):\n")
early=input("Are you early registered? (yes/no):\n")
dis=0
if student=="yes":
    dis= dis+(fee*0.1)
if early=="yes":
    dis=dis+(fee*0.05)
final_amt=fee-dis
print("Course name is ", course)
print("Original Fees of the course is ",fee)
print("Discount offered is ", dis)
print("Final Payable Amount of the course is ",final_amt)
