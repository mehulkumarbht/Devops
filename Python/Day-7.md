# Create a Python script that analyzes Linux_2k.log and produces a report showing:

##Total number of log entries
##Number of failed login attempts
##IPs with most failed attempts
##Export the above information to linux_log_report.txt

import os
   
import re

from collections import Counter

from loguru import logger

log_file = "Linux_2k.log"

report_file = "linux_log_report.txt"

total_entries = 0

failed_attempts = 0

failed_ips = []

*Regular expressions to match failed login attampts and extract Ips

failed_login_attempt = re.compile(r"authentication failure.*rhost=\s*([\w\.\-]+)")

try:

    with open(log_file,"r") as file:

        for line in file:

            total_entries += 1

            match = failed_login_attempt.search(line)

            if match:

                failed_attempts += 1

                failed_ips.append(match.group(1))

    *Count Ip occurances

    ip_counter = Counter(failed_ips)

    top_failed_ips = ip_counter.most_common()

    *Generate the report

    with open(report_file, "w") as report:

        report.write("=== Linux Log Report ===\n")

        report.write(f"Total log entries: {total_entries}\n")

        report.write(f"failed login attempts: {failed_attempts}\n")

        report.write(f"IPs with most failed attempts: \n")

        for ip, count in top_failed_ips:

            report.write(f"{ip}: {count} times\n")

    logger.info(f"Report generated: {report_file}")

except FileNotFoundError:

    logger.info(f"Error: Log file {log_file} not found")