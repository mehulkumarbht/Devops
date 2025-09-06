# from loguru import logger
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
