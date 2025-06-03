from loguru import logger
from datetime import datetime

#1: Printing and Variables, Create two variables: name = "Alice" and age = 30.

##Print:
##"Hello, my name is Alice and I am 30 years old."
##(Make it dynamic using the variables.)

name = "Alice"
age = 30
logger.info(f"Hello, my name is {name} and I am {age} years old")

#2: Input and Type Conversion

##Write a script that: Asks the user for their birth year. Calculates their age in 2025.Prints: "You will be X years old in 2025."
birth_year = int(input("Enter your birth year: " ))
current_year = datetime.now().year
age = current_year - birth_year

logger.info(f"You will be {age} years old in 2025")

#3: Lists and Indexing: Create a list of five fruits.Print the first and last fruit.
#Replace the third fruit with "kiwi" and print the updated list.
fruit_list = ["apple", "banana", "cherry", "berry", "mango"]
print(fruit_list)

print(fruit_list[0])
print(fruit_list[-1])
fruit_list[2] = "kiwi"
print(fruit_list)

#4: If-Else Conditions: Write a script that checks if a number is even or odd.
# If even, print "This is an even number."
# If odd, print "This is an odd number."

num = int(input("Please add a number: "))
if num % 2 ==0:
    logger.info("This is an even number")
else:
    logger.info("This is an odd number")

#5: Simple Function: Define a function greet_user(name) that prints:"Welcome, <name>!"Call it with your own name.
def greet_user(name):
    logger.info(f"Welcome, {name}!")

greet_user("Sarah")