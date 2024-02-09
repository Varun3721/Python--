code=['._','_...','_._.','_..','.','.._.','__.','....','..','.___']
decode=""
word=input("enter the word for decoding ")
for x in word:
    indec=ord(x)-ord('a')
    decode+=code[indec]+" "

print(decode)


