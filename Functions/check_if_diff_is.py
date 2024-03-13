def diff(a,b):
    c=abs(a-b)
    if c<5:
        print("True")
    else:
        print("False")


a=int(input("enter the no. first "))
b=int(input("enter the no. second "))
diff(a,b)