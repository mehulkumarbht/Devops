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
text = "apple banana apple orange banana apple"


def count_words(text):
    word_count = {}
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


result = count_words(text)
print(result)

# Write a function called get_max_value(d) that:Receives a dictionary where keys are strings and values are numbers.Returns the key with the highest value.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}


def get_max_value(scores):
    highest_key = None
    highest_value = 0
    for key, value in scores.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
    return highest_key


result = get_max_value(scores)
logger.info(f"{result}")

# Print each student’s name and their average grade
grades = {"Alice": [85, 90, 88], "Bob": [72, 75, 70], "Charlie": [95, 100, 98]}
avg = 0
for key, value in grades.items():
    avg = sum(value) / len(value)
    logger.info(f"{key}: {avg:.2f}")

# Write a function create_dict(keys, values) that:Receives two lists.Returns a dictionary pairing keys and values.
keys = ["id", "name", "age"]
values = [1, "Alice", 30]


def creat_dict(keys, values):
    new_dict = {}

    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]

    for key, value in new_dict.items():
        logger.info(f"{key}:{value}")
    return new_dict


result = creat_dict(keys, values)
logger.info(f"{result}")


def creat_dict(keys, values):
    new_dict = {}
    for k, v in zip(keys, values):
        new_dict[k] = v
    logger.info(f"{keys}:{values}")
    return new_dict


result = creat_dict(keys, values)
logger.info(f"{result}")

# Write code to create a new dictionary containing only items where the quantity > 0.
inventory = {"apple": 5, "banana": 0, "orange": 3, "kiwi": 0}
positive_inventory = {}
for key, value in inventory.items():
    if value > 0:
        positive_inventory[key] = value
logger.info(f"{positive_inventory}")
