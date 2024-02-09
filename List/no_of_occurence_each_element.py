l=['a','b','c','d','e','a','b','e','b','d','b','e','a']
# l1=[]
# l2=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# for i in l1:
#     count=0
#     for j in l:
#         if i == j:
#             count+=1
#     l2.extend((i,count))
#
# print(l2)

# modified way
result=[]
for x in l:
    if x not in result:
        result.append(x)
        result.append(l.count(x))
print(result)


