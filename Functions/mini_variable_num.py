def minimum(*val,low_limit):

    if low_limit == None:
        mini = 0
        for i in range(len(val)):
            if val[i]<mini:
                mini=val[i]

        return mini
    else:
        mini=low_limit
        L=[x for x in val if x>=low_limit]
        for i in range(len(L)):
            if L[i]<mini:
                mini=L[i]
        return mini


value=minimum(1,2,3,4,-1,8,low_limit=2)
print("the minimum value as per low_limit is",value)


#def minimum(*val,low_limit)
# # if low_limit == None:
#
#
#         return min(val)
#     else:
#         mini=low_limit
#         L=[x for x in val if x>=low_limit]
#         return min(L)
