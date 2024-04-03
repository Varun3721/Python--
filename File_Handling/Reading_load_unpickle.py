import classfileForPickle,pickle

with open('students.data','rb') as file:
    for i in range(3):
        s=pickle.load(file)
        s.display()