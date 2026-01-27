class Student:
    def __init__(self, roll_no=None, name=None, percentage=None):
        self.roll_no = roll_no
        self.name = name
        self.percentage = percentage

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Percentage:", self.percentage)
        print("---------------------")

s1 = Student(101)

s2 = Student(102, "Rahul")

s3 = Student(103, "Anjali", 88.5)

s1.display()
s2.display()
s3.display()
