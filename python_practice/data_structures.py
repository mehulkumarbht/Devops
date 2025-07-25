from loguru import logger
import string
from collections import Counter

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
# text = "Hello World"


# def char_frequency(text):
#     new_dict = {}
#     for char in text.lower():
#         if char == " ":
#             continue
#         if char in new_dict:
#             new_dict[char] += 1
#         else:
#             new_dict[char] = 1
#     return new_dict


# result = char_frequency(text)
# logger.info(f"{result}")


# Day-7:
# 1:Write a function get_grade(score):Takes a number (0–100).Returns "A" if score ≥ 90, "B" if ≥ 80, "C" if ≥ 70, else "Fail".
# def get_grade(score):
#     if score < 0 or score > 100:
#         return "Invalid score. Must be between 0 and 100 "
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     else:
#         return "Fail"


# result = get_grade(99)
# logger.info(f"{result}")

# 2: Write a function odd_even(numbers):Takes a list of numbers.Returns a dictionary like {"odd": count, "even": count}.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def odd_even(numbers):
#     my_dict = {"odd": 0, "even": 0}
#     for num in numbers:
#         if num % 2 == 0:
#             my_dict["even"] += 1
#         else:
#             my_dict["odd"] += 1
#     return my_dict


# result = odd_even(numbers)
# logger.info(f"{result}")

# 3: Write a function is_leap_year(year): A year is leap if: Divisible by 4 and not by 100 or divisible by 400, Return True if leap year, else False.
# year = int(input("Please enter a year: "))


# def is_leap_year(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False


# result = is_leap_year(year)
# logger.info(f"{result}")

# 4: Write a function count_vowels(text): Returns how many vowels are in a string. Ignore case.
# text = "Hello world"


# def count_vowels(text):
#     vowel = "aeiou"
#     count = 0
#     for char in text.lower():
#         if char in vowel:
#             count += 1
#     return count


# result = count_vowels(text)
# logger.info(f"{result}")

# 5: Write a function min_max(numbers):Takes a list of numbers.Returns a dictionary like {"min": val, "max": val}, Don’t use min() or max() functions.
# numbers = [5, 3, 2, 8, 9]


# def min_max(numbers):
#     new_dict = {"min": numbers[0], "max": numbers[0]}
#     for num in numbers:
#         if num > new_dict["max"]:
#             new_dict["max"] = num
#         elif num < new_dict["min"]:
#             new_dict["min"] = num
#     return new_dict


# result = min_max(numbers)
# logger.info(f"{result}")

# 6: Write a function that:Takes a list of numbers, Returns a dictionary with:"second_min": second smallest number, "second_max": second largest number,Do not use built-in functions like sorted(), min(), or max(), Make sure to handle edge cases (like if the list has less than 2 unique elements)

# numbers = [4, 7, 1, 9, 2, 5]


# # Expected output: {'second_min': 2, 'second_max': 7}
# def second_min_max(numbers):
#     unique_numbers = list(set(numbers))
#     print(unique_numbers)
#     if len(unique_numbers) < 2:
#         return {"second_min": None, "second_max": None}

#     return {"second_min": unique_numbers[1], "second_max": unique_numbers[-2]}


# result = second_min_max(numbers)
# logger.info(f"{result}")

# Day-8:
# Write a function that takes a list of integers and returns a dictionary with the counts of even and odd numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def odd_even_numbers(numbers):
#     new_dict = {"odd_numbers": 0, "even_numbers": 0}
#     for num in numbers:
#         if num % 2 == 0:
#             new_dict["even_numbers"] += 1
#         else:
#             new_dict["odd_numbers"] += 1
#     return new_dict


# result = odd_even_numbers(numbers)
# logger.info(f"{result}")

# 2: Write a function that takes a list of numbers and returns a new list with only the numbers divisible by 3.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def divisible_three(numbers):
#     new_list = []
#     for num in numbers:
#         if num % 3 == 0:
#             new_list.append(num)
#     return new_list


# result = divisible_three(numbers)
# logger.info(f"{result}")

# 3: Write a function that accepts two lists and returns a list of elements common to both, without duplicates.
# list_a = [1, 2, 3, 4, 5]
# list_b = [2, 4, 6, 8, 10]


# def new_list_set(list_a, list_b):
#     set_a = set(list_a)
#     set_b = set(list_b)
#     set_c = set_a.intersection(set_b)
#     return set_c


# result = new_list_set(list_a, list_b)
# logger.info(f"{result}")

