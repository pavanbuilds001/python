#arthematic operations
salary=25000
ha=salary*0.20
dfa=salary*0.10
total_salary = salary + ha + dfa
print("Total Salary:", total_salary)     

a=10
b=3

print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("floor division:", a//b)
print("remainder:", a % b)
print("power:", a ** b)


#simple calculator
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("floor division:", a//b)


#student marks calculator 
name= input("Enter student name: ")

m1= int(input("Enter marks of python 1: "))
m2= int(input("Enter marks of java 2: "))
m3= int(input("Enter marks of sql 3: "))

total_marks= m1 + m2 + m3
average= total_marks / 3

print("\n------ student report  ------")
print("Student name:", name)
print("Total marks:", total_marks)
print("Average marks:", average)


#shopping bill calculator
price1= int(input("Enter price of item 1: "))
price2= int(input("Enter price of item 2: "))
price3= int(input("Enter price of item 3: "))
total = price1 + price2 + price3

discount= total * 0.10
final_amount = total - discount

print("Total price:", total)
print("Discount:", discount)
print("Final amount:", final_amount)

#comparison operators
a=10 
b=20
print( a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)   

#age eligibility checker
age= int(input("Enter your age: "))
if age >= 18:
    print("eligible", age >= 18)  
#password  checker
    correct_username= "pavan"
    correct_password= "pavan123" 

    username = input("Enter username: ")
    password = input("Enter password: ")

print(username == correct_username)
print(password == correct_password)

    #assignment operators
x=10
x += 5
print(x)

x -= 2
print(x)
x *= 3
print(x)

#bank balance
balance= 10000
deposit=5000
balance += deposit
print("after deposit :", balance)

withdraw= 2000
balance -= withdraw
print("after withdrawal :", balance)

#pass or fail checker
marks= int(input("Enter your marks: "))

print("passed:", marks >= 40)

#atm eligibility
balance=10000
withdraw=5000


print(withdraw > 0 and withdraw <= balance)