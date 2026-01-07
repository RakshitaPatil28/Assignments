def calculate_discount(price, customer_type):
    if price>0:
        if customer_type == 'regular':
            cost= (price*0.05)
            print("Final price is ",price-cost)
            print("Discount amount is",cost)
        elif customer_type=='premium':
            cost= (price*0.15)
            print("Final price is ",price-cost)
            print("Discount amount is",cost)
        elif customer_type== 'employee':
            cost=(price*0.25)
            print("Final price is ",price-cost)
            print("Discount amount is",cost)
        else:
            print("Enter the valid customer type")
    else:
        print("Enter the appropriate price")
price=int(input("Enter the price:\n"))
customer_type=input("Enter the type of customer(regular/premium/employee):\n")
calculate_discount(price,customer_type)
