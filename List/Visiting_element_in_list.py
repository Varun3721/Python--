list1=[3,2,4,5,6,7]
for x in list1:
    print(x,end="")
print("  ")

for i in range(len(list1)):
    print(list1[i], end=" ")
print(" ")

for i in range(len(list1)-1,-1,-1):
    print(list1[i], end=" ")

print(" ")

for i in range(-1,-(len(list1)+1),-1):
    print(list1[i], end=" ")

print(" ")

i=0
while(i<len(list1)):
    print(list1[i], end=" ")
    i=i+1