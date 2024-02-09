itemname=input("enter item name")
price=input("enter the price ")
totallen=len(itemname)+len(price)
dots="."*(25-totallen)


print(itemname+dots+price)