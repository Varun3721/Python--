def closure(msg):
    def display():
        print('*'*11)
        print(msg)
        print('*'*11)

    return display


d=closure("Best Wishes ")
d()

#so here we are accessing a non local variable ;
#now lets relate it with caller class
#closure func means nested function ok
