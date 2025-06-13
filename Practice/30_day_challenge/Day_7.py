# Count word frequencies in a text file - Day_7
from loguru import logger

file = open(
    "C:\\Users\\Documents\\Programming\\Practice\\30_day_challenge\\linux_log_report.txt",
    "r",
)

for line in file:
    word = line.split(" ")
    logger.info(f"{len(word)}")
