#copy methods
a={4,5,6,7}
b=a.copy()
print(b)
#add method
a.add(10)
print(a)
#update methods for adding multiple element which are of form list, tuple,string etc.
a.update((1,2,3))
print(a)
b.update({3,9,8})
print(b)
b.update([111,234,12,456,47])
print(b)
a.update('pythonis ')
print(a)

#removing methods
#pop method but we don't know which element will be remove as it uses hash
a.pop()
print(a)
#discard method
a.discard('p')
print(a)
#a.remove(99990) so remove method will give keyerror if not found
# while discard will igonore if element not found

#print(a)
a.discard(9990)
print(a)
b.clear()
print(b)#clear will remove all elements

