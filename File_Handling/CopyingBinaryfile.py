file=open('Money1.jpeg','rb')

data=file.read()

copyFile=open('Money2.jpg','wb')  #as we are encoding - decoding media file that is only possible in binary .
copyFile.write(data)

file.close()
copyFile.close()