#OS Module

#1: List all files and directories in a given path

import os
from loguru import logger

path = "C:/Users/Documents/Programming"
try:
    items = os.listdir(path)
    logger.info(f"Contents of {path}")
    for item in items:
        logger.info(f"{item}")
except FileNotFoundError:
    logger.info(f"File not found!")
except PermissionError:
    logger.info(f"Permission denied to {path}!")

#2: Delete a file or directory
file = "C:/Users/Documents/Programming/scraper.py"
try:
    os.remove(file)
    logger.info(f"File {file} deleted successfully")
except PermissionError:
    logger.info(f"Permission denied to delete {file}")

#3: Print all environment variables

for key,value in os.environ.items():
    logger.info(f"These are the env variables {key}: {value}")

#4: Set a custom environment variable, DB_ADMIN as user(Extract user from environment variables)
import os

current_user = os.getenv("USERNAME")

if current_user:
    os.environ["DB_ADMIN"] = current_user
    logger.info(f"DB_ADMIN set to: {os.environ['DB_ADMIN']}")
else:
    logger.info(f"Error: Couldn't find current user")

#5: Install curl using os module
import os

os.system("sudo apt update && sudo apt install -y curl")
#6: Create a script that checks disk usage by calling df -h using os module

import os
os.system("df -h")

