from datetime import date
from loguru import logger

#1: Input two numbers and calculate their sum.
num_1 = int(input())
num_2 = int(input())
final_number = num_1 + num_2
logger.info(f"{final_number}")

# #2: Compare two numbers and print which is greater.
num_1 = int(input())
num_2 = int(input())
higher = max(num_1,num_2)
logger.info(f"This is a higher number: {higher}")

# #3: Input a number from the user and print its square and cube.
num = int(input()) # Get input from the user

square = num ** 2 # Square the number
cube = num ** 3 # Cube the number

logger.info(f"Square of number is: {square}")
logger.info(f"Cube of the number is: {cube}")

# #4: Take the user's name and birth year as input, and calculate their age.

first_name= str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
birth_year = int(input("Enter your birth year: "))

current_year = date.today().year # get current year

age = current_year - birth_year # To get age, find difference between current year and birth age

logger.info(f"Hi {first_name} {last_name}, Your age is: {age}")
