try:
    a=int(input("enter the value first one "))

    try:
        b=int(input("enter the value second "))


        try:
            c=a//b

        except ZeroDivisionError as err:
            print(err)

    except ValueError as msg:
        print(msg)

except:
    print("value error")

