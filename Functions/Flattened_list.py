def flattened(L):
    for e in L:
        if hasattr(e,'__iter__'):
            yield from flattened(e)

        else:
            yield e










L=[1,2,[3,4,[5,6],7],8]
f=flattened(L)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
