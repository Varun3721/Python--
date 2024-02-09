l1=[56,1,2,3,4,5,65,4,7,9,4]
print(id(l1))
print(id(l1[0]))
print(l1.index(4))
print(l1.index(4,4))
print(l1.index(4,7))
#print(l1.index(4,4,5))

#count method just count the no. of occurence ok
print(l1.count(4))
print(l1.count(567))
#reverse method reverse the orignal list
l1.reverse()
print(l1)
print(id(l1))
print(id(l1[0]))
#sort method
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l2=['yy','jj','mm','BB','aa','ZZ']
l2.sort()
print(l2)#according to ascii value

l2.sort(key=str.lower)
print(l2)
#global sorted method based on ascii only
print(sorted(l2))
#sorted function gives just modified list but the orignal list is same only
