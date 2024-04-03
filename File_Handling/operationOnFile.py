file=open('test.txt','r')

# print(file.name)
# print(file.mode)
# print(file.closed)
# print(dir(file))

#file.readline() gives string

line=file.readline()
print(line,end="")


line=file.readline()
print(line)
#
#
# print(type(line))


#file.readlines() gives list of strings,
# #but one thing to notice when i run along with
# #file.readline method the no. of print lines are two same as readline()
lines=file.readlines()
print(lines,type(lines))