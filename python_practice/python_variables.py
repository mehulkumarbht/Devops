from loguru import logger

# #1: Create a variable named user_age and assign your age to it. Print the variable.

# user_age = 35

# logger.info(f"{user_age}")

# #2: Assign the value 3.14159 to a variable called pi and print its type using type().

# pi = 3.14159

# logger.info(type(pi))

# #3: Declare two variables width = 5 and height = 10. Calculate the area of a rectangle and store the result in area. Print it.

# width = 5

# height =10

# area = width * height

# logger.info(f"{area}")

# #4: Create a variable name and assign it your name. Then print:"Hello, my name is <your name>!"

# my_name = "sarah"

# logger.info(f"Hello, my name is {my_name}")

# #5: What happens if you assign a new value to an existing variable? Try this: color = "red", color = "blue", print(color)

# color = "red"

# color = "blue"

# logger.info(f"{color}") # Variable assigned with new value

# #6: Swap the values of two variables a = 5 and b = 10 without using a third variable.

# a=5

# b=10

# a,b = b,a

# print(a)

# print(b)

# #7: Convert a string variable year = "2024" into an integer and print its type after conversion.

# year = "2024"

# year = int(year)

# print(type(year))

# #8: Create variables num1 = 7, num2 = 3. Perform and print:Addition, Subtraction, Multiplication, Division, Integer division, Modulo

# num1 = 7

# num2 = 3

# Addition = num1 + num2

# Substraction = num1 - num2

# Multiplication = num1 * num2

# Division = num1 /num2

# Integer_division = num1 // num2

# Modulo = num1 % num2

# print (Addition)

# print (Substraction)

# print (Division)

# print (Integer_division)

# print (Modulo)

# #9: Assign None to a variable called data and check if the variable is None using an if condition.

# data = None

# if data is None:

#      print(data)

# #10: Explain the difference between global and local variables in a function using a short code example.

# x = "awesome"

# def myfunc():

#      global x

#      x = "fantastic"

# myfunc()

# logger.info(f"Python is {x}")

# #when x is global and local variable

# x = "awesome"

# def myfunc():

#      x = "fantastic"

#      logger.info(f"Python is {x}")

#  myfunc()

# logger.info(f"Python is {x}")

# #11:What type is assigned?

# x = 42

# y = "42"

# z = 42.0

# print(type(x))

# print(type(y))

# print(type(z))

# #12: Create a variable is_valid and assign a Boolean value (True or False). Print its type

# is_valid = True

# print(type(is_valid))

# #13: number =100, Convert it to an int, then a float, then back to str. Print each result with its type.

# number ='100'

# number_int = int(number)

# print(number_int)

# print(type(number_int))

# number_fl = float(number)

# print(number_fl)

# print (type(number_fl))

# number_st = str(number)

# print(number_st)

# print(type(number_st))

# #14:Use the isinstance() function to check if 3.14 is a float, and "hello" is a string.
# print(isinstance(3.14, float))
# print(isinstance("hello", str))

# #15: What is the result of this expression:
# result = 10 / 2
# print(result, type(result))

# #16: Assign a complex number (like 2 + 3j) to a variable. Print its type and real/imaginary parts.
# num = 2+3j
# print(type(num))
# print(num.real)
# print(num.imag)

# #17: What happens if you try to add a string and an integer?
# a = "Age: "
# b = "25"
# print(a + b)

# #18: Create a variable called names and assign a list of three strings. Then print the type and length of the list
# names = ["Roy", "Vance", "John"]
# print(type(names), len(names))

# #19: Use a tuple to store three values: a name, an age, and a country. Print each element using indexing.
# value = ("John", 29, "Spain")
# print(value[0])
# print(value[1])
# print(value[2])

# #20: Create a dictionary called employee with keys: name, age, and department. Assign appropriate values and print the dictionary and the type of employee.
# employee = {"name": "john", "age": 29, "department": "Finance" }
# print(employee, type(employee))

