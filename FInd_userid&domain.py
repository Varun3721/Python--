email_id=input("enter your gmail id ")
'''li=email_id.split("@")
print(li)'''
atrate=email_id.find("@")
print("user name is ",email_id[:atrate])
print("domain name is ",email_id[atrate+1:])



#print("user name is ",li[0])
#print("domain name is ",li[1])