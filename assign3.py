def calculate_electricity_bill(units):
    if units<=100:
        a=units*2
        print(f"Total charge is {a}")
    elif units<=200 and units>100:
        a= (100*2)+(units-100)*4
        print(f"Total charge is {a}")
    else:
        a= (100*2)+(100*4)+(units-200)*6
        print(f"Total charge is {a}")
    return a
units=int(input("Enter the number of units used:\n"))
calculate_electricity_bill(units)
