def check_attendance(login):
    if login <= 9.30:
        res=print("present")
    elif login > 9.30 or login <= 10.00 :
        res=print("late")
    else:
        res=print("absent")
    return res
time=float(input("Enter the login time:\n"))
check_attendance(time)   

