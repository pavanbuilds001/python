#logical operators
age = 10
citizen = True
print(age >= 18 and citizen == True)

age = 36
citizen = True
print(age >= 18 and citizen == True)

is_logged_in = True

print(not is_logged_in )

#atm eligibility checker
balance=10000
withdraw=5000
print(withdraw > 0 and withdraw <= balance)
print(withdraw > 0 or withdraw <= balance)

#student scholarship eligibility checker
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance: "))
eligible = marks >= 85 and attendance >= 75

print("scholarship Eligible:", eligible)
