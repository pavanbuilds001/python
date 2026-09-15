#dictionaries in python
#dictionary is a collection of key-value pairs enclosed in curly braces. Each key is unique,
student = {"name": "Bhargavi", "age": 25, "course": "python"}
print(student["name"])
print(student["age"])
print(student["course"])
#access elements in dictionary
student = {"name": "Bhargavi", "age": 25, "course": "python"}
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

print(student.values())
#values() returns all the values in tyhe dictionary

print(student.items())
#items() returns all the value key-value pairs

print(student.get("name"))
#get() returms the valuse of the specified key

student.update({"age: 22"})
#update() updates the value of the specified key

#add new data to  a dictionary           
student["city"] = "hyderabad"

print(student)

print(student.items())
student.pop("age")
print(student)

print(student.values())
#values() returns all the values in tyhe dictionary

print(student.items())
#items() returns all the value key-value pairs

print(student.get("name"))
#get() returms the valuse of the specified key

student.update({"age": 22})
#update() updates the value of the specified key  

print(student)

student.pop("age")
#pop() removes the specified key and its value 

print(student)

# pop item removes the last inserted key-valuer pair
student = {
    "name": "Bhargavi",
    "age": 22 ,
    "course": "python"
}

student.popitem()
print(student)
