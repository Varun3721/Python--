from re import *
x=r'^hell'
c=compile(x)
r=c.search('helloworld')
print(r.group())


y=r'orld$'
d=compile(y)
z=d.search("helloworld")
print(z.group())

# print(match('.+','\n').group())
print(match('.+','7849jfdkiskhfcn').group())
print(match('[.]+','dfsfhsdf').group())