# #21: Create three variables in one line: x = 1, y = 2, and z = 3. Print them all in one print() statement.
# x,y,z = 1,2,3
# print(x,y,z)

# #22: What is the difference between these two assignments?
# a = 5
# b = a
# a = 10
# print(b) # as b is assigned values of a earlier, assigning another value doesn't make any change to previous value

# #23: Assign a multiline string to a variable called description using triple quotes ("""). Then print it.
# description = '''I have not learned this in manay years,
# I am starting to learn this now,
# I hope I learn it quickly! '''
# print(description)

# #24: Create a variable filename = "data.csv". Use in to check if the string "csv" is in the variable. Print the result.
# filename = "data.csv"
# print("csv" in filename)

# #25: price = 9.99, quantity = 5, Calculate and print the total cost.
# price = 9.99
# quantity = 5
# calculate = price * quantity
# print(calculate)

# #26: Use the id() function to print the memory location of two variables with the same value:
# x = 100
# y = 100
# print(id(x), id(y))

# #27: What will be the output of this code?
# counter = 1
# counter += 3
# print(counter)

# #28: Declare a variable path = r"C:\Users\data" (a raw string). Print it and explain why the raw string is useful.
# link = r"C:\Users\data"
# print(link)

# #29: Create a variable result = None. Use an if statement to print "No result yet" if the variable is None.
# result = None
# if result == None:
#     print("No result yet")

# #30: Declare a variable with a name that is not allowed in Python and try running it (e.g., 1st_place = "John"). Observe the error message and fix it.
# _1st_place = "john"
# print(_1st_place)

# 31: Declare four variables of different types: an int, a float, a string, and a bool. Print all their values and types.
# a = 5
# b = 9.0
# c = "hello"
# d = True
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)

# 32: What is the output?
# x = 4
# x *= 3
# print(x) # After assinging 4 value to x, 4 is multiplied with 3, that why answer is 12

# 33: Combine two strings first = "Data" and second = "Engineer" using string concatenation and store the result in full_title. Print it.
# first = "Data"
# second = "Engineer"
# full_title = first +" "+ second
# print (full_title)

# 34: number = 25, Check whether number is even or odd using the modulo operator and if condition. Print "Even" or "Odd".
# num = 311646145
# if num % 2 == 0:
#     logger.info(f"number is even")
# else:
#     logger.info(f"number is odd")

# 35: Assign the same value "Pending" to three variables: status1, status2, and status3 in a single line.
# status1=status2=status3 = "Pending"
# print(status1)
# print(status2)
# print(status3)

# 36: What is the output and type of the following expression?
# value = 5 + 2.0
# print(value, type(value))

# 37: Create a list called scores with values [90, 85, 70], then store the average in a variable called avg_score and print it.
# score = [90, 85, 70]
# avr = sum(score) / len(score)
# print(avr)

# from statistics import mean
# avr = mean(score)
# print(avr)

# 38: Assign a value of your choice to a variable named temperature. Write a condition to print "Hot" if it’s above 30, otherwise print "Cool".
# temp = float(input("Enter temperature: "))
# if temp > 30:
#     print(f"Hot")
# else:
#     print(f"Cool")

# 39: Declare a constant (by convention) named PI with value 3.14159. Print the area of a circle with radius r = 5 using the formula πr².
# PI = 3.14159
# r = 5
# area_of_circle = PI*(r**2)
# print(area_of_circle)

# 40: What will this print and why?
# x = y = z = 0 #Each x,y and z assigned value of 0
# x += 1 # 1 is added to 0 for x
# print(x, y, z) # so while printing x,y,z, answers will be 1, 0, 0

# 41: Multiple assignments with same value
# Assign the value "unknown" to variables city, country, and region in a single line. Print them all.
# city = country = region = "unknown"
# print(city)
# print(country)
# print(region)

