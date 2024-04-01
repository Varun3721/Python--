class NegativeAgeError(Exception):


    def __str__(self):
        return 'Negative age is not allowed'


def age_checker(age):
    if age<0:
        raise NegativeAgeError
    if age>=0 and age<13:
        print("kid")
    elif age>13 and age<19:
        print("teen")

    elif age>=19 and age<50:
        print("young")

    else:
        print("Old")




try:
    age=int(input("enter the age of yours "))
    age_checker(age)


except NegativeAgeError as msg:
    print(msg)

except ValueError as err:
    print(err)