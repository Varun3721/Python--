# l1=[]
# for i in range(10):
#     l1.append(i)
#
# print(l1)
#
# #same can be achieved by list comprehension
# #l2=[expression for item in iterable]
# l2=[x for x in range(10)]
# print(l2)
#
# l3=[x**2 for x in range(8)]
# print(l3)
#
# #this braces() is tuple in which we are checking criteria %2==0
# l4=[x for x in (1,2,3,45,6,7,10) if x%2==0]
# print(l4)
#
# l5=[x.lower() for x in 'PYTHon']
# print(l5)



# l6=[x for x in 'ajdl-jsdf@gmail%' if x.isalnum()]
# print(l6)
#
# l7=input("enter names with space ")
# data=l7.split()
# print(data)
# #same stuff by list comprehension
# l8=[input("enter names with space in between ").split()]
# print(l8)

l10=[x for x in range(10) if x%2 == 0]
print(l10)
