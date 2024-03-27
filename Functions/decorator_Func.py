                                                               #passing Function as parameter
                                                               #Nested Function calling  parameter function
                                                               #return Nested function
                                                               #@ for decoraion

def decorator(my_fun):
    def wrapper(msg):
        print("*"*10)

        my_fun(msg)

        print("*"*10)

    return wrapper

@decorator
def display(msg):
    print(msg)

display("third way of calling")

# display=decorator(display)
# display("yash")
#
# w = decorator(display)
# w('varun')


