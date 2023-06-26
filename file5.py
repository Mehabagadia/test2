class Student:
    count =1
    def __init__(self):
        Student.count=Student.count+1
s1= Student()
s2= Student()
s3= Student()
print("The Number Of students: " ,Student.count)