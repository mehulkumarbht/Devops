from loguru import logger

#1: Create a script that writes the following lines to a file named log.txt
# Server started at 10:00 AM
# Health check passed
# Backup completed

log_lines = [
    "Server started at 10:00 AM",
    "Health check passed",
    "Backup completed"]

# Open the file in write mode and write each line
with open("log.txt", "w") as log_file:
    for line in log_lines:
        log_file.write(line + "\n")

logger.info(f"Log written to log.txt")


#2: Read the contents of log.txt and print each line with line numbers prefixed like: 1: Server started at 10:00 AM

with open("log.txt", "r") as log_file:
    for idx, line in enumerate(log_file, start=1):
        print(f"{idx}: {line.strip()}")

#3:Append a new entry like "Deployment completed at 11:00 AM" to log.txt.
with open("log.txt", "a") as file:
    file.write("Deployment completed at 11:00 AM \n")

with open("log.txt","r") as file:
    lines = file.readlines()
    if lines:
        logger.info(f"Last line in log.txt:, {lines[-1].strip()}")
    else:
        logger.info(f"Last line was not added")

#4: Check if a file named config.ini exists. If not, create it and write default content:[server], port=8080

import os

# File name
filename = "config.ini"

# Check if the file exists
if not os.path.exists(filename):
    # Default content
    default_content = "[server]\nport=8080\n"
    
    # Create and write to the file
    with open(filename, "w") as file:
        file.write(default_content)
    
    logger.info(f"{filename} created with default content.")
else:
    logger.info(f"{filename} already exists.")

#5: Read the config.ini file and extract the port number using Python.

import configparser

##Create a ConfigParser instance
config = configparser.ConfigParser()

##Read the config.ini file
config.read("config.ini")

##Extract the port number
port = config.getint("server", "port")

print(f"Port number is: {port}")


#6: Write a script that deletes a file temp.txt only if it exists. If it doesn’t, print a warning.

import os

filename = "temp.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print(f"Warning: {filename} does not exist.")



