# l=[3,5,9,8,3,4,5,9,6,3,7,2]
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
#
# print(l1)

#can we make unique list initself only

l=[3,5,9,8,3,4,5,9]
print(len(l))

for i in range(len(l)-1,-1,-1):
    if l[i] not in l[:i]:
        i+=1

    else:del l[i]
print(l)

i=0
while i<len(l):
    if l[i] not in l[:i]:
        i+=1

    else:
        del l[i]

print(l)

#so we have to use reverse for loop range as it can create out of range error as we are