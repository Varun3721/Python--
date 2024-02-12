#  S={expresion for item in iterable}
S=set()
print(S)
S.add(9)
print(S)
S={x for x in range(10)}
print(S)
A={x**2 for x in (1,23,4,5)}
print(A)
B={x**3 for x in {3,4,5,6}}
print(B)
#same you can do with list
S3={x for x in (10,5,7,8,12,3) if x%2==0}
print(S3)
S4={x for x in 'phTHon is the THEEE' if x.isupper()}
print(S4)
S5={x.upper() for x in 'phillipines'}
print(S5)

#now remember that SET can contain only immutable object
# S1={1,2,3,9,(9,39),[8,9]}
# print(S1)#UnHashable type:list
# #similarly if you tried to add set also
# S2={1,2,3,9,{9,39}}
# print(S2)  #TypeError: unhashable type: 'list'\\

#Just put immutable type members for SETS
#Yes, strings are immutable in Python. This means that once a string is created,
# its value cannot be changed. If you try to modify a string,
# Python will create a new string object with the modified value.
# The original string object will remain unchanged.