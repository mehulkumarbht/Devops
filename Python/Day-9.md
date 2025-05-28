from loguru import logger
import platform
import socket
import subprocess
import os

# 1: Collect all platform info like OS name, release, version, machine type,  hostname and architecture.Save it in system_info.txt.

info = {"OS Name": platform.system(),

        "OS Release": platform.release(),
		
        "OS Version": platform.version(),
		
        "Machine Type": platform.machine(),
		
        "Architecture" : platform.architecture()[0],
		
        "Hostname": socket.gethostname()}

* Save to system_info.txt

with open("system_info.txt", "w") as file:

    file.write("=== System information ===\n")
	
    for key, value in info.items():
	
        file.write(f"{key} : {value}\n")
		
logger.info("File saved as System_info.txt")

#2: Ping google.com and save the output to ping_log.txt.

command = ["ping", "google.com", "-c", "4"]

with open ("ping_log.txt","w") as file:

    subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)

logger.info(f"File saved as ping_log.txt")

#3: Check the running process and parse output to find if nginx, python, or mysqld is running

targets = ["nginx", "python", "mysqld"]

found = {service: False for service in targets}

result = subprocess.run(["tasklist"], stdout=subprocess.PIPE, text=True)

for line in result.stdout.splitlines():
    for service in targets:
        if service.lower() in line.lower():
            found[service] = True

logger.info("=== Process Check ===")
for service, status in found.items():
    logger.info(f"{service}: {'Running' if status else 'Not Running'}")

#4: Write a script that accepts two numbers as arguments and prints their sum.
try:
    num_1 = float(input("Please enter first number: "))
    num_2 = float(input("Please enter second number: "))
    total = num_1 + num_2
    logger.info(f"total is {total}")
except ValueError:
    logger.info(f"Error: Add valid numeric values")

#5: Pass log file path and number of lines to read from end: python tail.py myapp.log 10

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python tail_log.py <file_path> <num_lines>")
    else:
        file_path = sys.argv[1]
        num_lines = int(sys.argv[2])
        print(tail(file_path, num_lines))
