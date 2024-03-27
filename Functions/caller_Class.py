# class dept:
#     def __init__(self):
#         self.depts={'hr':"Human resource department",
#                     'mkt':'marketing department',
#                     'mft':'manufacturing department'
#                     ,'sd':'sales department'}
#
#
#     def __call__(self, dept):
#         return self.depts[dept]
#
#
#
# d=dept()
# name=d('hr')
# print(name)

# so we can see this is a caller class as d variable is able to take class
# and also able to access it methods and its variables.
#caller class can be easily converted to closure function or say nested funct

def dept():

        depts = {'hr':"Human resource department",
                    'mkt':'marketing department',
                    'mft':'manufacturing department'
                    ,'sd':'sales department'}


        def dname(dept):
         return depts[dept]

        return dname



d=dept()
name=d('hr')
print(name)



