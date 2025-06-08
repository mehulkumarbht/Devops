import psutil

import time

import requests

from loguru import logger

#1: Print current CPU usage percentage.

def cpu_usage(interval=1):

    try:

        while True:

            usage = psutil.cpu_percent(interval=interval)

            logger.info(f"CPU Usage : {usage}%")

    except KeyboardInterrupt:

        logger.info(f"Intruppted by user") #(by Ctrl + c)
		
if __name__ == "__main__":

    logger.info(f"{cpu_usage(1)}") # (CPU usage by interval of 1 second)

#2: List all running processes

def running_process():

    process_list = []

    for process in psutil.process_iter(["pid", "name", "username", "cpu_percent", "memory_percent"]):

        try:

            process_info = process.info

            process_list.append(process_info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

            pass

    logger.info(f"{'pid':<8} {'name':<25},{'username':<24} {'cpu_percent':<8}{'memory_percent':<10}")

    logger.info(f'-'*75)

    for p in process_list:

        logger.info(f"{p.get('pid', ''):<8} {(p.get('name')or '')[:24]:<25} {(p.get('username')or '')[:24]:<25} {p.get('cpu_percent',0):<8} 
		
		{p.get('memory_percent', 0):<8}")

if __name__=="__main__":

    running_process()

#3: Show total, used, free, and percentage disk usage .

def show_disk_usage(path="/"):

    usage = psutil.disk_usage(path)

    logger.info(f"Disk usage for path: {path}")

    logger.info(f"{'Total:':<10} {(usage.total/1024**3):.2f}GB")

    logger.info(f"{'Used:':<10} {(usage.used/1024**3):.2f}GB")

    logger.info(f"{'Free:':<10} {(usage.free/1024**3):.2f}GB")

    logger.info(f"{'percentage:':<10} {usage.percent}%")

if __name__ == '__main__':

    show_disk_usage()

#4: Display network I/O stats.

def show_network_stats():

    network_io = psutil.net_io_counters()

    logger.info(f"Network I/O Statistics (system-wide):")

    logger.info(f"{'Bytes sent:':<20} {(network_io.bytes_sent/1024**2):.2f} MB")

    logger.info(f"{'Byetes received:':<20} {(network_io.bytes_recv/1024**2):.2f} MB")

    logger.info(f"{'Packets sent:':<20} {network_io.packets_sent}")

    logger.info(f"{'Packets received:':<20} {network_io.packets_recv}")

    logger.info(f"{'Errors in:':<20} {network_io.errin}")

    logger.info(f"{'Errors out:':<20} {network_io.errout}")

    logger.info(f"{'Dropped in:':<20} {network_io.dropin}")

    logger.info(f"{'dropped out:':<20} {network_io.dropout}")

if __name__ == '__main__':

    show_network_stats()

#5: Fetch https://example.com/ and display headers including content-type, server, etc.

def fetch_headers(url):

    try:

        response = requests.get(url)

        logger.info(f"Response headers for url {url}")

        for key, value in response.headers.items():

            logger.info(f"{key}:{value}")

    except requests.exceptions.RequestException as e:

        logger.info(f"Error fetching {url}: {e}")

if __name__ == '__main__':

    fetch_headers("https://example.com/")

#6: Use your github user api like https://api.github.com/users/haribabu9298, Extract and print name, public repos, followers.

def fetch_github_user(username):

    url = f"https://api.github.com/users/{username}"

    try:

        response = requests.get(url)

        data = response.json()

        logger.info(f"Github user: {username}")

        logger.info(f"Name: {data.get('name')}")

        logger.info(f"Public Repositories: {data.get('Public repos')}")

        logger.info(f"Followers: {data.get('Followers')}")

    except requests.exceptions.RequestException as e:

        logger.info(f"Error fetching Github data:{e}")

if __name__ == '__main__':

    fetch_github_user('mehulkumarbht')