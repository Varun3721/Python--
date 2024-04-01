L=[10,23,45,43,56,65]

try:
    index = int(input("enter any index "))

    print(L[index])
    print("end of try block")  #statement 3rd so if above statment gives exception it will not excecute ok

except (IndexError,ValueError) as msg: #here error type msg will reflect in msg and then all goes inside
    print(msg)

except:
    print("for all other type of errors")


print("terminated gracefully")