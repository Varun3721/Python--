G=10

def fun2():
    G=9
    print(G)

fun2()

print("global",G)
def fun3():
    global G
    G=G+9
    print(G)

fun3()
print("outside")
print("modifying global G",G)

#can we modify a global var in function answer is no but forcefullly by using Global