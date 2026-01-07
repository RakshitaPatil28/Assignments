import re
def check_password_strength(password) :
    a=b=c=False
    if len(password)>=8:
        print ("Password has more than 8 characters")
        a=True
    if any(char.isdigit() for char in password):
        print("Password has digit ")
        b=True
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("password has special character ")
        c=True
    
    if a==True and b==True and c==True:
        res=print("Strong Password")
    else:
        res=print("Weak Password")
    
    

check_password_strength('rakshita@2005' )


