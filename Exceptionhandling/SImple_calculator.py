class Calculatorchecker(Exception):
    pass

def evaluate(formula):
    f=formula.split()
    if len(f)<3:
        raise Calculatorchecker('The formula or expression typed by you is invalid ')

    opt1=f[0]
    opt2=f[1]
    opt3=f[2]

    if opt1=='+' or opt1=='-' or opt1=='*'or opt1=='/':
        raise Calculatorchecker("formula is wrongly typed like (a + b)")

    if opt2=='+' or opt2=='-' or opt2=='*' or opt2=='/':
        op1=int(f[0])
        op2=int(f[2])
        if opt2=='+':
            result=op1+op2
            return result
        elif opt2=='-':
            result=op1-op2
            return result

        elif opt2=='*':
            result=op1*op3
            return result

        else:
            result=op1/opt2
            return result

    else:
        raise Calculatorchecker('Invalid operator used Please check (+,-,*,/ )')


try:
    formula=input("enter the expression:- ")
    res=evaluate(formula)
except Calculatorchecker as msg:
    print(msg)
else:
    print(res)