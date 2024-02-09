password1=input("Enter your password ")
password2=input("Enter your confirm again ")
if password1==password2:
    print("Log in ")
elif password1.casefold()==password2.casefold():
    print("you need to be case sensitive check your confirm password")
else:
    print("password are not matching")
