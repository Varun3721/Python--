#adding a function

def add(a,b):
    c=a+b

    return c

k=add(9,9)
print(k)

sumed=lambda a,b:a+b

print(sumed(9,8))

greater=lambda a,b: a if a>b else b
print("greater is ",greater(9,34))