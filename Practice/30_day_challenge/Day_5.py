#  Write a function that computes the sum and average of a list of numbers

from loguru import logger

num_list = [1, 2, 3, 4, 5, 6]
total = 0

for item in num_list:
    total = total + item
logger.info(f"{total} is the total of num_list")

for item in num_list:
    ave = sum(num_list) / len(num_list)
logger.info(f"Average of the num_list is {ave}")
