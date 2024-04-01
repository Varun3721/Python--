class AccountBalanceException(Exception):        #for inheriting exception base class
    pass


balance = 10000
def withdrawl(amnt):
    global balanceg
    balance -= amnt

    if balance<=5000:
        raise AccountBalanceException ('AccountBalanceException')

    else:

        print(balance)


try:
    amnt=int(input("enter the amnt you want to withdrawl "))
    withdrawl(amnt)


except AccountBalanceException as msg:
    print(msg)





