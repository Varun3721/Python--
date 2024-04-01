def division(a,b):
    try:
        c=a//b
        return c
    except:
        raise ZeroDivisionError
    finally:
        print("final block got executs")


#z=division(10,0)
z=division(10,5)
print(z)

#so finally will execute irrespect of exception will come or not come
#and why to use them
