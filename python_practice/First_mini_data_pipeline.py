# Day-28 # Mini Pipeline
# Read the CSV file using csv.reader.
# Regex extraction: from the message column, extract any words with only letters (ignore punctuation/numbers).
# Text cleaning: lowercase everything, remove stopwords like {“a”, “the”, “in”, “on”, “at”}.
# Grouping/analysis:
# Count how many times each user performed each action.
# Count how many Error events occurred in total.
# Write back to a new CSV: save results like:
from loguru import logger
import csv
import re
from collections import defaultdict

# config
STOPWORDS = {"a", "the", "in", "on", "at"}
# storage
log_summary = defaultdict(int)
total_errors = 0
with open(
    r"C://Users//Documents//Programming//python_practice//logs.csv",
    "r",
    encoding="utf-8-sig",
) as file:
    reader = csv.reader(file)
    headers = next(reader)
    logger.info(f"Detected headers: {headers}")

    # find column indexes (since we're using csv.reader)
    idx_user = headers.index("user")
    idx_action = headers.index("action")
    idx_message = headers.index("message")

    for row in reader:
        user = row[idx_user]
        action = row[idx_action]
        message = row[idx_message]

        # 1: Regex extract only words (letters only)
        words = re.findall(r"[a-zA-Z]+", message)

        # 2: Clean: lowercase + remove stopwords
        cleaned_words = []
        for word in words:
            if word.lower() not in STOPWORDS:
                cleaned_words.append(word.lower())
        # not required to output cleaned words, but this is where you'd use them
        logger.debug(f"cleaned message words for {user}: {cleaned_words}")

        # 3: Group by user + action
        log_summary[(user.lower(), action.lower())] += 1

        # 4: Count error events
        if action.lower() == "error":
            total_errors += 1
# write summary output
with open("log_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user", "action", "count"])
    for (user, action), count in log_summary.items():
        writer.writerow([user, action, count])

logger.info(f"Total errors: {total_errors}")
