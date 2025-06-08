from loguru import logger
## Write a script that calculates the sum of the first n natural numbers using a loop.
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1,n+1): # loop from 1 to n (inclusive)
    total += i

logger.info(f"Sum of the first(n) natural number is: {total}")

# ## Write a program to print the multiplication table of a given number using a for loop.

num = int(input("Please input a number to get its multiplication table: "))
logger.info(f"\nMultiplication Table of {num}:\n")
for i in range(1,11):
    logger.info(f"{num}*{i} = {num*i}")

# ## Create a countdown timer using a while loop from 10 to 1, then print "Blast off!"
countdown=10
while countdown > 0:
    logger.info(f"{countdown}")
    time.sleep(1) # wait for a second
    countdown -= 1 # decrease count by 1
logger.info(f"Blast off!")