# 42: Calculate the average cost per item and store it in avg_cost. Print the result with 2 decimal places.
# total = 120
# items = 8
# avg_cost = total / items
# logger.info(f"{avg_cost:.2f}")

# 43: Create a variable name = "Alex" and age = 30. Print this sentence using an f-string:Alex is 30 years old.
# name = "Alex"
# age = 30
# logger.info(f"{name} is {age} years old")

# 44: Store today’s date using the datetime module in a variable today, and print it.
# from datetime import date
# today = date.today()
# print(today)

# 45: Create two variables a = 10 and b = "5". Convert b to integer and multiply with a. Print the result.
# a = 10
# b = "5"
# total = a * int(b)
# print(total)

# 46: What will be the output?
# score = 0 # Assigned 0 value to the score
# score = score + 5 # Assigned new value score + 5
# score += 10 # now new value i.e 5 + 10 = 15 will be the answer
# print(score)

# 47: Create a variable is_admin = True. Use an if-else block to print "Access granted" if is_admin is True, else "Access denied".
# is_admin = False
# if is_admin is True:
#     logger.info(f"Access granted")
# else:
#     logger.info(f"Access denied")

# 48: Create a variable sentence = "Data Engineering is fun" and print the number of words in it.
# sentence = "Data Engineering is fun"
# num = sentence.split()
# sent_length = len(num)
# logger.info(f"{sent_length}")

# 49: Create a variable x = None. Write a condition to print "No value assigned" if x is None.
# x = None
# if x == None:
#     logger.info(f"No value assigned")

# 50: Create a variable balance = 500. Then:Subtract 100 for a purchase, Add 50 as cashback, Print the final balance
# balance = 500
# purchase = balance - 100
# cashback = purchase + 50
# logger.info(cashback)

# 51: Create a variable filename = "report_2025.xlsx". Extract the file extension (xlsx) and print it.
# import os
# filename = "report_2025.xlsx"
# _, extension = os.path.splitext(filename)
# logger.info(f"{extension}")

# 52: Assign product = "Laptop" and price = 999.99. Use an f-string to print: The price of Laptop is $999.99
# product = "Laptop"
# price = 999.99
# logger.info(f"The price of {product} is {price}")

# 53: What does this print and why?
# a = 5
# b = 2
# a //= b #the floor division // rounds the result down to the nearest whole number
# print(a)

# 54: Create a variable bio = "Python is amazing."Convert the entire string to uppercase and print it.
# bio = "Python is amazing"
# uppercase = bio.upper()
# logger.info(f"{uppercase}")

# 55: Create a variable count = "1000". Convert it to an integer, add 250, and store in total. Print total.
# count = "1000"
# converted_count = int(count)
# total = converted_count + 250
# logger.info(f"{total}")

# 56: What happens in this code? Explain and fix it: num1 = "10", num2 = 5, result = num1 + num2
# num1 = "10"
# num2 = 5
# result = int(num1)+ num2 # need to convert num1 from string to int to add it to num2
# logger.info(f"{result}")

# 57: Store your name in a variable. Use slicing to print just the first 3 characters.
# name = "sarman"
# print(name[:3])

# 58: What’s the difference between is and ==?
# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x == y) # x is matching with y, so it is giving true
# print(x is y) # x is not y so it is giving false

# 59: Create variables weight_kg = 72. Convert it to pounds (1 kg = 2.20462 pounds) and store in weight_lb. Print the result rounded to 2 decimals.
# weight_kg = 72
# convert_to_pounds = weight_kg * 2.20462
# logger.info(f"{convert_to_pounds:.2f}")

# 60: Suppose description = " Raw data feed ". Remove extra spaces at the beginning and end. Print the cleaned string and its length.
# description = " Raw data feed "
# clean_description = description.strip()
# logger.info(f"{clean_description}")

# 61: Lists – Practice Questions
# Create a list of 5 integers. Replace the second item with 100 and print the list.
# num = [1, 2, 3, 4, 5]
# num[1] = 100
# print(num)

