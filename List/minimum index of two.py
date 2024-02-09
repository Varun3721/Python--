fav1=['pizza','nuggets','hotdogs','noodles','pasta','burger']
fav2=['burger','hotdogs','noodles','pasta','nuggets','pizza']
index1=len(fav1)+1
index2=len(fav2)+1
for i in range(len(fav1)):
    j=fav2.index(fav1[i])
    if i+j<index2+index1:
        index2=j
        index1=i

print(fav1[index1])