# # 4: Write a function that takes a list of strings and returns a new list where words longer than 5 characters are capitalized.
# name = "Write a function that takes a list of strings and returns a new list where words longer than 5 characters are capitalized."


# def long_capitalized_words(name):
#     words = name.split()
#     new_list = []
#     for word in words:
#         if len(word) > 5:
#             new_list.append(word.upper())
#         else:
#             new_list.append(word)
#     return new_list


# result = long_capitalized_words(name)
# logger.info(f"{result}")

# # 5: Write a function that accepts an integer and returns the sum of its digits.

# # Example: sum_digits(1234) → 10
# numbers = 56789


# def sum_digits(numbers):
#     digits = []
#     total = 0
#     for digit in str(numbers):
#         digits.append(int(digit))

#     for num in digits:
#         total += num
#     return total


# result = sum_digits(numbers)
# logger.info(f"{result}")

# Day-09
# 1: Write a list comprehension to create a list of squares of even numbers between 1 and 20.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# result = [num**2 for num in numbers if num % 2 == 0]
# print(result)

# # 2: Write a function count_case(text) that returns a dictionary with the number of uppercase and lowercase letters in a string.
# text = "Write a function count_case that returns a dictionary with the number of uppercase and lowercase letters in a string."


# def count_case(text):
#     new_dict = {"uppercase": 0, "lowercase": 0}
#     for char in text:
#         if char.isupper():
#             new_dict["uppercase"] += 1
#         elif char.islower():
#             new_dict["lowercase"] += 1
#     return new_dict


# result = count_case(text)
# logger.info(f"{result}")
# # 3: Write a function reverse_words(sentence) that takes a string and returns a new string with the words reversed (not the characters).
# sentence = "Hello, I am from this World"


# def reverse_words(sentence):
#     words = sentence.split()  # split() breaks the sentence into a list of words.
#     reverse_words = words[::-1]  # [::-1] reverses the list.
#     return " ".join(reverse_words)  # " ".join() combines the list back into a string.


# result = reverse_words(sentence)
# logger.info(f"{result}")

# # 4: Write a function that takes a list of words and returns only the words with 3 or fewer characters.
# sentence = "Hello, I am from this World"


# def long_words(sentence):
#     words = sentence.split()
#     new_list = []
#     for word in words:
#         if len(word) <= 3:
#             new_list.append(word)
#     return new_list


# result = long_words(sentence)
# logger.info(f"{result}")

# # 5: Write a function that takes two strings and returns a list of common characters (without duplicates).
# a = "Hello Dear"
# b = "I am good"


# def common_characters(a, b):
#     set_a = set(a)
#     set_b = set(b)
#     set_c = set_a.intersection(set_b)
#     return list(set_c)


# result = common_characters(a, b)
# logger.info(f"{result}")

# Day-10
# 1: Write a function that takes a string and returns True if it’s a palindrome (ignoring spaces and case), otherwise False.
# Example: "Racecar" → True
# s = "level"


# def is_palindrome(s):
#     new_string = s.replace(" ", "").lower()
#     if new_string == new_string[::-1]:
#         return True
#     else:
#         return False
#     return new_string


# result = is_palindrome(s)
# logger.info(result)

# 2: Write a function that merges two lists by taking elements alternately.
# Example: [1,2,3], ['a','b','c'] → [1, 'a', 2, 'b', 3, 'c']
# a = [1, 2, 3]
# b = ["a", "b", "c"]


# def merge_fun(a, b):
#     new_list = []
#     for pair in zip(a, b):
#         for item in pair:
#             new_list.append(item)
#     return new_list


# result = merge_fun(a, b)
# print(result)

# 3: Write a function that removes all punctuation from a string.
# # Example: "Hello, world! Let's code." → "Hello world Lets code"
# import string

# text = "Hello, world! Let's code."


# def remove_punctuation(text):
#     clean_text = ""
#     clean_text = text.translate(str.maketrans("", "", string.punctuation))
#     return clean_text


# result = remove_punctuation(text)
# logger.info(f"{result}")


# 4: Write a function that takes a list and a value, and returns all indices where that value occurs.
# Example: [1, 2, 3, 2, 4], 2 → [1, 3]
# numbers = [1, 2, 3, 2, 4]


# def get_index(numbers):
#     result = []
#     for index, num in enumerate(numbers):
#         result.append(f"Index {num}:{index}")
#     return result


# result = get_index(numbers)
# logger.info(f"{result}")


# 5: Write a function that returns True if all characters in a string are unique, otherwise False.
# Example: "abcde" → True, "hello" → False
# words = "Hello"


