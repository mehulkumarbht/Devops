from loguru import logger
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
table = [m * n for m in range(1, 6) for n in range(1, 6)]
logger.info(f"{table}")

# 2: Create all pairs (x, y) where x is from [1,2,3] and y is from [‘a’, ‘b’].
num = [1, 2, 3]
char = ["a", "b"]
pairs = [(x, y) for x in num for y in char]
logger.info(f"{pairs}")

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
