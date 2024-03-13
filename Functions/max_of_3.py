def maxim(a,b,c):
    if a>b and a>c:
        print(a ,34,"is greater")

    elif(b>c):
        print(b)
    else:
        print(c)

a=int(input("enter first no. "))
b=int(input("enter second no. "))
c=int(input("enter third no. "))
maxim(a,b,c)