# def unique_word(words):
#     result = set()
#     for word in words:
#         if word in result:
#             return False
#         result.add(word)
#     return True


# result = unique_word(words)
# logger.info(f"{result}")

# 6: Return all indices of a value in a list, # Example: [1, 2, 3, 2, 4], 2 → [1, 3]
# numbers = [1, 2, 3, 2, 4]
# value = 2


# def find_indices(numbers, value):
#     result = []
#     for index, num in enumerate(numbers):
#         if num == value:
#             result.append(index)
#     return result


# result = find_indices(numbers, value)
# logger.info(f"{result}")

# 7: Try writing a function that returns True if all characters in a string are unique (no duplicates).
# Example:"abcde" → True, "hello" → False
# words = "hello"


# def is_unique(words):
#     result = set()
#     for word in words:
#         if word in result:
#             return False
#         result.add(word)
#     return True


# result = is_unique(words)
# logger.info(f"{result}")  # Expected: False

# 8: Write a function that removes all vowels from a string.
# Example: "Beautiful Day" → "Btfl Dy"
# import string

# text = "Beautiful Day"


# def clean_vowel(text):
#     new_str = ""
#     vowels = "aeiouAEIOU"
#     for letter in text:
#         if letter not in vowels:
#             new_str += letter
#     return new_str


# result = clean_vowel(text)
# logger.info(f"{result}")

# 9: Write a function that merges two lists alternately, but handles lists of different lengths.
# Example: [1, 2, 3] and ['a', 'b'] → [1, 'a', 2, 'b', 3]

# from itertools import zip_longest

# a = [1, 2, 3]
# b = ["a", "b"]


# def merge_list(a, b):
#     new_list = []
#     for pair in zip_longest(a, b):
#         for item in pair:
#             if item not in new_list:
#                 new_list.append(item)
#     return new_list


# result = merge_list(a, b)
# logger.info(f"{result}")

# 10: Write a function that returns the first non-repeating character in a string.Example: "aabbcde" → "c", If none, return None.


# letters = "aabbccdde"


# def non_repeat_char(letters):
#     count = Counter(letters)
#     for letter in letters:
#         if count[letter] == 1:
#             return letter
#     return None


# result = non_repeat_char(letters)
# logger.info(f"{result}")

# 11: Write a function that takes two lists and returns a list of unique common elements.
# list1 = [1, 2, 2, 3, 4]
# list2 = [2, 3, 5]


# Output → [2, 3]
# def unique_list(list1, list2):
#     list3 = set(list1).intersection(set(list2))
#     return list3


# result = unique_list(list1, list2)
# logger.info(f"{(list(result))}")

# 12: Write a function that removes all vowels (a, e, i, o, u) from a given string (case-insensitive).
# Example:
# Input: "Beautiful Day"
# Output: "Btfl Dy"
# sentence = "Beautiful Day"


# def remove_vowels(sentence):
#     vowels = "aeiouAEIOU"
#     output = ""

#     for char in sentence:
#         if char not in vowels:
#             output += char
#     return output


# result = remove_vowels(sentence)
# logger.info(f"{result}")

# 13: Write a function to flatten a nested list of lists into a single list.
# Example:Input: [[1, 2], [3, 4], [5]], Output: [1, 2, 3, 4, 5]
# numbers = [[1, 2], [3, 4], [5]]


# def nested_list(numbers):
#     flat_list = []
#     for sub_list in numbers:
#         for num in sub_list:
#             flat_list.append(num)
#     return flat_list


# result = nested_list(numbers)
# logger.info(f"{result}")

# 14: Write a function that takes a sentence and returns a dictionary with the frequency of each word.
# Example:Input: "this is a test this is only a test"
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

# input = "this is a test this is only a test"


# def word_frequency(input):
#     words = input.split()
#     new_dict = {}
#     for word in words:
#         if word in new_dict:
#             new_dict[word] += 1
#         else:
#             new_dict[word] = 1
#     return new_dict


# result = word_frequency(input)
# logger.info(f"{result}")

# 15: Write a function that converts a sentence to title case (capitalize the first letter of each word).
# Example:Input: "python is fun"
# Output: "Python Is Fun"

# input = "python is fun"


# def title_case(input):
#     s = input.title()
#     return s


# result = title_case(input)
# logger.info(f"{result}")

# 16: Write a function that reverses the words in a sentence, not the characters.
# input = "Hello world this is fun"
# output = "fun is this world Hello"


