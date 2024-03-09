#Variable arguments used basically to give *args as a tuple.

def fun1(*args):
    print(args)
    print(type(args))

fun1()
fun1(5,4,3,"jack")

def fun2(a,b,*ar):
    print(a,b,ar)

#fun2()
fun2(1,2,3,4,"jackfruit")


def fun3(*arg,a,b):
    print(a,b,arg)

#fun3(4,5,6,7,8,4)# fun3() missing 2 required keyword-only arguments: 'a' and 'b'
fun3(9,34,5,a="jack",b=9)

