def calculate_discount(price, customer_type):
    if price>0:
        if customer_type == 'regular':
            cost= print(price*0.05)
        elif customer_type=='premium':
            cost= print(price*0.15)
        elif customer_type== 'employee':
            cost=print(price*0.25)
        else:
            cost = print(price)
    else:
        print("Enter the appropriate price")
price=float(input("Enter the price:\n"))
customer_type=input("Enter the type of customer(regular/premium/employee):\n")
calculate_discount(price,customer_type)
