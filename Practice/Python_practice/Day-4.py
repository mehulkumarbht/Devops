from loguru import logger
from datetime import date
import time

# Create a list of server names (e.g., "web1", "db1", "cache1"). Loop through the list and print a message like: "Pinging web1... OK"
servers = ["web1", "db1", "cache1"]

for server in servers:
    logger.info(f"Pinging {servers}, OK")

# Given a list of disk usages [40, 70, 90, 55] (in %), write a script that checks each and prints whether it’s under or over the threshold (e.g., 80%).
disk_usages = [40, 70, 90, 55]

for disk_usage in disk_usages:
    if disk_usage < 80:
        logger.info(f"It's under!")
    else:
        logger.info(f"It's over")

# Store a tuple of running service names (e.g., ("nginx", "docker", "ssh")). Print the second service and convert it to a list to add service "kubernetes".
service_names = ("nginex", "docker", "ssh") #tuple of running services name
logger.info(f"Second service name: {service_names[1]}") # Print second service name

service_list = list(service_names) # convert tuple to list

service_list.append("kubernetes") # Add kubernetes to new list

logger.info(f"New service list is: {service_list}")

# Create a dictionary "config" that holds a server's configurations:  hostname = web1, ip = 192.168.1.10, port =  80. Print each key and value in a readable format.

sever_configuration = {"hostname": "web1", "ip": "192.168.1.10", "port":  80}

for key, value in sever_configuration.items():
    logger.info(f"{key}, {value}")

# You have a list of IP addresses with duplicates. Display the unique IP's (Hint: You can use set).

ip_addresses = ["192.168.1.10", "192.168.1.10", "192.187.1.11", "191.167.0.99"]
ip_addresses =set(ip_addresses) # set datastructure automatically removes duplicates from a list 
logger.info(f"{ip_addresses}")

# Define two sets: web_servers and db_servers. Perform and print: Servers common to both, Servers only in web, All unique servers.
web_server = {"web1", "web2", "web3"}
db_server = {"web4","web3", "web5"}
common_server = web_server.intersection(db_server) # servers common in both sets
only_web_server = web_server.difference(db_server) # servers only in web set
unique_server = web_server.union(db_server) # server in both sets
logger.info(f"{common_server}")
logger.info(f"{only_web_server}")
logger.info(f"{unique_server}")