from loguru import logger

# Day:1
colors = ["Red", "Blue", "Black", "White"]
# logger.info(f"{colors}")
# logger.info(f"{colors[0]}")
# logger.info(f"{colors[-1]}")
# colors[1] = "purple"
# logger.info(f"{colors}")
# colors.append("Pink")
# logger.info(f"{colors}")
# colors.remove("Black")
# logger.info(f"{colors}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# logger.info(f"{numbers[:3]}")
# logger.info(f"{numbers[-2:]}")

# logger.info(f"{len(colors)}")

# Day-2
# colors = ["red", "blue", "green"]
# for i in range(len(colors)):
#     print(f"Index {i}: {colors[i]}")

# print only numbers less than 8.
# numbers = [1, 3, 6, 8, 10]
# for num in numbers:
#     if num < 8:
#         logger.info(f"{num}")

# Make a new list with all colors in your colors list longer than 3 letters.
# colors = ["red", "blue", "green"]
# long_name_colors = []
# for color in colors:
#     if len(color) > 3:
#         long_name_colors.append(color)
# logger.info(f"{long_name_colors}")

# Sum all numbers in and print the total.
# numbers = [5, 10, 15]
# total = 0
# for num in numbers:
#     total += num
# logger.info(f"{total}")


# def sum_numbers(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total


# def multiply_numbers(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product

# result = multiply_numbers([2, 3, 4])
# print(result)

# Day-3
# Write a function get_long_words(words) that:
# Receives a list of strings.
# Returns a new list with words longer than 4 characters.
# def get_long_words(words):
#     word_list = []
#     for word in words:
#         if len(word) > 4:
#             word_list.append(word)
#     return word_list


# result = get_long_words(["apple", "is", "very", "delicious"])
# print(result)

# Build a reversed version without [::-1] or .reverse().
# nums = [10, 20, 30, 40]
# reversed_list = []
# for num in range(len(nums) - 1, -1, -1):
#     reversed_list.append(nums[num])
# logger.info(f"{reversed_list}")

# # Write a function sum_positive(numbers): It returns the sum of all numbers in the list ignoring any negative numbers.
# numbers = [5, -2, 7, -3, 10]


# def sum_positive(numbers):
#     positive_numbers = 0
#     for num in numbers:
#         if num > 0:
#             positive_numbers += num
#     return positive_numbers


# result = sum_positive(numbers)
# print(result)

# Day-4
# Write a function called count_words(text) that:Receives a string of text.Returns a dictionary with counts of each word.
# text = "apple banana apple orange banana apple"


# def count_words(text):
#     word_count = {}
#     words = text.split()
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count


# result = count_words(text)
# print(result)

# # Write a function called get_max_value(d) that:Receives a dictionary where keys are strings and values are numbers.Returns the key with the highest value.
# scores = {"Alice": 85, "Bob": 92, "Charlie": 78}


# def get_max_value(scores):
#     highest_key = None
#     highest_value = 0
#     for key, value in scores.items():
#         if value > highest_value:
#             highest_value = value
#             highest_key = key
#     return highest_key


# result = get_max_value(scores)
# logger.info(f"{result}")

# # Print each student’s name and their average grade
# grades = {"Alice": [85, 90, 88], "Bob": [72, 75, 70], "Charlie": [95, 100, 98]}
# avg = 0
# for key, value in grades.items():
#     avg = sum(value) / len(value)
#     logger.info(f"{key}: {avg:.2f}")

# # Write a function create_dict(keys, values) that:Receives two lists.Returns a dictionary pairing keys and values.
# keys = ["id", "name", "age"]
# values = [1, "Alice", 30]


# def creat_dict(keys, values):
#     new_dict = {}

#     for i in range(len(keys)):
#         new_dict[keys[i]] = values[i]

#     for key, value in new_dict.items():
#         logger.info(f"{key}:{value}")
#     return new_dict


# result = creat_dict(keys, values)
# logger.info(f"{result}")


# def creat_dict(keys, values):
#     new_dict = {}
#     for k, v in zip(keys, values):
#         new_dict[k] = v
#     logger.info(f"{keys}:{values}")
#     return new_dict


# result = creat_dict(keys, values)
# logger.info(f"{result}")

# # Write code to create a new dictionary containing only items where the quantity > 0.
# inventory = {"apple": 5, "banana": 0, "orange": 3, "kiwi": 0}
# positive_inventory = {}
# for key, value in inventory.items():
#     if value > 0:
#         positive_inventory[key] = value
# logger.info(f"{positive_inventory}")

# Day-5
# Write a function get_passed_students(grades) that returns a list of names with grades ≥ 60.
# grades = {"Alice": 85, "Bob": 62, "Charlie": 48, "Daisy": 90}


# def get_passed_students(grades):
#     high_grades = {}
#     for key, value in grades.items():
#         if value >= 60:
#             high_grades[key] = value
#     return high_grades


