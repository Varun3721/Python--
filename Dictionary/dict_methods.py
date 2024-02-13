dict1={101:'production',102:'onion',103:'pringles',104:'rabbit'}

dict2=dict1.copy()
print(dict2)
print(id(dict1[101]))
print(id(dict2[101]))
#so copy method is give shadow of the orignal dictionary only so that's why same object is reference

