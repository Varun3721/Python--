from zipfile import *

file=ZipFile('images.zip','r')

file.extractall()
file.close()