# result = get_passed_students(grades)
# logger.info(f"{result}")

# # Write code to calculate the total quantity for each item and print:
# items = {"apple": [10, 15, 20], "banana": [5, 0, 12], "orange": [7, 8, 6]}
# new_items = {}
# for key, value in items.items():
#     value = sum(value)
#     new_items[key] = value
# logger.info(f"{new_items}")

# # Create a dictionary like:
# products = ["pen", "notebook", "eraser"]
# prices = [10, 50, 5]
# stationary = {}
# for k, v in zip(products, prices):
#     stationary[k] = v
# logger.info(f"{stationary}")

# for i in range(len(products)):
#     stationary[products[i]] = prices[i]
# for products, prices in stationary.items():
#     logger.info(f"{stationary}")

# Write a function that finds the number that appears most frequently.
# numbers = [1, 2, 2, 3, 4, 4, 4, 5]


# def most_frequent_number(numbers):
#     frequent_number = {}
#     for num in numbers:
#         if num in frequent_number:
#             frequent_number[num] += 1
#         else:
#             frequent_number[num] = 1

#     most_frequent = None
#     max_count = 0
#     for k, v in frequent_number.items():
#         if v > max_count:
#             max_count = v
#             most_frequent = k
#     return most_frequent


# result = most_frequent_number(numbers)
# logger.info(f"{result}")

# Day-6
# 1: Print Numbers from 1 to 20 (Skip Multiples of 3)
# Write a function that prints all numbers from 1 to 20, skipping those that are divisible by 3.


# def numbers_from():
#     new_list = []
#     for num in range(1, 21):
#         if num % 3 != 0:
#             new_list.append(num)
#     return new_list


# result = numbers_from()
# print(result)


# 2: Write a function fizzbuzz(n) that:Loops from 1 to n, For multiples of 3, print "Fizz", For multiples of 5, print "Buzz", For multiples of both 3 and 5, print "FizzBuzz", Otherwise, print the number
# def fizzbuzz(n):
#     for num in range(1, n):
#         if num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")
#         elif num % 3 or 5 == 0:
#             print("FizzBuzz")
#         else:
#             print(n)


# fizzbuzz(15)

# 3: Write a function count_case(text) that:Receives a string, Returns a dictionary with keys: 'uppercase' and 'lowercase' and their counts.
# text = "Hello World"


# def count_case(text):
#     my_dict = {"uppercase": 0, "lowercase": 0}
#     for char in text:
#         if char.isupper():
#             my_dict["uppercase"] += 1
#         if char.islower():
#             my_dict["lowercase"] += 1
#     return my_dict


# result = count_case(text)
# logger.info(f"{result}")

# 4: Write a function that takes a list and returns a new list with duplicates removed, but preserves the order.

# numbers = [1, 2, 2, 3, 4, 4, 5]


# def numbers_in_orders(numbers):
#     new_numbers = []
#     for num in numbers:
#         if num not in new_numbers:
#             new_numbers.append(num)
#     return new_numbers


# result = numbers_in_orders(numbers)
# logger.info(f"{result}")


# 5: Write a function check_password_strength(password) that: Returns "Strong" if the password, Has 8 or more characters, Contains at least one digit, Contains at least one uppercase letter, Otherwise, return "Weak"
# def check_password_strength(password):
#     has_upper = False
#     has_digits = False

#     if len(password) > 8:
#         return "Strong"
#     for char in password:
#         if char.isdigit():
#             has_digits = True
#         elif char.isupper():
#             has_upper = True
#     if has_digits and has_upper:
#         return "Strong"
#     else:
#         return "Weak"


# result = check_password_strength("hello wor")
# logger.info(f"{result}")

# 6: Write a function remove_duplicates() that:Takes a list as input.Returns a new list with duplicates removed, original order preserved.
# data = [1, 2, 2, 3, 4, 4, 5]


# def remove_duplicates(data):
#     new_list = []
#     for num in data:
#         if num not in new_list:
#             new_list.append(num)
#     return new_list


# result = remove_duplicates(data)
# logger.info(f"{result}")

# 7: Write a function count_case(text) that:Takes a string input.Returns a dictionary with two keys:"uppercase" → number of uppercase letters, "lowercase" → number of lowercase letters.
# text = "Hello World"


# def count_case(text):
#     new_dict = {"uppercase": 0, "lowercase": 0}
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 new_dict["uppercase"] += 1
#             else:
#                 new_dict["lowercase"] += 1
#     return new_dict


# result = count_case(text)
# logger.info(result)

# 8: Write a function char_frequency(text) that:Takes a string input.Returns a dictionary showing how many times each character appears. Ignore spaces and count case-insensitively (treat A and a the same).
text = "Hello World"


def char_frequency(text):
    new_dict = {}
    for char in text.lower():
        if char == " ":
            continue
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict


result = char_frequency(text)
logger.info(f"{result}")
