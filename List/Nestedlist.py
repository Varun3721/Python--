# l=[1,2,['a','b',['c','d']],30,40]
# print(l)
#
# print(l[2][1]) #b
# print(l[2][2][1])  #d

#now lets do matrix addition 3*3 vali do
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
c=[]
for i in range(3):
    s=[]     #for one row
    for j in range(3):
        s.append(a[i][j]+b[i][j])

    c.append(s)


print(c)
