birthdays={'sachin':"23/02/2000",'varun':"21/12/2000",'naveen':"23/03/2001"}
birthd=input("enter you name ")
print(birthdays.get(birthd,'invalid name'))

if birthd  in birthdays:
    print(f"Mr/Mrs {birthd} was born on {birthdays[birthd]}")
else:
    print("wrong name entered")