l1=[10,15,6,9,12,8,4]
l2=[14,6,19,4,7,10,11]
l3=[] #10,6,4
for x in l1:
    if x in l2:
        l3.append(x)

print(l3)

