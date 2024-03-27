def outer():
    def inner():
        print("hello world")

    return inner


d=outer()
d()
c=outer() #so func return value stores in c that is inner
c()
