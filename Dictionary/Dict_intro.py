#so if you trying to create a dict
#dictinary is collection of hetrogenous key-value pair
D={}
print(type(D))
#so its not set as set is initialize by
S=set()
print(type(S))

#dic is a  collection of key-value pair
#pair or item or entry
#Note that you can take only immutable datatype for key while for value you can put any type
dic1={'abacus':'a calculator','bachelor':'unmarried person','cable':'strong rope'}
print(dic1['bachelor'])
#for add
dic1[109]=45
print(dic1)
#for update
dic1['abacus']=5678
print(dic1)
#for deleting key-value particularly
del dic1['cable']
print(dic1)

dic2={101:'smith',102:'mathew',103:'harry'}
for i in dic2:
    print(i)

for i in dic2:
    print(i,dic2[i])

