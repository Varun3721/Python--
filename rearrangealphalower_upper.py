str1=input("enter mix string of both lower and upper case alphabets ")
lower=""
upper=""
for x in str1:
    if x.isupper():
        upper=upper+x
    else:lower+=x
print(lower+upper)