def checker(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
            upper+=1
        else:lower+=1

    print("upper case are ",upper)
    print("lower case are ",lower)



string="aBcHDksjdkJJJ"
checker(string)