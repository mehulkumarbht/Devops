import base64
import getpass
import json
import requests
from datetime import datetime
import socket
from loguru import logger

#1: Input a password from user. Prevent the entered password from being displayed on the screen. Encrypt it using base64 and store it locally in a text file.
password = getpass.getpass("Enter your password: ")

encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")

with open ("encoded_password","w") as file:
    file.write(encoded_password)

logger.info(f"Password saved in base64 format")

#2: Input password from user in the same manner, check the password by decrypting password saved in text file. Display success message if  password is correct.
file_name = "encoded_password.txt"

password = getpass.getpass("Enter your password: ")

encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")

with open (file_name, "r") as file:
    stored_password = file.read()

if stored_password == encoded_password:
    logger.info(f"Password is successfully verified")
else: 
    logger.info(f"Password verification failed")

#3: Use json.dumps() to log deployment data (e.g., timestamps, status, host) in a structured format.

deployment_data = {
    "timestamps": datetime.now().isoformat(),
    "status": "success",
    "host": socket.gethostname(),
    "service": "user-auth-api",
    "version": "v1.0.0"
}

json_log = json.dumps(deployment_data, indent=4)

with open ("deployment_date","a") as file:
    file.write(json_log + "\n")

#4: Use requests.get() to hit API: https://jsonplaceholder.typicode.com/users and extract values from the JSON response using the json module.

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = json.loads(response.text)

for user in users:
    logger.info(f"Name: {user['name']}")
    logger.info(f"Username: {user['username']}")
    logger.info(f"Email: {user['email']}")
    logger.info(f"City: {user['address']['city']}")
    logger.info(f"-" * 40)

#5: Write a function to check required keys ("host", "port", "auth") in a JSON config file.

def check_required_keys(config_path):
    required_keys = {"host", "port", "auth"}

    try:
        with open (config_path,"r") as file:
            config_data = json.load(file)

        missing_keys= required_keys - config_data.keys()

        if missing_keys:
            print(f"Missing required keys: {', '.join(missing_keys)}")
            return False
        else:
            print("All required keys are present")
            return True
    except FileNotFoundError :
        print(f"File not found: {config_path}")
        return False
    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {config_path}")
        return False
    
check_required_keys("config.json") 
