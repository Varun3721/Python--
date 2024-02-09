string1=input("enter a string for checking palindrome ")
size=len(string1)
string2=string1[::-1]
if string1==string2:
    print("the given string is palindrome ")
else:
    print("the given string is not a palindrome")