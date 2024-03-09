#iterator


l=[1,2,3,4,5]

itr=iter(l)
# for i in range(3):
#     print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


#Have created a customized iterator known as generator

def gene():
    L=['sun','mon','tue','wed','thr','frid','sat']
    i=0
    while True:
        x=L[i]
        i=(i+1)%7
        yield x

g=gene()
for i in range(10):
    print(next(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

