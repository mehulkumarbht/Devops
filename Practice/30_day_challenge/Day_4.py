# Day-4 Check if user entered number is prime?

from loguru import logger


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))

if is_prime(num):
    logger.info(f"{num} is prime number")
else:
    logger.info(f"{num} is not prime number")
