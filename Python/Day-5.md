from loguru import logger

# Create a script that writes the following lines to a file named log.txt
Server started at 10:00 AM
Health check passed
Backup completed

log_lines = [
    "Server started at 10:00 AM",
    "Health check passed",
    "Backup completed"]

with open("log.txt", "w") as log_file: # Open the file in write mode and write each line
    for line in log_lines:
        log_file.write(line + "\n")

logger.info(f"Log written to log.txt")


# Read the contents of log.txt and print each line with line numbers prefixed like: 1: Server started at 10:00 AM

with open("log.txt", "r") as log_file:
    for idx, line in enumerate(log_file, start=1):
        print(f"{idx}: {line.strip()}")

# Check if a file named config.ini exists. If not, create it and write default content:
[server] port=8080

import os

filename = "config.ini"

# Check if the file exists
if not os.path.exists(filename):
    
    default_content = "[server]\nport=8080\n" # Default content
    
    
    with open(filename, "w") as file: # Create and write to the file
        file.write(default_content)
    
    print(f"{filename} created with default content.")
else:
    print(f"{filename} already exists.")

# Read the config.ini file and extract the port number using Python.

import configparser

config = configparser.ConfigParser() # Create a ConfigParser instance


config.read("config.ini") # Read the config.ini file


port = config.getint("server", "port") # Extract the port number

print(f"Port number is: {port}")


# Write a script that deletes a file temp.txt only if it exists. If it doesn’t, print a warning.

import os

filename = "temp.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print(f"Warning: {filename} does not exist.")