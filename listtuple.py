#accessing elements in a list
from statistics import stdev


marks = [80, 90, 75, 85,]

print(marks[0])
print(marks[1])
print(marks[3])

#change elements in a list
marks = [80, 90, 75]
marks[1] = 95
print(marks)

#remove elements from a list
marks = [80, 90, 95]
marks.remove(90)
print(marks)

numbers = [10, 20, 30]

numbers.insert(1,15)

print(numbers)


#extend() method is used to add the elements of one list to the end of another list. In this case, the elements of list b are added to the end of list a.
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
#remove() method is used to remove the first occurrence of a specified value from a list. 
a.remove(2)
print(a)
#clear() method is used to remove all elements from a list, resulting in an empty list.
a.clear()
print(a)
#index() method is used to find the index of the first occurrence of a specified value in a list.
numbers = [10, 20, 30, 40, 50]
index = numbers.index(30)
print(index)

#count() method is used to count the number of occurrences of a specified value in a list.
numbers = [10, 20, 30, 20, 40, 20, 50, 20, 60, 20, 70, 20, 80, 20, 90, 20, 100, 20]
count = numbers.count(20)
print(count)

#sort() method is used to sort the elements of a list in ascending order by default. It modifies the original list.
numbers = [50, 20, 80, 10, 40]
numbers.sort()
print(numbers)
#reverse() method is used to reverse the order of elements in a list. It modifies the original list.
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)
#copy() method is used to create a shallow copy of a list. It returns a new list that contains the same elements as the original list.
a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Output: [20, 30, 40]
print(numbers[:3])   # Output: [10, 20, 30]
print(numbers[2:])  # Output: [30, 40]
print(numbers[::-1]) # Output: [50, 40, 30, 20, 10] # 
print(numbers[-1::]) # Output: [50] #
print(numbers[-4::])# output: [20, 30, 40, 50] #
print(numbers[::-5]) 
print(numbers[-1::])
print(numbers[::-4])
print(numbers[::-3])

#touples in python
#touple is a colection of multiple values that is ordered and cannot be changed after creation
student = ("bhargavi", 98, "python")

print(student[0])
#immutable nature of tuples



#tuple gives error 
#count
numbers = (10, 20, 20, 30, 20)
print(numbers.count(20))

numbers = (5, 6, 7, 8, 9,)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
