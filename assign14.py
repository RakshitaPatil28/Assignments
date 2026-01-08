#updating wallet balance
wallet= input("Enter the reason (cashback/purchase):\n")
bal=int(input("Enter the balance amount in the account:\n"))
if wallet=="cashback":
    amt=int(input("Enter the cashack amount:"))
    bal+=amt
    print("Total Amount After Adding Cashack Amount is :",bal)
if wallet=="purchase":
    amt=int(input("Enter the amount you have purchased:"))
    bal-=amt
    print("Total Amount Remained After Purchasing is:",bal)

    
#incrementing score of the game
score=int(input("Enter the initial stage score:\n"))
print("The intial stage score of the game is :",score)
sco=0
sco+=score
sco1=int(input("Enter the score\n"))
sco+=sco1
print("The total score of the game is:",sco)

#Reduce stock
stock=int(input("Enter the number of stock present in initial stage:\n"))
sale=int(input("Enter the number of stock sold:\n"))
stock-=sale
print("Stock present after reducing:\n",stock)



