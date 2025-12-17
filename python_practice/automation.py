from loguru import logger

# excercise:1
# num1 = float(input("Please add first number:"))
# num2 = float(input("Please add second number:"))
# name1 = str(input("Please add your first name:"))
# name2 = str(input("Please add your last name:"))
# cities = ["Toronto", "Delhi", "London"]
# Add = num1 + num2
# multiply = num1 * num2
# combine_name = name1 + name2
# logger.info(f"{Add}")
# logger.info(f"{multiply}")
# logger.info(f"{combine_name}")
# logger.info(f"{cities[0]}")
# logger.info(f"{cities[-1]}")

# excercise: 2
# name1 = str(input("Please Enter your first name:"))
# logger.info(f"Hello {name1}! Today you will learn Python Automation")

# Day-2
# 1:
# age1 = float(input("Please enter your age: "))
# if age1 >= 18:
#     logger.info(f"Eligible to vote")
# else:
#     logger.info(f"Not eligible")

# 2
# password = "admin123"
# pw = str(input("Please enter a password:"))
# if pw == password:
#     logger.info(f"Access granted")
# else:
#     logger.info(f"Access denied")

# 3:
# error_count = 7
# if error_count == 0:
#     logger.info(f"System healthy")
# elif error_count <= 5:
#     logger.info(f"Minor issue")
# else:
#     logger.info(f"Critical issue - alert admin")

# 4:
# name1 = str(input("Please add your name: "))
# hours_worked = float(input("Enter number of hours worked:"))
# if hours_worked > 8:
#     logger.info(f"Overworking is detected")
# else:
#     logger.info(f"Work-life balance is good")
# logger.info(f"{name1}, keep improving your automation skills!")

# day-3:
# 1:
# automation_tasks = ["backup files", "send report", "check logs"]
# for task in automation_tasks:
#     logger.info(f"Executing: {task}")

# 2:
# for i in range(1, 11):
#     logger.info(f"{i}")

# 3:
# retry = 1
# while retry <= 3:
#     logger.info(f"Retry attempt: 1")
#     retry += 1

# 4:
# files = ["data1.csv", "data2.csv", "data3.csv"]
# for file in files:
#     logger.info(f"Processing: {file}")
# logger.info("All files processed successfully")


# day-4:
# 1:
# def print_status():
#     logger.info("Automation script running...")

# 2:
# def check_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# result = check_even(5)
# logger.info(f"{result}")


# 3:
# def process_files(files):
#     for file in files:
#         logger.info(f"Processing: {file}")
#     return "All files processed successfully"


# result = process_files("file_1")
# logger.info(f"Final result: {result}")


# 4:
def send_notification(name):
    logger.info(f"Notification sent to {name}")


users = ["Admin", "Manager", "Support"]
for user in users:
    send_notification(user)
