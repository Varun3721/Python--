# l=[]
# for i in range(5):
#     data=int(input("enter no. of hrs you give for each day of the 5 day week "))
#     l.append(data)

l= [int(x) for x in input("enter the hrs per day , seprated by spaces ").split()]
print(l)




# total_hrs=0
# for i in range(len(l)):
#     total_hrs+=l[i]
total_hrs=sum(l)


hr_wages=int(input("enter the hr wages "))
total_salary=total_hrs*hr_wages

print(total_salary)

