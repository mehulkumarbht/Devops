from loguru import logger
import re
# Day:1: Convert normal loops into list comprehensions.

# 1: Create a list of numbers from 1 to 10 using list comprehension.
# number_list = [n for n in range(1, 11)]
# logger.info(f"{number_list}")

# 2: Generate a list of their squares.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# squares = [n**2 for n in numbers]
# logger.info(f"{squares}")

# 3: Make a list of only even numbers from 1 to 20.
# evens = [n for n in range(1, 21) if n % 2 == 0]
# logger.info(f"{evens}")

# 4: Create a list of strings: ["Hello 1", "Hello 2", ..., "Hello 5"].
# list_of_string = [f"Hello {n}" for n in range(1, 6)]
# logger.info(f"{list_of_string}")
# list_of_string = []
# for n in range(1, 6):
#     list_of_string.append(f"Hello {n}")
# logger.info(f"{list_of_string}")

# 5: Convert each word in ["apple", "banana", "cherry"] to uppercase using list comprehension.
# fruits = ["apple", "banana", "cherry"]
# upper_list = [word.upper() for word in fruits]
# logger.info(f"{upper_list}")

# Day-2:Add filters (if) and transformations.
# 1: From numbers 1–15, create a list of squares only for odd numbers.
# squares = [n**2 for n in range(1, 16) if n % 2 != 0]
# logger.info(f"{squares}")

# 2: Replace numbers 1–10 with "even" or "odd" strings depending on the number.
# even_odd = ["even" if n % 2 == 0 else "odd" for n in range(1, 11)]
# logger.info(f"{even_odd}")

# 3: Given words = ["cat", "house", "dog", "elephant"], create a list of words with length > 3.
# words = ["cat", "house", "dog", "elephant"]
# wordslist = [word for word in words if len(word) > 3]
# logger.info(f"{wordslist}")

# 4: From words, create a list of their first letters.
# words = ["cat", "house", "dog", "elephant"]
# first_letters = [word[0] for word in words]
# logger.info(f"{first_letters}")

# 5: Flatten a 2D list: [[1,2], [3,4], [5,6]] → [1,2,3,4,5,6].
# num_list = [[1, 2], [3, 4], [5, 6]]
# flatten = [num for row in num_list for num in row]
# logger.info(f"{flatten}")

# Day-3: Practice nesting and combining.
# 1: Create a multiplication table for numbers 1–5 (like [1,2,3,4,5,2,4,6,...]).
# table = [m * n for m in range(1, 6) for n in range(1, 6)]
# logger.info(f"{table}")

# 2: Create all pairs (x, y) where x is from [1,2,3] and y is from [‘a’, ‘b’].
# num = [1, 2, 3]
# char = ["a", "b"]
# pairs = [(x, y) for x in num for y in char]
# logger.info(f"{pairs}")

# 3: Given a sentence "the quick brown fox", split into words and make a list of their lengths.
# sentence = "the quick brown fox"
# words = sentence.split()
# length_of_words = [len(word) for word in words]
# logger.info(f"{length_of_words}")

# 4: Extract vowels from "programming is fun" into a list.
# vowels = "aeiou"
# sentence = "programming is fun"
# vowles_list = [word for word in sentence if word in vowels]
# logger.info(f"{vowles_list}")

# 5: From nums = [0,1,2,3,4,5,6,7,8,9], build a list that keeps numbers < 5 as is, but replaces numbers ≥ 5 with "big".
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums_list = ["big" if n >= 5 else n for n in nums]
# logger.info(f"{nums_list}")

# Day-4:
# 1: Extract numbers from a string
# text = "Order IDs are: 23, 45, 67, and 89"
# # Expected: [23, 45, 67, 89]
# number_as_string = re.findall(
#     r"\d+", text
# )  # Extract all sequences of one or more digits
# number_as_integer = [
#     int(num) for num in number_as_string
# ]  # Convert the extracted strings to integers
# logger.info(f"{number_as_integer}")

# 2: Flatten + filter logs
# logs = [
#     ["INFO: Start", "ERROR: Disk full"],
#     ["INFO: Running", "ERROR: Timeout"],
#     ["INFO: Finished"],
# ]
# # Expected: ['Disk full', 'Timeout']   (only error messages, without 'ERROR:')
# errors = [
#     msg.replace("ERROR: ", "")
#     for sublist in logs
#     for msg in sublist
#     if msg.startswith("ERROR:")
# ]
# logger.info(f"{errors}")

# 3: Unique words, lowercase, no stopwords
# sentence = "The quick brown fox jumps over the lazy dog"
# stopwords = {"the", "over"}
# # Expected: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']
# words = sentence.lower().split()
# cleaned_words = [word for word in words if word not in stopwords]
# logger.info(f"{cleaned_words}")

# 4: Transpose a matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
# # Expected: [[1, 4], [2, 5], [3, 6]]
# transpose_matrix = [list(row) for row in zip(*matrix)]
# logger.info(f"{transpose_matrix}")

# 5: Dictionary from two lists
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "Toronto"]
# # Expected: {'name': 'Alice', 'age': 25, 'city': 'Toronto'}
# my_dict = dict(zip(keys, values))
# logger.info(f"{my_dict}")

# Day-5:
# 1: Word frequency counter
# sentence = "apple banana apple orange banana apple"
# from collections import Counter
# words = sentence.split()
# counter = Counter(words)
# logger.info(f"{counter}")

# 2: Reverse dictionary
# students = {"Alice": 25, "Bob": 30, "Charlie": 35}
# reverse_students = {value: key for key, value in students.items()}
# logger.info(f"{reverse_students}")

# 3: Filter dictionary
# scores = {"Alice": 85, "Bob": 60, "Charlie": 95, "Dave": 40}
# high_scores = {key: value for key, value in scores.items() if value >= 70}
# logger.info(f"{high_scores}")

# 4: From the word "programming", build a set of all unique consonants (exclude vowels).
# word = "programming"
# vowels = "aeiou"
# unique_consonants = {char for char in word if char not in vowels}
# logger.info(f"{unique_consonants}")

# 5: Convert into a dictionary where keys are column indexes and values are lists of column elements.
matrix = [[1, 2], [3, 4], [5, 6]]
transposed_matrix = {i: [row[i] for row in matrix] for i in range(len(matrix[0]))}
logger.info(f"{transposed_matrix}")
