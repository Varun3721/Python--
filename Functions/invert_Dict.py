def invert(d):
    newd={}
    for k,v in d.items():
        newd[v]=k

    return newd

d1={"ajay":12,"varun":13,"raj":16,"abhay":19}

d2=invert(d1)
print(d2)