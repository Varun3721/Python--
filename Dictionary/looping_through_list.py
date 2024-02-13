dict1={101:'production',102:'onion',103:'pringles',104:'rabbit'}
for x in dict1:
    print(x)

for x in dict1:
    print(x,dict1[x])

for x in dict1:
    print(x,dict1.get(x))

print(dict1[102])
# print(dict1[109]) #so it gives error
print(dict1.get(109)) #so it will ignore it also you can print msg for wrong key
print(dict1.get(109,'invalid key'))

#keys()->> in form of list all keys
print(dict1.keys())
#values()
print(dict1.values())

#items()->> gives all (key,value) in as tuple form inside list or say gives list of tuples

print(dict1.items())

#for looping inside the items 
for x,y in dict1.items():
    print(x,y)