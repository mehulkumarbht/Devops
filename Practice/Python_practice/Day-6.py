from loguru import logger

#1: Take user input for two integers and divide them. 
# Handle: ValueError if input is not an integer, ZeroDivisionError for division by zero.

try:
    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))
    final_num = num_1/num_2
    logger.info(f"{final_num}")
except ValueError:
    logger.info(f"Error: Please add valid integer")
except ZeroDivisionError:
    logger.info(f"Error: Division by zero is not allowed")

#2: Try to open a file named important_config.txt. 
# If it doesn’t exist, print "Config file not found!" instead of crashing
# Modify the previous task and add a finally block to print "Operation complete" no matter what happens.

try:
    with open ("important_config.txt", "r") as file:
        content = file.read()
        logger.info(f"{content}")
except FileNotFoundError:
    logger.info(f"File not found!")

finally:
    logger.info(f"Operation complete!")

#3: Create a custom exception class InvalidPortException. Raise it if a given port number is not in the range 1-65535
# Define the custom exception
class InvalidPortException(Exception):
    def __init__(self, port, message="Port number must be between 1 and 65535"):
        self.port = port
        self.message = message
        super().__init__(f"{message}: {port}")

# Function to validate port
def validate_port(port):
    if not (1 <= port <= 65535):
        raise InvalidPortException(port)
    else:
        print(f"Port {port} is valid.")

##Example usage
try:
    user_port = int(input("Enter a port number: "))
    validate_port(user_port)
except InvalidPortException as e:
    print(f"InvalidPortException caught: {e}")
except ValueError:
    print("Please enter a valid integer.")


#4: Try to delete a file using os.remove() and handle PermissionError, FileNotFoundError, and generic OSError
import os

filename = "import_config.txt"  # Replace with the file you want to delete

try:
    os.remove(filename)
    logger.info(f"{filename} has been deleted.")

except FileNotFoundError:
    logger.info(f"Error: {filename} not found.")

except PermissionError:
    logger.info(f"Error: Permission denied to delete {filename}.")

except OSError as e:
    logger.info(f"Error: Failed to delete {filename}. Reason: {e}")
