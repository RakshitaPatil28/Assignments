#login authentication system
username = "dd_admin"
password = "dd@2025"
user=input("Enter username\n")
pswd=input("Enter password\n")
if user==username and pswd==password:
    print("Valid credentials, Login Successful")
else:
    print("Invalid credentials, Access Denied")