# 62: Write a loop to sum all elements in a list: [3, 5, 7, 9].
# num = [3, 5, 7, 9]
# total = 0
# for item in num:
#     total = total + item
# logger.info(f"Total is {total}")

# 63: Check if "apple" exists in the list ["banana", "apple", "cherry"].
# fruits = ["banana", "apple", "cherry"]
# if "apple" in fruits:
#     logger.info(f"Yes, Apple is part of the list!")

# 64: Remove the last element from a list using pop() and print the updated list.
# fruits = ["banana", "apple", "cherry"]
# fruits.pop()
# logger.info(f"{fruits}")

# 65: Sort a list of numbers in descending order.
# num = [37, 51, 73, 69]
# num.sort(reverse=True)
# logger.info(f"{num}")

# 66: Create a tuple of 4 colors. Try modifying the second color — what happens?
# colors = ("red", "yellow", "green", "blue")
# color = list(colors)
# color[1] = "black"
# colors = tuple(color)
# logger.info(f"New colors list is {colors}")

# 67: Convert the tuple ("red", "green", "blue") into a list, change "green" to "yellow", and convert it back to a tuple.
# colors = ("red", "green", "blue")
# color = list(colors)
# color[1] = "yellow"
# colors = tuple(color)
# logger.info(f"New list of colors is {color}")
# 68: Unpack the tuple coordinates = (10, 20) into two variables x and y.
# coordinates = (10, 20)
# x, y = coordinates
# logger.info(f"{x}")
# logger.info(f"{y}")

# 69: Write a function that takes a tuple of numbers and returns their average.
# mytuple = (1, 2, 3, 4, 5)
# # Option:1
# # avg = sum(mytuple) / len(mytuple)
# # logger.info(f"Average of mytuple is {avg}")


# # Option:2
# def average(mytuple):
#     if len(mytuple) == 0:
#         return 0
#     return sum(mytuple) / len(mytuple)


# avg = average(mytuple)
# logger.info(f"Average is {avg}")

# 70: Create a tuple with one element (the number 5). What’s the syntax?
# mytuple = (5,)
# logger.info(f"syntax is {type(mytuple)}")

# 71: Create a set of numbers: {1, 2, 3, 4}. Add 5 to it.
# num = {1, 2, 3, 4}
# num.add(5)
# logger.info(f"{num}")

# # 72: Try adding a duplicate number to the set — what happens?
# # Adding duplicate number will not work in case of set
# # 73: Remove an item from a set safely using .discard().
# num = {1, 2, 3, 4, 5}
# num.discard(5)
# logger.info(f"{num}")
# # 74: Find the union and intersection of two sets: {1, 2, 3} and {3, 4, 5}.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set1.union(set2)
# logger.info(f"{set3}")

# # 75: Convert a list with duplicates [1, 2, 2, 3, 3, 3] into a set and print the result.
# list1 = [1, 2, 2, 3, 3, 3]
# myset = set(list1)
# print(type(myset))

# # 76: Create a dictionary {"name": "Alice", "age": 25} and print the value of "name".
# x = {"name": "Alice", "age": 25}
# logger.info(x["name"])
# # 77: Add a new key-value pair "city": "Toronto" to the dictionary.
# x = {"name": "Alice", "age": 25}
# x.update({"city": "Toronto"})
# logger.info(x)
# # 78: Loop through the dictionary and print each key and its value.
# x = {"name": "Alice", "age": 25}
# for y in x.items():
#     logger.info(f"{y}")
# # 79: Use .get() to safely access the value for the key "email" (which doesn't exist).
# x = {"name": "Alice", "age": 25}
# y = x.get("email")
# logger.info(f"{y}")
# # 80:Create a dictionary of student names and their scores. Print names of students who scored above 80.
# scores = {"name1": 80, "name2": 92, "name3": 89, "name4": 68}
# for name, score in scores.items():
#     if score > 80:
#         logger.info(f"{name}: {score}")
# # 81: Write a program that takes a list of numbers [10, 20, 30, 40, 50] and prints a new list containing only the numbers greater than 25.
# list1 = [10, 20, 30, 40, 50]
# number = []
# for num in list1:
#     if num > 25:
#         number.append(num)
# print(number)
# 82: A = {1, 2, 3, 4}  , B = {3, 4, 5, 6}, Find Elements common to both sets & Elements unique to set A
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A.intersection(B)  # Elements common to both sets
# D = A.difference(B)  # Elements unique to set A
# print(C)
# print(D)

