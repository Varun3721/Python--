#sets are stored in the form of hash

#h(x)%16=results give the index and then if element already present we give a list to it
#suppose you make a set {10,20,30,40,50}
#it will store in {50,20,40,10,30}

#as 10%16 gives 10 so it will store at 10th
#while 50%16 gives 2 as remainder ( indices)

S={10,20,30,40,50}
print(S)
#lets add 60 a/q to calculation 60%16 gives 12  so it will be after 10 as 10 is on 10th indices
S.add(60)
print(S)
#add 18 as it will store in 18%16=2 indices
#store like 50->18
S.add(18)
print(S)
#Note this Hash function will change according to the size of the distribution of array
# as if any one indices list size got increase it (x->y->z->a)like that
#surely the hash function will modify to make it distribute.
    
