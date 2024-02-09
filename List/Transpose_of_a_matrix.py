l=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l1=[]
for i in range(4):
    s=[]
    for j in range(3):
        s.append(l[j][i])
    l1.append(s)

print(l1)