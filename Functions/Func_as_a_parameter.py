def outer():
    print("this is called by another func as arguments ")



def func(d):
    d()

func(outer)


#another example

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def func(f,a,b):
    f(a,b)

func(add,5,6)
func(sub,9,4)