file=open('modefile1.txt','a')

#firstly add
# file.write('hello how are you varun\n')
# file.write('this is file mode\n')
# file.write('check it out ok\n')

# file.write('lets add some more stuff\n')
# file.write('bsr add some varun\n')


file1=open('modefile1.txt','r+')
str1=file1.read(10)
print(str1)
str2=file1.write('pm k vaade')