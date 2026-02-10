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
# c = int(input("Please add temperature in Celcius: "))
# f = c * 1.8 + 32
# logger.info(f"Temprature from Celsius to Fahrenheit is: {f}")

# 3: Ask for a name and age; print how old the person will be after 10 years.
# name = str(input("Please enter your name: "))
# age = int(input("Please enter your age: "))
# years_old = age + 10
# logger.info(f"{name} will be {years_old} years old after 10 years")

# 4: Swap two variables without using a third variable.
# a = 3
# b = 4
# a, b = b, a
# logger.info(f"{a}")
# logger.info(f"{b}")

# Day 2: Conditions (if / else)
# 1: Check whether a number is positive, negative, or zero.
# x = float(input("Please enter a digit: "))
# if x > 0:
#     logger.info(f"{x} is positive value")
# elif x < 0:
#     logger.info(f"{x} is negative value")
# else:
#     logger.info(f"{x} is zero")


# Check if a number is even or odd.
# x = float(input("Please enter a digit: "))
# if x % 2 == 0:
#     logger.info(f"Value is even")
# else:
#     logger.info(f"Value is odd")
# Find the largest of three numbers.
# x, y, z = 10, 20, 30
# largest = max(10, 20, 30)
# logger.info(f"{largest}")
# Write a program to check if a year is a leap year.
# year = int(input("Please enter a year: "))
# if year % 4 == 0:
#     logger.info(f"{year} is leap year")
# else:
#     logger.info(f"{year} is not leap year")


# Day 3: Loops (for, while)

# 1:Print numbers from 1 to 100.
# for i in range(1, 101):
#     logger.info(f"{i}")

# another way:
# i = 1
# while i < 101:
#     print(i)
#     i += 1


# 2: Print the sum of first n natural numbers.
# i = 1
# n_num = i * (i + 1) // 2
# logger.info(f"{n_num}")
# 3: Print the multiplication table of a given number.
# number = int(input("Please enter your number: "))
# for i in range(1, 11):
#     logger.info(f"{number} x {i} = {number * i}")
# 4: Reverse a number using a loop.
# n = int(input("Please enter a two digit number: "))
# if n > 9:
#     rev = int(str(n)[::-1])
#     logger.info(f"{rev}")
# else:
#     logger.info(f"Invalid entry!")

# Day 4: Loop Logic Practice
# 1: Count digits in a number.
# n = int(input("Please enter your number: "))
# num = len(str(abs(n)))
# logger.info(f"{num}")


# 2: Check if a number is a palindrome.
# n = int(input("Please enter your number: "))
# s = str(n)
# if s == s[::-1]:
#     logger.info(f"{s} is palindrome")
# else:
#     logger.info(f"{s} is not palindrome")


# 3: Print all prime numbers between 1 and 100.
# primes = []
# for num in range(2, 101):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)
# logger.info(f"{primes}")
# 4: Find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


logger.info(f"{factorial(12)}")
