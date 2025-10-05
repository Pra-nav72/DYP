#class variables: shared among all instance of class
#                  defined outside the constructor
#          allow you to share data among all objects created from the class

#instance variables are defined inside a constructor

class Student:
    
    #class variable: accessed through class name(good practice)
    class_session="2025-27"
    class_students=0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        #add 1 after each object created
        Student.class_students += 1

student1 = Student("Pranav", 22)
student2 = Student("shanu", 25)
student3 = Student("ankit", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)

#accessed using class name(for clear understanding)
# (can also be access through object: student1.class_session)
print(f"My class of session {Student.class_session} has {Student.class_students} students.")