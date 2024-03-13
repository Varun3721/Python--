def pangram(phrase):
    letter = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z'}
    phr=set(phrase)
    if len(phr)>=len(letter)+1:
        return True

    else:return False
seter="The quick brown fox jumps over the lazy dog."

r=pangram(seter)
print(r)



