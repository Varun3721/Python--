from re import *

# print(match("ab","abvc").group())
# #print(match("[abc]","db").group())
# print(match("[abc]","cacbc").group())
#
# print(match("[abc]+","abnnc").group())
# print(match("[abc]{8}","abbcbcbcc").group())
#

# print(match("[a-z]+","pythonkijai").group())
# print(match("[a-z]+","jaiho").group())
#
# #print(match("[^a-z]+","letsee").group())
# print(match("[^a-z]+","AJSL@-89").group())

# print(match('([a-z]+)|([A-Z]+)','abc').group())

print(match('[a-z]+|[A-Z]+',"abccc").group())