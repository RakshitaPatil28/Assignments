#simple interest
def si(p,r,t):
    sim_int=p*r*t/100
    print("Simple Interest is ",sim_int)
p=int(input("Enter the Principal amount:"))
r=int(input("Enter the Rate of Interest:"))
t=int(input("Enter the Time in years:"))
si(p,r,t)