# def reverse_sentence(input):
#     words = input.split()
#     reverse_words = words[::-1]
#     return " ".join(reverse_words)


# result = reverse_sentence(input)
# logger.info(f"{result}")

# 17: Write a function that returns a dictionary showing how many times each character appears in a string (ignore case and spaces).
# input = "Aa Bb Aa"
# # output = {"a": 4, "b": 2}


# def count_char(input):
#     new_dict = {}
#     for char in input.lower():
#         if char == " ":
#             continue
#         if char in new_dict:
#             new_dict[char] += 1
#         else:
#             new_dict[char] = 1
#     return new_dict


# result = count_char(input)
# logger.info(f"{result}")

# 18: Write a function that returns a dictionary: {"vowels": X, "consonants": Y} for a given string (only letters count).
# input = "Hello, World!"
# # output = {'vowels': 3, 'consonants': 7}


# def count_vowels_consonants(input):
#     vowels = "aeiou"
#     new_dict = {"vowels": 0, "consonants": 0}
#     for word in input.lower():
#         if word.isalpha():
#             if word in vowels:
#                 new_dict["vowels"] += 1
#             else:
#                 new_dict["consonants"] += 1
#     return new_dict


# result = count_vowels_consonants(input)
# logger.info(f"{result}")

# 19: Write a function that returns the longest word from a sentence. If multiple, return the first.
# input = "This is a programming challenge"


# # output = "programming"
# def length_of_words(input):
#     words = input.split()
#     output = ""
#     for word in words:
#         if len(word) > len(output):
#             output = word
#     return output


# result = length_of_words(input)
# logger.info(f"{result}")

# 20: Write a function that returns the elements common to two lists — including how many times they repeat (minimum match).


# list1 = [1, 2, 2, 3]
# list2 = [2, 2, 4]


# # output = [2, 2]
# def common_char(list1, list2):
#     count1 = Counter(list1)
#     count2 = Counter(list2)
#     result = []

#     for num in count1:
#         if num in count2:
#             result.extend([num] * min(count1[num], count2[num]))
#     return result


# result = common_char(list1, list2)
# logger.info(f"{result}")

# Day-11
# 1: Write a function that takes a sentence and returns the most frequent word in it.
# Ignore punctuation and make the comparison case-insensitive.
# sentence = "The sun shines over the lake, and the sun is bright."
# Output: "the"


# def repeat_words(sentence):
#     clean = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
#     words = clean.split()
#     count = Counter(words)
#     most_common = count.most_common(1)[0][0]
#     return most_common


# result = repeat_words(sentence)
# logger.info(f"{result}")

# 2: Write a function that removes duplicates from a list but preserves the original order of elements.
# input = [1, 2, 2, 3, 1, 4]


# def remove_dupes(input):
#     new_list = []
#     for num in input:
#         if num not in new_list:
#             new_list.append(num)
#     return new_list


# result = remove_dupes(input)
# logger.info(f"{result}")

# 3: Write a function that counts how many times each character appears in a string, ignoring case and excluding spaces.
# input = "Hello World"


# def count_char(input):
#     new_input = {}
#     for char in input.lower():
#         if char == " ":
#             continue
#         if char in new_input:
#             new_input[char] += 1
#         else:
#             new_input[char] = 1
#     return new_input


# result = count_char(input)
# logger.info(f"{result}")

# 4: Write a function that takes a sentence and returns a new sentence with the order of words reversed, but the words themselves remain unchanged.
# input = "Python is awesome"


# def reversed_words(input):
#     words = input.split()
#     reverse = words[::-1]
#     return " ".join(reverse)


# result = reversed_words(input)
# logger.info(f"{result}")

# 5: You are given a list of integers from 1 to n, except one number is missing. Write a function to find the missing number.
# num = [1, 2, 4, 5]


# def find_missing(num):
#     expected = set(range(min(num), max(num) + 1))
#     actual = set(num)
#     missing = list(expected - actual)
#     return sorted(missing)


# result = find_missing(num)
# logger.info(f"{result}")

# 6: Check if a string is a palindrome (ignoring spaces and case)
# input = "Race car"


# def is_palindrome(input):
#     new_word = input.replace(" ", "").lower()
#     if new_word == new_word[::-1]:
#         return True
#     else:
#         return False


# result = is_palindrome(input)
# logger.info(f"{result}")

# 7:  Merge two dictionaries. If a key exists in both, sum their values
# dict1 = {"a": 2, "b": 3}
# dict2 = {"a": 4, "c": 5}


