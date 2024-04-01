print("before try block")

try:
    a=int(input("enter first no. "))
    b=int(input("enter second no. "))
    c=a//b
    #print(c) learn below at the last about it.
    print("try block executed fully")

except ZeroDivisionError as err:
    print(err)

else:
    print(c)
    print("This else part execution shows that our try block fully executed .")


#one thing to Learn here is that in Try block:-
#we should write only those lines which can cause exception
#that's why we have not written print(c) inside try block
#as it will not be sensible so we put it in else part