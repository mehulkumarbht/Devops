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
# matrix = [[1, 2], [3, 4], [5, 6]]
# transposed_matrix = {i: [row[i] for row in matrix] for i in range(len(matrix[0]))}
# logger.info(f"{transposed_matrix}")

# Day-6:
# 1: Write a list comprehension that generates squares of numbers 1–10.
# squares = [num**2 for num in range(1, 11)]
# logger.info(f"{squares}")
# bonus: extract only the even squares.
# even_squares = [num**2 for num in range(1, 11) if num % 2 != 0]
# logger.info(f"{even_squares}")
# 2: From ["cat", "house", "dog", "elephant"], keep only words with length > 3.
# words = ["cat", "house", "dog", "elephant"]
# long_words = [word for word in words if len(word) > 3]
# logger.info(f"{long_words}")

# bonus: collect only their first letters.
# first_letters = [word[:1] for word in words]
# logger.info(f"{first_letters}")

# Day-7
# 1: Build a list of each word’s length.
# sentence = "The quick brown fox jumps over the lazy dog"
# words = sentence.split()
# length_words = [len(word) for word in words]
# logger.info(f"{length_words}")
# bonus:build a dict {word: length}
# length_words = {word: len(word) for word in words}
# logger.info(f"{length_words}")

# 2: From "programming", build a set of all unique consonants.
# word = "programming"
# vowels = "aeiou"
# number_of_consonants = [char for char in word if char not in vowels]
# logger.info(f"{number_of_consonants}")

# bonus: count vowels vs consonants
# number_of_vowels = sum([1 for char in word if char in vowels])
# number_of_consonants = sum([1 for char in word if char not in vowels])
# logger.info(f"Number of vowels: {number_of_vowels}")
# logger.info(f"Number of consonants: {number_of_consonants}")


# Day-8:
# 1: Extract error messages only (remove "ERROR:").
# import re

# logs = ["INFO: Start", "ERROR: Disk full", "INFO: Run", "ERROR: Timeout"]
# error = []
# for line in logs:
#     match = re.search(r"ERROR: (.*)", line)
#     if match:
#         error.append(match.group(1))
# logger.info(f"{error}")
# Bonus: build a dict {level: [messages...]}.
# error = {}
# for line in logs:
#     level, message = line.split(":", 1)
#     error.setdefault(level, []).append(message)
# logger.info(f"{error}")

# Day-09
# Choose one of these:
# Word analyzer: word → length, frequency, unique letters.
# Mini CSV transformer: list of strings → list of dicts.
# Log summary: count INFO, ERROR, WARNING.

# Word Analyzer:
# word = "banana"

# word_length = len(word)
# logger.info(f"{word_length}")
# word_frequency = sum[1 for char in word if char == word_frequency[char]]
# logger.info(f"{word_frequency}")

# word_frequency = {}
# for char in word:
#     if char in word_frequency:
#         word_frequency[char] += 1
#     else:
#         word_frequency[char] = 1
# logger.info(f"{word_frequency}")

# word_unique = set(word)
# logger.info(f"{word_unique}")

# logs = ["INFO: Start", "ERROR: Disk full", "INFO: Run", "WARNING: Low memory"]

# log_dict = {}
# for line in logs:
#     level, message = line.split(":", 1)
#     log_dict.setdefault(level, []).append(message)
# logger.info(f"{log_dict}")

# Day-10
# Mini Word Analyzer
# Take an input word and produce:Length of the word, Unique letters, Frequency of each letter
# word = "Programming"
# words = word.lower()
# words_length = len(words)  # length of the word
# logger.info(f"{words_length}")
# unique_letters = set(words)
# logger.info(f"{unique_letters}")
# frequency_letters = {}
# for word in words:
#     if word in frequency_letters:
#         frequency_letters[word] += 1
#     else:
#         frequency_letters[word] = 1
# logger.info(f"{frequency_letters}")

# Mini CSV Transformer
# data = ["name,age,city", "Alice,25,Toronto", "Bob,30,New York", "Charlie,35,London"]
# headers = data[0].split(",")
# rows = data[1:]
# result = [dict(zip(headers, row.split(","))) for row in rows]
# logger.info(f"{result}")

# older_than_30 = [
#     dict(zip(headers, row.split(","))) for row in rows if int(row.split(",")[1]) > 30
# ]
# logger.info(f"{older_than_30}")

# Day-11:
# 1: Group People by City
# result = [
#     {"name": "Alice", "age": "25", "city": "Toronto"},
#     {"name": "Bob", "age": "30", "city": "New York"},
#     {"name": "Charlie", "age": "35", "city": "London"},
#     {"name": "Dave", "age": "32", "city": "New York"},
# ]
# grouped_by_city = {}
# for row in result:
#     city = row["city"]
#     name = row["name"]
#     grouped_by_city.setdefault(city, []).append(name)
# print(grouped_by_city)

# 2: Log Summary Generator
# logs = [
#     "INFO: System started",
#     "ERROR: Disk full",
#     "WARNING: Low memory",
#     "INFO: Running task",
#     "ERROR: Timeout",
#     "INFO: Completed",
# ]
# log_summary = {}
# for line in logs:
#     level, message = line.split(": ", 1)
#     log_summary[level] = log_summary.get(level, 0) + 1
# logger.info(f"{log_summary}")

# 3: Error log extractor
logs = [
    "INFO: System started",
    "ERROR: Disk full",
    "WARNING: Low memory",
    "INFO: Running task",
    "ERROR: Timeout",
    "INFO: Completed",
]
log_summary = []
for line in logs:
    if line.startswith("ERROR:"):
        message = line.split(":", 1)[1]
        log_summary.append(message)
logger.info(f"{log_summary}")
