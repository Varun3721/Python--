import zipfile
from zipfile import *

file=ZipFile('images.zip','w',ZIP_DEFLATED)

file.write('money1.jpeg')
file.write('money2.jpg')

file.close()
