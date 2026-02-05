from loguru import logger
# Day 1: Variables & Input

# 1: Take two numbers from user input and print their sum, difference, product, and division.
# x = int(input("Please provide first number: "))
# y = int(input("Please provide second number: "))
# Sum
# z = x + y
# logger.info(f"{z}")
# Difference
# a = x - y
# logger.info(f"{a}")
# product
# b = x * y
# logger.info(f"{b}")
# division
# c = x // y
# logger.info(f"{c}")

# 2: Convert a temperature from Celsius to Fahrenheit.
c = int(input("Please add temperature in Celcius: "))
f = c * 1.8 + 32
logger.info(f"Temprature from Celsius to Fahrenheit is: {f}")
