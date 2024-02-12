S={1,2,3,4,5,6,7,8,9,10}
a={1,2,3,5,7}
b={5,7,9,10,11}
print(a|b)#Union
print(a&b) #intersection
print(a-b) #difference
print(a^b) #disjoint
print(a<S) # proper subset
print(a<=S) #subset equal to
print(S>a) # proper  superset
print(S>=a) #super set equal to
print(S>=b)#same as above
print(S==S) #equal to sets
print(S!=a)#not equal to sets
print(2 in S) # if present in set

print(11 not in S)
a|=b
print(a)
