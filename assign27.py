#delivery distance categorizer
dist=int(input("Enter distance in km: "))
if dist <= 5:
    print("Local Distance")
elif dist >=6 and dist <20:
    print("City Distance")
else:
    print("Outstation Distance")
    
