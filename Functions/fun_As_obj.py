def display():
    print("Hello man what's up")


d = display
d()

p = display
p()

#so function is treated as objects as we are taking them in variable and calling them
def  display2(name):
    print(f'hello my name is {name}')

obj = display2
obj('varun')

#so here above we are using variable with arguments