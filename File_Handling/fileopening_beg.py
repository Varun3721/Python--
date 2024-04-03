try:
    file_handler = open('myFile.txt', 'r')
    str1 = file_handler.read(6)
    print(str1)
    str2 = file_handler.read(10)
    print(str2)
    # this  is because the file pointer is pointing at 7 th so start by 7 th alphabet that is 's'

finally:
    file_handler.close()

    #file is a resource to a program as it is outside from program so make sure that if we use it we should close it also.
    #close all the resources when not are in used, so that the neccesary one can use it , so as not achieve starvation.
    #reading the file, opening and closing a file finally.