# def merge_dictionary(dict1, dict2):
#     new_dict = dict1.copy()
#     for key, value in dict2.items():
#         if key in new_dict:
#             new_dict[key] += value
#         else:
#             new_dict[key] = value
#     return new_dict


# result = merge_dictionary(dict1, dict2)
# logger.info(f"{result}")

# 8:Find the second highest number in a list
# input = [4, 1, 7, 3, 7, 2]


# def second_highest(input):
#     first = second = float("-inf")
#     for num in input:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#     return second if second != float("-inf") else None


# result = second_highest(input)
# logger.info(f"{result}")

# 9: Convert a list of words into a sentence with proper spacing and punctuation
# input = ["hello", "world"]


# def form_sentence(input):
#     sentence = " ".join(input)
#     s_capitalize = sentence.capitalize()
#     if not s_capitalize.endswith("."):
#         s_capitalize += "."
#     return s_capitalize


# result = form_sentence(input)
# logger.info(f"{result}")

# # 10: Count how many words start with each letter in a sentence
# input = "She sells sea shells by the seashore"


# def starts_with(input):
#     word_count = Counter()
#     cleaned = input.translate(str.maketrans("", "", string.punctuation)).lower()
#     words = cleaned.split()
#     for word in words:
#         first_letter = word[0]
#         word_count[first_letter] += 1
#     return word_count


# result = starts_with(input)
# logger.info(f"{result}")

# Day-12: Write a function that takes a string and returns a dictionary with the count of:
# Letters (A-Z, a-z)
# Digits (0-9)
# Special characters (anything else, excluding spaces)

# input = "Hello123! How are you? :)"


# def count_words(input):
#     letters = 0
#     digits = 0
#     specials = 0
#     for char in input:
#         if char.isalpha():
#             letters += 1
#         elif char.isdigit():
#             digits += 1
#         elif not char.isspace():
#             specials += 1
#     return {"letters": letters, "digits": digits, "specials": specials}


# result = count_words(input)
# logger.info(f"{result}")

# 2: Write a function that takes a string and returns the count of each vowel (a, e, i, o, u), case-insensitive.
# input = "Beautiful day in the neighborhood"


# # Output:
# # {'a': 2, 'e': 3, 'i': 3, 'o': 3, 'u': 2}
# def count_vowels(input):
#     sentence = input.lower()
#     new_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#     for word in sentence:
#         if word in new_dict:
#             new_dict[word] += 1
#     return new_dict


# result = count_vowels(input)
# logger.info(f"{result}")

# 3: Write a function that takes a sentence and returns a dictionary where each key is the length of the word, and the value is the number of words with that length.
# sentence = "This is an amazing day for programming"


# def lenght_of_words(sentence):
#     words = sentence.split()
#     new_dict = {}
#     for word in words:
#         length = len(word)
#         if length in new_dict:
#             new_dict[length] += 1
#         else:
#             new_dict[length] = 1
#     return new_dict


# result = lenght_of_words(sentence)
# logger.info(f"{result}")

# 4: Write a function that takes a sentence and returns the shortest and longest word(s) in it.
# sentence = "The quick brown fox jumps over the lazy dog"


# def lenght_of_words(sentence):
#     clean = sentence.translate(str.maketrans("", "", string.punctuation))
#     words = clean.split()
#     shortest_len = float("inf")
#     longest_len = 0
#     for word in words:
#         length = len(word)
#         if length < shortest_len:
#             shortest_len = length
#         if length > longest_len:
#             longest_len = length
#     result = {"shortest": [], "longest": []}

#     for word in words:
#         if len(word) == shortest_len:
#             result["shortest"].append(word)
#         if len(word) == longest_len:
#             result["longest"].append(word)
#     return result


# result = lenght_of_words(sentence)
# logger.info(f"{result}")

# 5: Write a function that takes a sentence and returns a dictionary where the keys are word lengths, and the values are lists of words that have that length.
# sentence = "The rain in Spain falls mainly in the plain"
# output{  3: ['The', 'rain', 'the'],  2: ['in', 'in'],  5: ['Spain', 'falls', 'plain'],  6: ['mainly']}


# def length_of_words(sentence):
#     clean = sentence.translate(str.maketrans("", "", string.punctuation))
#     words = clean.split()
#     new_dict = {}
#     for word in words:
#         length = len(word)
#         if length in new_dict:
#             new_dict[length].append(word)
#         else:
#             new_dict[length] = [word]
#     return new_dict


# result = length_of_words(sentence)
# logger.info(f"{result}")
