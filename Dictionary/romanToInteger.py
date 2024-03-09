roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
romanNumb=input("enter the roman number you want to convert ")  #IXXX

sum=0
i=0
while i<len(romanNumb):
    if i+1<len(romanNumb) and roman[romanNumb[i]]<roman[romanNumb[i+1]]:
        sum+=roman[romanNumb[i+1]]-roman[romanNumb[i]]
        i+=2

    else:
        sum+=roman[romanNumb[i]]
        i=i+1

print(sum)