

with open('my.data','rb') as file1:
    str=file1.read(2)
    print(str) #for getting string words only use .decode()

    file1.seek(3,1)
    print(file1.read(1))      #f will come

    #print(file1.tell())

    file1.seek(-4,2)
    print(file1.read(2).decode())

    file1.seek(-5,1)
    print(file1.tell())
    print(file1.read(1))
