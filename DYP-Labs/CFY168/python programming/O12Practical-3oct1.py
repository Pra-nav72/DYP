#Q5. Write a Python program to calculate the gross salary of 10 employees using the following data:
#       Basic Salary, DA (25%), HRA (15%), PF (12%), TA (75%)


Basic_salary = [12000, 15000, 12300, 10200, 13400, 12500, 14500, 11000, 11200, 13200]
DA, HRA, PF, TA = 0.25, 0.15, 0.12, 0.75
gross_salary = []


def calculate_gross_salary(basic_salary):
    NetPay = basic_salary + (basic_salary * DA) + (basic_salary * HRA) + (basic_salary * TA)
    gross_pay = NetPay - (basic_salary * PF)
    return gross_pay

for salary in Basic_salary:
    gross_salary.append(calculate_gross_salary(salary))

print(f"basic salary: {Basic_salary}")
print(f"gross salary: {gross_salary}")