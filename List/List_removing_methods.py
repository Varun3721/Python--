#pop
l1=[3,4,5,6,765,5677]
# l1.pop()
# print(l1)
# l1.pop(1)
# print(l1)
#del keyword
del l1[2]

print(l1)
del l1[3:4]
print(l1)

#remove method
l3=[23,44,43,2,1,44,5,6]
l3.remove(44)
print(l3)
#so first occuring will be remove
#Clear method
l4=[3,2,5,67,654]
#l4.clear()

#or by using slicing
l4[:]=[]
print(l4)
