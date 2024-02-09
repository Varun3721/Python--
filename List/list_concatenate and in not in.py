list1=[1,2,3]
print(id(list1))
list1.extend([9,4,5])
print(list1)
list2=[1,2,3]
print(id(list2))
list2=list2+[9,4,5]
print(list2)
print(id(list2))
print(id(list1))

#so the function of concatenates makes different addrence or say point to different object