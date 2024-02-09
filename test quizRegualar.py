# import re
#
#
# var = 'hello beautiful people'
#
# x = re.findall('pe.{3}e',var)
# print(x)

import re
str = 'kk@hl.com'
match = re.search(r'[\w-]+[\w-]+@[\w.-]+com', str)  #note this thing that one square bracket gives one word it could be of one letter or many
if match:
    print(match.group())
else :
    print('the email is not valid')

# from re import *
#
# print(match('(D|d)is(c|k)',"disc").group())

