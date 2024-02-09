str=input("enter the sentence you want removal of punuation ")
punctuation='''{}[]-.@,*&^$#/""!()'''
str1=""
for x in str:
    if x not in punctuation:
        str1+=x

print(str1)
