#so as we know tuple is immutable so it has very less methods

#comprehension check
# t=(x for x in range(10))
# print(t)
t=tuple(x for x in range(10))
print(t)
t1=t=(*(x for x in range(10)),)
print(t1)
t2=(*(x for x in range(0,11,2)),)
print(t2)
print(type(t2))

t3=(*(x for x in 'python'),)
print(t3)
t4=(*(x for x in "PyThon" if x.isupper()),)
print(t4)
t5=(*(x**4 for x in range(8)),)
print(t5)

t7=(2,3,4,5,6,3,2)
print(t7.count(3))
print(t7.index(3,2,6))

