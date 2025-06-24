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
