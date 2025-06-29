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
# numbers = [1, 2, 3, 4, 5, 6]
# new_list = []
# for num in numbers:
#     if num % 2 != 0:
#         new_list.append(num)

# logger.info(f"{new_list}")

# 17: Given a tuple colors = ("red", "green", "blue"), convert it to a list, add "yellow", and convert it back to a tuple.
# colors = ("red", "green", "blue")
# new_set = list(colors)
# new_set.insert(3, "yellow")
# logger.info(f"{(tuple(new_set))}")

# 18: Given two sets:Write a program to check if small is a subset of big.
# small = {1, 2, 3}
# big = {1, 2, 3, 4, 5, 6}
# if small.issubset(big):
#     logger.info(f"Small is subset of big")
# else:
#     logger.info(f"Small is not subset of big")

# 19: Given a dictionary: Write code to increase the age by 1.
# person = {"name": "Alice", "age": 25}
# person["age"] = 25 + 1
# print(person)

# 20: Write a program that counts how many vowels (a, e, i, o, u) are in this string:"hello world"
# vowels = ("a", "e", "i", "o", "u")
# my_string = "My name is anthony gonsalves"

# count = 0

# for char in my_string:
#     if char in vowels:
#         count += 1

# logger.info(f"{count}")

# 21: Given a list of numbers [10, 20, 30, 40], write a program to calculate and print the total sum.
# numbers = [10, 20, 30, 40]
# totalsum = sum(numbers)
# logger.info(f"{totalsum}")

# 22: Given a tuple colors = ("red", "green", "blue"), convert it into a single string separated by commas, e.g., "red,green,blue".
# colors = ("red", "green", "blue")
# mystring = str(colors)
# logger.info(f"{mystring}")

# 23: Given set1 = {1, 2, 3} and set2 = {3, 4, 5}, create a new set containing all unique elements from both sets.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set1.intersection(set2)
# logger.info(f"{set3}")

# 24: Given d = {"a": 1, "b": 2, "c": 3}, remove the key "b" and print the updated dictionary.
# d = {"a": 1, "b": 2, "c": 3}
# d.pop("b")
# print(d)

# 25: Given a list [8, 12, 4, 19, 5], write code to find and print the largest number without using the max() function.
# mylst = [8, 12, 4, 19, 5]

# large = mylst[0]

# for num in mylst:
#     if num > large:
#         large = num
# logger.info(f"{large}")

# 26: Given a list [8, 12, 4, 19, 5], write code to find and print the smallest number without using min().
# mylst = [8, 12, 4, 19, 5]
# small = mylst[0]

# for num in mylst:
#     if num < small:
#         small = num

# logger.info(f"{small}")

# 27: Given [8, 12, 4, 19, 5], write a program to calculate the average manually (loop through to sum and count).
# mylst = [8, 12, 4, 19, 5]
# total = 0
# count = 0

# for num in mylst:
#     total += num
#     count += 1
# avg = total / count
# logger.info(f"{avg}")

# 28: Write a program to count how many even numbers are in [8, 12, 4, 19, 5].
# numbers = [8, 12, 4, 19, 5]
# even_num = []
# for num in numbers:
#     if num % 2 == 0:
#         even_num.append(num)
# logger.info(f"{even_num}")

# 29: Given [8, 12, 4, 19, 5], write code to find the second largest number without using sorted() or max().
# mynum = [8, 12, 4, 19, 5]
# largest = mynum[0]

# for num in mynum:
#     if num > largest:
#         largest = num

# second_largest = None
# for num in mynum:
#     if num != largest:
#         if (second_largest is None) or (num > second_largest):
#             second_largest = num

# logger.info(f"{second_largest}")
# 30: Without using index() or max(), find and print the index position of the largest number in [8, 12, 4, 19, 5].
# mylst = [8, 12, 4, 19, 5]
# largest = mylst[0]
# largest_index = 0
# for num in range(len(mylst)):
#     if mylst[num] > largest:
#         largest = mylst[num]
#         largest_index = num
# logger.info(f"{largest}")
# logger.info(f"{largest_index}")

# 31: Write code to print all the indices where the value 7 appears.
# numbers = [3, 7, 2, 7, 9, 7]
# seven_index = []

# for num in range(len(numbers)):
#     if numbers[num] == 7:
#         seven_index.append(num)
# logger.info(f"{seven_index}")  # This will give you indices where value is 7
# # To get how many times it appeares in the list,
# numbers = [3, 7, 2, 7, 9, 7]
# count = 0

# for num in range(len(numbers)):
#     if numbers[num] == 7:
#         count += 1
# logger.info(f"{count}")

# 32: Given the string:"mississippi", Use a dictionary to count how many times each character appears.
# name = "mississippi"
# count = {}
# for char in name:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# logger.info(f"{count}")
# 33: Create a new list containing only the words that have more than 3 letters.
# words = ["apple", "is", "delicious", "and", "red"]
# new_list = []

# for char in words:
#     if len(char) > 3:
#         new_list.append(char)
# logger.info(f"{new_list}")

# 34: Write code to find and print the smallest number without using min().
# numbers = [12, 3, 7, 1, 9]
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num
# logger.info(f"{smallest}")

# 35: Write code to reverse the string using a loop and build a new reversed string.
mystrng = "python"
newstrng = ""
for char in range(len(mystrng) - 1, -1, -1):
    newstrng += mystrng[char]

logger.info(f"{newstrng}")
