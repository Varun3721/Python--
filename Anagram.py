s1=input("enter the string ")
s2=input("enter the string2 ")
if len(s1)!=len(s2):
    print("not anagram")
else:

    for x in s1:
        if x not in s2:
            print("not anagram")
            break;
    else:print("anagram")
    print("bye")