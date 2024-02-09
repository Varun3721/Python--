L1=[4,5,6,7,8]
print(id(L1))
L1.insert(0,10)
print(L1)
print(id(L1))
#now by using slice also
#lets insert 67 after 5
L1[3:3]=[67]
print(L1)
L1[0:0]=['uioo']
print(L1)

#copy method learn

l2=[8,3,2,1]
print(id(l2[0]))
l3=l2.copy()
print(l3)
print(id(l3[0]))