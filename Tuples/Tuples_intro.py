# # t=(10)
# # print(t)
# # print(type(t))
# #
# # #so give comma always for making it as tuple
# #
# # t=(10,)
# # print(t)
# # print(type(t))
# # tu=tuple(((23,45,45),(45,65,45),(5,6,'er')))
# # print(tu)
# #
# # tup=(1,2,3,499,(4,3),6,6)
# # print(tup)
# # print(type(tup))
# #
# # #packing
# #
# #
# # t1=1,2,3,4
# # print(t1)
# # print(type(t1))
# # # and unpacking
# # a,b,c,d=t1
# # print(a)
# # print(b)
# # print(type(a))
# # #so unpacking can be done on string as well as tuple also list as well
# a,b,c='sky'
# print(a)
# print(b)
# print(type(c))
#
# l=[2,3,4]
# a,b,c=l
# print(a)
# print(b)
# print(type(c))
#
# #if we give less no of variables
# ty=1,2,3,4,5
# # a,b,c=ty
# # print(ty)
# a,b,*c=ty
# print(a)
# print(b)
# print(c)
# print(type(c))
# print(type(a))

yes=(1,2,35,43,23)
a,*b,c=yes
print(a)
print(b)
print(c)
print(type(b))
print(type(a))
#as pointer shows that it is list only
#one more thing an empty tuple is of no use ok



