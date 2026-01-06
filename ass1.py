def check_intern_eligibility(age,percentage) :
    if age>=18 and percentage>=60:
        reason= print("Eligible as intern is satisfied with all circumstance")
    else :
        reason= print("Not Eligible as intern is under age of 18 and having lessthan 60%")
    return reason
def main():
    check_intern_eligibility(age,percentage)
age=int(input("Enter the age:"))
percentage=float(input("Enter the percentage:"))
if __name__ =="__main__":
    main()