# 83: Create a tuple of your top 3 favorite movies. Unpack the tuple into three separate variables and print each movie on a new line.
# mytuple = ("me", "you", "and")
# a, b, c = mytuple
# logger.info(a)
# logger.info(b)
# logger.info(c)

# 84: Create a dictionary of 3 employees and their salaries. Then: Increase all salaries by 10%. Print the updated dictionary.
# salary = {"Joy": 1000, "Roy": 2000, "Max": 3000}
# for name, sal in salary.items():
#     inc_sal = sal + (sal * 0.10)
#     logger.info(name, inc_sal)

# 85: Create a dictionary where each key is a student’s name, and the value is a list of their marks. Then, print each student’s name with their average marks.
# marks = {"Joy": [85, 65, 70], "Roy": [90, 61, 73], "Max": [85, 72, 89]}
# for name, mark in marks.items():
#     avg_mark = sum(mark) / len(mark)
#     logger.info(f"{name}: {avg_mark:.2f}")

# 86: Remove Even Numbers, Given a list of numbers, remove all even numbers from the list:
# numbers = [12, 7, 9, 14, 5, 2]
# odd_numbers = []
# for num in numbers:
#     if num % 2 != 0:
#         odd_numbers.append(num)
# print(odd_numbers)

# 87: Write a list comprehension to create a list of squares from 1 to 10.
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = [x**2 for x in num_list]
# logger.info(f"{squares}")

# 88: Find the largest number in a list without using max().
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = num_list[0]
# for x in num_list:
#     if x > new_list:
#         new_list = x
# logger.info(f"{new_list}")

# 89: Indexing a Tuple: Given a tuple t = (10, 20, 30, 40, 50), print the third element.
# t = (10, 20, 30, 40, 50)
# print(f"{t[2]}")

# 90: Try changing the second element of the tuple (1, 2, 3) to 5. What happens and why?
# t = (1, 2, 3)
# x = list(t)
# x[1] = 5
# t = tuple(x)
# print({t})

# 91: Set from List: Convert the list [1, 2, 2, 3, 4, 4, 5] into a set and print it.
# list1 = [1, 2, 2, 3, 4, 4, 5]
# list2 = set(list1)
# logger.info(f"{list2}")  # duplicates removed as list converted into set

# 92: Given sets A = {1, 2, 3} and B = {3, 4, 5}, find:The union, The intersection, The difference (A - B)
# A = {1, 2, 3}
# B = {3, 4, 5}
# C = A.union(B)
# D = A.intersection(B)
# E = A.difference(B)
# logger.info(f"{C}")
# logger.info(f"{D}")
# logger.info(f"{E}")

# 93: Check if the key "Math" exists in the dictionary: grades = {"Science": 90, "English": 85}
# grades = {"Science": 90, "English": 85}
# if "Match" in grades:
#     logger.info(f"There is key 'Math' is dictionary")
# else:
#     logger.info(f"There is no key 'Math' is dictionary")

# 94: Update Value: Increase "Science" marks by 10 in the dictionary above.
# grades = {"Science": 90, "English": 85}
# grades["Science"] = 100
# print(grades)

# 95:Create from Two Lists: Given keys = ["a", "b", "c"] and values = [1, 2, 3], create a dictionary using a loop.
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

logger.info(f"{my_dict}")
