list1=[8,3,2]
print(id(list1))
list1.append(9)
print(list1)
list1.append([[8,3],[9,9],'fgty'])
print(id(list1))
print(list1)
#append takes only 1 argument ok

#now lets check extend
list2=[9,3,56]
print(id(list2))
#list2.extend([[7,5,3],'iot'])

list2.extend([8,34,543])
print(list2)

#so by extend we can add multiple list elements inside list,  |&|  while append do only 1 element added to the list
#appending can be done by slicing also

list3=[45,43,2345]
list3[3:]=[76,98]
print(list3)