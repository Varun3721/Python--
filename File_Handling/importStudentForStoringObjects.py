import classfileForPickle,pickle

stud=[classfileForPickle.Student('ajay',18,'cse'),classfileForPickle.Student('varun',23,'cse'),classfileForPickle.Student('ganesh',25,'Ece')]

with open('students.data','wb') as file:
    for sd in stud:
        pickle.dump(sd,file)


