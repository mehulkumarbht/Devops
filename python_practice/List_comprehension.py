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
