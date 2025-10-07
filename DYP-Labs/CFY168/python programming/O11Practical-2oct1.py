#3.display students info
student_info={}
student_details = []
marks = []

num = int(input("Enter total number of students: "))

for i in range(1,num+1):
    print(f"Enter details of student Roll no.{i}:")
    name = input("Enter Name: ")
    student_details.append(name)

    num_subjects = int(input("Enter total number of subjects: "))
    student_details.append(num_subjects)
    
    for j in range(1, num_subjects+1):
        marks.append(int(input(f"Enter marks obtainded in subject {j}: ")))
    student_details.append(marks)

    student_details.append(sum(marks))  
    
    full_marks = int(input("Full marks: "))
    
    percentage = ((sum(marks)) / (num_subjects*full_marks)) * 100
    student_details.append(percentage)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    student_details.append(grade)

    student_info.update({i: student_details})
    student_details = []
    marks = []



    # student_info.keys = i
    # student_info.values = student_details
for key, value in student_info.items():
    print(f"Roll no.{key}: {value}")
