dict1={101:'production',102:'onion',103:'pringles',104:'rabbit'}

dict2=dict1.copy()
print(dict2)
print(id(dict1[101]))
print(id(dict2[101]))
#so copy method is give shadow of the orignal dictionary only so that's why same object is reference
#so lets change the value for some key
dict2[103]="bringal"
print(dict1)
print(dict2)
print(id(dict1[103]))
print(id(dict2[103]))
#so now shallow of orignal is changed to some different object
#lets see #UPDAte() methhod
dict2.update({105:"madangles", 109:"tasty",1110:"hello"})
print(dict2)
dic3={99:"han",56:"fjdks"}
dict1.update(dic3)
print(dict1)
#setdefault() methods so this one is used for same as get method but by default if the value is not there
#it will add it in dictionary with default value None else you can put
print(dic3.setdefault(50))
print(dic3)
print(dic3.get(999))#so get method will not add in dictionary
print(dic3)
#fromkeys method for makind a dictionary from keys so all have same value
l3=[3,4,5,6]
dict9={}
dict9.fromkeys(l3,76)
print(dict9)
#pop
#popitem
#clear

