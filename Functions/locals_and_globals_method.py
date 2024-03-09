a,b,c,d=10,23,45,65

def func(a=23,b=90,):
    b="inkput"
    print(locals())  #storing in form of dictionary of all variable which are local


func()
print(globals())
#print(locals())so for a global func itself as analogy all insider are local hahaaaa


# global variable have a local same variable and it is used very well
x = 12


def f1():
    x = 15
    print(x)


f1()
print(x)



