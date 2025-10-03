age=34
cgpa= 9.4
name= "kunal"
is_student = True

print(f"age:{type(age)}, cgpa: {type(cgpa)}, name: {type(name)}, student? : {type(is_student)}")

#Typecasting into another type
age1 = str(age)
age2 = float(age)
age3 = bool(age)
print(f"str: {(age1)}, float: {(age2)}, bool: {age3}")

cgpa1 = int(cgpa)
cgpa2 = str(cgpa)
cgpa3 = bool(cgpa)
print(f"int: {cgpa1}, str: {cgpa2}, bool: {cgpa3}")

