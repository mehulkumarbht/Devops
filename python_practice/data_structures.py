from loguru import logger

# 1 List – Remove and Insert
# Given a list:#fruits = ["apple", "banana", "cherry", "mango"]
# Remove "banana" and insert "orange" at index 1.
# fruits = ["apple", "banana", "cherry", "mango"]
# fruits[1] = "orange"
# logger.info(f"{fruits}")

# 2: Create a tuple with 3 elements and unpack it into 3 variables. Print each variable on a new line.
# my_tuple = (1, 2, 3)
# x, y, z = my_tuple
# logger.info(f"{x}")
# logger.info(f"{y}")
# logger.info(f"{z}")

# 3: From the list ["cat", "dog", "cat", "bird", "dog", "elephant"], create a set and print only the unique animal names.
# my_list = ["cat", "dog", "cat", "bird", "dog", "elephant"]
# my_set = set(my_list)
# logger.info(f"{my_set}")

# 4: Create a dictionary with names and phone numbers. Add one new contact and update an existing contact’s number.
# contact_info = {"john": "9925253", "jason": 9625461, "ramen": 5656632}
# contact_info["mosh"] = 3652421
# logger.info(f"{contact_info}")
# contact_info["john"] = 9356254
# logger.info(f"{contact_info}")

# 5: Given a list of words:words = ["book", "pen", "book", "bag", "pen", "book"]
# Create a dictionary where the keys are words and the values are how many times each word appears.
# words = ["book", "pen", "book", "bag", "pen", "book"]
# new_list = {}

# for word in words:
#     if word in new_list:
#         new_list[word] += 1
#     else:
#         new_list[word] = 1
# logger.info(f"{new_list}")
# 6:Given a list:numbers = [1, 2, 3, 4, 5], Reverse the list manually using a loop.
# numbers = [1, 2, 3, 4, 5, 6]
# reverse_numbers = []

# for number in range(len(numbers) - 1, -1, -1):
#     reverse_numbers.append(numbers[number])
# logger.info(f"{reverse_numbers}")

# # 7: Given a tuple:t = ("red", "green", "blue").Write a program to check if "green" exists in the tuple.
# t = ("red", "green", "blue")
# if "green" in t:
#     logger.info(f"'Green' is in tuple 't'")

# 8: Set – Given sets:set1 = {1, 2, 3, 4}. set2 = {3, 4, 5, 6}. Remove elements from set1 that are also in set2.
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.difference(set2)
# logger.info(f"{set3}")

# 9: Dictionary – Loop and Print
# Given a dictionary:person = {"name": "John", "age": 30, "city": "Toronto"}
# Loop through the dictionary and print each key with its value.
# person = {"name": "John", "age": 30, "city": "Toronto"}
# my_dict = {}
# for key, value in person.items():
#     logger.info(f"{key}: {value}")

# 10: Mix – Convert Two Lists to Dictionary
# Given: keys = ["name", "age", "city"]
# values = ["Alice", 28, "New York"]
# Combine them into a dictionary using a loop.
# keys = ["name", "age", "city"]
# values = ["Alice", 28, "New York"]

# my_dict = {}
# for num in range(len(keys)):
#     my_dict[keys[num]] = values[num]

# for key, value in my_dict.items():
#     logger.info(f"{key}: {value}")

# 11: Given a list of numbers, write a program that multiplies each element by 2 and stores the result in a new list.
# numbers = [1, 2, 3, 4, 5]
# new_list = []

# for num in range(1, 6, 1):
#     new_list.append(num * 2)
# logger.info(f"{new_list}")

# 12:Given a tuple t = (5, 10, 15, 20), write a program to find the index of the value 15.
# t = (5, 10, 15, 20)
# index_of_15 = t.index(15)
# logger.info(f"{index_of_15}")

# 13: Set – Find Difference, Given two sets,
# Print the elements that are in set a but not in set b.
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a.difference(b)
# logger.info(f"{c}")

# 14: Given a dictionary of names and scores, Print only the names of people who scored more than 80.
# scores = {"Amy": 75, "Bob": 90, "Chad": 60, "Dana": 88}
# for key, value in scores.items():
#     if value > 80:
#         logger.info(f"{key}")

# 15: Mix – Combine Lists into Dictionary with zip() Given two lists:Create a dictionary that maps field names to their values.
# fields = ["id", "name", "age"]
# data = [101, "Jane", 29]

# # names = {}
# # for name in range(len(fields)):
# #     names[fields[name]] = data[name]
# # logger.info(f"{names}")

# names = zip(fields, data)
# print(dict(names))

# 16: Given a list numbers = [1, 2, 3, 4, 5, 6], write a program that creates a new list containing only the odd numbers.
numbers = [1, 2, 3, 4, 5, 6]
new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num)

logger.info(f"{new_list}")
