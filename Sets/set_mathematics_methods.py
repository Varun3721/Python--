#union
a={1,2,3,4,5,7}
b={6,7,5,9,98,45}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
#print(a.symmetric_difference(b))
#this update makes the a set change to this symmetric one

#a.symmetric_difference_update(b)
a.intersection_update(b)
print(a)

a={2,3,4,5,6,7}
b={2,3,4}

#issubset
#issuperset
#isdisjoint methods just like sets of mathematics all stuff adds here
print(b.issubset(a))
print(a.issuperset(b))
c={3,4,5}
d={6,7,8}
print(c.isdisjoint(d))

#for knowing all sets methods
print(dir(set))