class Varun_error(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return self.msg



try:
    raise Varun_error('help varun yeah buddy ')
except Varun_error as msg:
    print(msg)
