#5th method
l2=['a','b','c']
for i in enumerate(l2):
    print(i)
#dict1=dict(enumerate(iterable))
l1=['a','b','c']
dict1=dict(enumerate(l1))
print(dict1)

#6th
#dicti={exp:exp for item in iterable}
l3={x:x**2 for x in range(1,6)}
print(l3)

#7th
#dic7=dict((exp,exp)for item in iterable))

dict7=dict((x,x**2)for x in range(1,6))
print(dict7)

#8th
#dict8=dict((x,y)for x,y in zip(iterable,iterable))
L1=[1,2,3]
L2=['a','b','c']
dict8=dict((x,y) for x,y in zip(L1,L2))
print(dict8)

#9th dict9={item for item in enumerate(iterable)}

dict9={x:y for x,y in enumerate(L2)}
print(dict9)





