def func1(a,b,*args,c,**kwargs):
    print(kwargs,type(kwargs))



func1(4,56,64,3,2,"jackgfruit","last_args",c=98,v=543,o=643,l="og")

#so basically keyword variable arguments can make us pass variable length of keyword argument without taking
#tension that we need to put one or two or something else