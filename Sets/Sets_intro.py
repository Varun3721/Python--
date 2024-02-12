#Hetrogenous
#Unordered so can't used slicing or indexing
#No duplicates
#Growable.

T={"jak","smith",3,4,5,7,8,6}
print(T)#as unordered don't expect you see them in same ordered as you mentioned

#create set by set method
T1=set((1,2,3,"jack",2,3,3))
print(T1)

s3=set(('python','el'))
print(s3)
s4=set('pythOn')
print(s4)

#so One thing is clear the indices is not preserved in Sets

#sets are growable means mutable but methods are different a bit

l={1,34,35,44,54,65}
l.discard(34)
l.add(66)
print(l)

print(len(l))

