dic1=dict()
print(dic1)
dic1['apple']='Red'
dic1[2]='Two'
print(dic1)

for x in range(1,6):
    dic1[x]=x**2

print(dic1)

#note that for key (2) we have updated the previous 2:Two so dictionary are mutable
#second way to make dictionary is

#2nd way dict((iterable pair))
dict2=dict(((1,2),('two',2),(5,'five'),('hello',64)))
print(dict2)

dict3=dict(('ab','cd','ef'))
print(dict3)

dict4=dict(([2,3],[45,43],['yes',2],['apple','two']))
print(dict4)

#3rd way dict(zip(iterable,iterable))
L1=[1,2,3]
l2=['one','two','three']
dcit=dict(zip(L1,l2))
print(dcit)
#by using set also
L1=[1,2,3]
l2={'one','two','three'}  #here value will be of no order as sets are used
dcit=dict(zip(L1,l2))
print(dcit)

dict5=dict(zip([1,2,3],{102,2029,2829,2829,23456}))




