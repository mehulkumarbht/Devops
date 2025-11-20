from loguru import logger
import re
import string
# Day:1: Convert normal loops into list comprehensions.

# 1: Create a list of numbers from 1 to 10 using list comprehension.
# number_list = [n for n in range(1, 11)]
# logger.info(f"{number_list}")

# 2: Generate a list of their squares.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# squares = [n**2 for n in numbers]
# logger.info(f"{squares}")

# 3: Make a list of only even numbers from 1 to 20.
# evens = [n for n in range(1, 21) if n % 2 == 0]
# logger.info(f"{evens}")

# 4: Create a list of strings: ["Hello 1", "Hello 2", ..., "Hello 5"].
# list_of_string = [f"Hello {n}" for n in range(1, 6)]
# logger.info(f"{list_of_string}")
# list_of_string = []
# for n in range(1, 6):
#     list_of_string.append(f"Hello {n}")
# logger.info(f"{list_of_string}")

# 5: Convert each word in ["apple", "banana", "cherry"] to uppercase using list comprehension.
# fruits = ["apple", "banana", "cherry"]
# upper_list = [word.upper() for word in fruits]
# logger.info(f"{upper_list}")

# Day-2:Add filters (if) and transformations.
# 1: From numbers 1–15, create a list of squares only for odd numbers.
# squares = [n**2 for n in range(1, 16) if n % 2 != 0]
# logger.info(f"{squares}")

# 2: Replace numbers 1–10 with "even" or "odd" strings depending on the number.
# even_odd = ["even" if n % 2 == 0 else "odd" for n in range(1, 11)]
# logger.info(f"{even_odd}")

# 3: Given words = ["cat", "house", "dog", "elephant"], create a list of words with length > 3.
# words = ["cat", "house", "dog", "elephant"]
# wordslist = [word for word in words if len(word) > 3]
# logger.info(f"{wordslist}")

# 4: From words, create a list of their first letters.
# words = ["cat", "house", "dog", "elephant"]
# first_letters = [word[0] for word in words]
# logger.info(f"{first_letters}")

# 5: Flatten a 2D list: [[1,2], [3,4], [5,6]] → [1,2,3,4,5,6].
# num_list = [[1, 2], [3, 4], [5, 6]]
# flatten = [num for row in num_list for num in row]
# logger.info(f"{flatten}")

# Day-3: Practice nesting and combining.
# 1: Create a multiplication table for numbers 1–5 (like [1,2,3,4,5,2,4,6,...]).
# table = [m * n for m in range(1, 6) for n in range(1, 6)]
# logger.info(f"{table}")

# 2: Create all pairs (x, y) where x is from [1,2,3] and y is from [‘a’, ‘b’].
# num = [1, 2, 3]
# char = ["a", "b"]
# pairs = [(x, y) for x in num for y in char]
# logger.info(f"{pairs}")

# 3: Given a sentence "the quick brown fox", split into words and make a list of their lengths.
# sentence = "the quick brown fox"
# words = sentence.split()
# length_of_words = [len(word) for word in words]
# logger.info(f"{length_of_words}")

# 4: Extract vowels from "programming is fun" into a list.
# vowels = "aeiou"
# sentence = "programming is fun"
# vowles_list = [word for word in sentence if word in vowels]
# logger.info(f"{vowles_list}")

# 5: From nums = [0,1,2,3,4,5,6,7,8,9], build a list that keeps numbers < 5 as is, but replaces numbers ≥ 5 with "big".
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums_list = ["big" if n >= 5 else n for n in nums]
# logger.info(f"{nums_list}")

# Day-4:
# 1: Extract numbers from a string
# text = "Order IDs are: 23, 45, 67, and 89"
# # Expected: [23, 45, 67, 89]
# number_as_string = re.findall(
#     r"\d+", text
# )  # Extract all sequences of one or more digits
# number_as_integer = [
#     int(num) for num in number_as_string
# ]  # Convert the extracted strings to integers
# logger.info(f"{number_as_integer}")

# 2: Flatten + filter logs
# logs = [
#     ["INFO: Start", "ERROR: Disk full"],
#     ["INFO: Running", "ERROR: Timeout"],
#     ["INFO: Finished"],
# ]
# # Expected: ['Disk full', 'Timeout']   (only error messages, without 'ERROR:')
# errors = [
#     msg.replace("ERROR: ", "")
#     for sublist in logs
#     for msg in sublist
#     if msg.startswith("ERROR:")
# ]
# logger.info(f"{errors}")

# 3: Unique words, lowercase, no stopwords
# sentence = "The quick brown fox jumps over the lazy dog"
# stopwords = {"the", "over"}
# # Expected: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']
# words = sentence.lower().split()
# cleaned_words = [word for word in words if word not in stopwords]
# logger.info(f"{cleaned_words}")

# 4: Transpose a matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
# # Expected: [[1, 4], [2, 5], [3, 6]]
# transpose_matrix = [list(row) for row in zip(*matrix)]
# logger.info(f"{transpose_matrix}")

# 5: Dictionary from two lists
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "Toronto"]
# # Expected: {'name': 'Alice', 'age': 25, 'city': 'Toronto'}
# my_dict = dict(zip(keys, values))
# logger.info(f"{my_dict}")

# Day-5:
# 1: Word frequency counter
# sentence = "apple banana apple orange banana apple"
# from collections import Counter
# words = sentence.split()
# counter = Counter(words)
# logger.info(f"{counter}")

# 2: Reverse dictionary
# students = {"Alice": 25, "Bob": 30, "Charlie": 35}
# reverse_students = {value: key for key, value in students.items()}
# logger.info(f"{reverse_students}")

# 3: Filter dictionary
# scores = {"Alice": 85, "Bob": 60, "Charlie": 95, "Dave": 40}
# high_scores = {key: value for key, value in scores.items() if value >= 70}
# logger.info(f"{high_scores}")

# 4: From the word "programming", build a set of all unique consonants (exclude vowels).
# word = "programming"
# vowels = "aeiou"
# unique_consonants = {char for char in word if char not in vowels}
# logger.info(f"{unique_consonants}")

# 5: Convert into a dictionary where keys are column indexes and values are lists of column elements.
# matrix = [[1, 2], [3, 4], [5, 6]]
# transposed_matrix = {i: [row[i] for row in matrix] for i in range(len(matrix[0]))}
# logger.info(f"{transposed_matrix}")

# Day-6:
# 1: Write a list comprehension that generates squares of numbers 1–10.
# squares = [num**2 for num in range(1, 11)]
# logger.info(f"{squares}")
# bonus: extract only the even squares.
# even_squares = [num**2 for num in range(1, 11) if num % 2 != 0]
# logger.info(f"{even_squares}")
# 2: From ["cat", "house", "dog", "elephant"], keep only words with length > 3.
# words = ["cat", "house", "dog", "elephant"]
# long_words = [word for word in words if len(word) > 3]
# logger.info(f"{long_words}")

# bonus: collect only their first letters.
# first_letters = [word[:1] for word in words]
# logger.info(f"{first_letters}")

# Day-7
# 1: Build a list of each word’s length.
# sentence = "The quick brown fox jumps over the lazy dog"
# words = sentence.split()
# length_words = [len(word) for word in words]
# logger.info(f"{length_words}")
# bonus:build a dict {word: length}
# length_words = {word: len(word) for word in words}
# logger.info(f"{length_words}")

# 2: From "programming", build a set of all unique consonants.
# word = "programming"
# vowels = "aeiou"
# number_of_consonants = [char for char in word if char not in vowels]
# logger.info(f"{number_of_consonants}")

# bonus: count vowels vs consonants
# number_of_vowels = sum([1 for char in word if char in vowels])
# number_of_consonants = sum([1 for char in word if char not in vowels])
# logger.info(f"Number of vowels: {number_of_vowels}")
# logger.info(f"Number of consonants: {number_of_consonants}")


# Day-8:
# 1: Extract error messages only (remove "ERROR:").
# import re

# logs = ["INFO: Start", "ERROR: Disk full", "INFO: Run", "ERROR: Timeout"]
# error = []
# for line in logs:
#     match = re.search(r"ERROR: (.*)", line)
#     if match:
#         error.append(match.group(1))
# logger.info(f"{error}")
# Bonus: build a dict {level: [messages...]}.
# error = {}
# for line in logs:
#     level, message = line.split(":", 1)
#     error.setdefault(level, []).append(message)
# logger.info(f"{error}")

# Day-09
# Choose one of these:
# Word analyzer: word → length, frequency, unique letters.
# Mini CSV transformer: list of strings → list of dicts.
# Log summary: count INFO, ERROR, WARNING.

# Word Analyzer:
# word = "banana"

# word_length = len(word)
# logger.info(f"{word_length}")
# word_frequency = sum[1 for char in word if char == word_frequency[char]]
# logger.info(f"{word_frequency}")

# word_frequency = {}
# for char in word:
#     if char in word_frequency:
#         word_frequency[char] += 1
#     else:
#         word_frequency[char] = 1
# logger.info(f"{word_frequency}")

# word_unique = set(word)
# logger.info(f"{word_unique}")

# logs = ["INFO: Start", "ERROR: Disk full", "INFO: Run", "WARNING: Low memory"]

# log_dict = {}
# for line in logs:
#     level, message = line.split(":", 1)
#     log_dict.setdefault(level, []).append(message)
# logger.info(f"{log_dict}")

# Day-10
# Mini Word Analyzer
# Take an input word and produce:Length of the word, Unique letters, Frequency of each letter
# word = "Programming"
# words = word.lower()
# words_length = len(words)  # length of the word
# logger.info(f"{words_length}")
# unique_letters = set(words)
# logger.info(f"{unique_letters}")
# frequency_letters = {}
# for word in words:
#     if word in frequency_letters:
#         frequency_letters[word] += 1
#     else:
#         frequency_letters[word] = 1
# logger.info(f"{frequency_letters}")

# Mini CSV Transformer
# data = ["name,age,city", "Alice,25,Toronto", "Bob,30,New York", "Charlie,35,London"]
# headers = data[0].split(",")
# rows = data[1:]
# result = [dict(zip(headers, row.split(","))) for row in rows]
# logger.info(f"{result}")

# older_than_30 = [
#     dict(zip(headers, row.split(","))) for row in rows if int(row.split(",")[1]) > 30
# ]
# logger.info(f"{older_than_30}")

# Day-11:
# 1: Group People by City
# result = [
#     {"name": "Alice", "age": "25", "city": "Toronto"},
#     {"name": "Bob", "age": "30", "city": "New York"},
#     {"name": "Charlie", "age": "35", "city": "London"},
#     {"name": "Dave", "age": "32", "city": "New York"},
# ]
# grouped_by_city = {}
# for row in result:
#     city = row["city"]
#     name = row["name"]
#     grouped_by_city.setdefault(city, []).append(name)
# print(grouped_by_city)

# 2: Log Summary Generator
# logs = [
#     "INFO: System started",
#     "ERROR: Disk full",
#     "WARNING: Low memory",
#     "INFO: Running task",
#     "ERROR: Timeout",
#     "INFO: Completed",
# ]
# log_summary = {}
# for line in logs:
#     level, message = line.split(": ", 1)
#     log_summary[level] = log_summary.get(level, 0) + 1
# logger.info(f"{log_summary}")

# 3: Error log extractor
# logs = [
#     "INFO: System started",
#     "ERROR: Disk full",
#     "WARNING: Low memory",
#     "INFO: Running task",
#     "ERROR: Timeout",
#     "INFO: Completed",
# ]
# log_summary = []
# for line in logs:
#     if line.startswith("ERROR:"):
#         message = line.split(":", 1)[1]
#         log_summary.append(message)
# logger.info(f"{log_summary}")


# 7 Day:List Comprehension & Logic series
# 1
# logs = [
#     "INFO: System started",
#     "ERROR: Disk full",
#     "WARNING: Low memory",
#     "INFO: Running task",
#     "ERROR: Timeout",
#     "INFO: Completed",
# ]
# log_summary = {}
# for line in logs:
#     level, message = line.split(":", 1)
#     log_summary[level] = log_summary.get(level, 0) + 1
# logger.info(f"{log_summary}")

# log_summary = []
# for line in logs:
#     if line.startswith("INFO:"):
#         message = line.split(":", 1)[1]
#         log_summary.append(message)
# logger.info(f"{log_summary}")

# 2: Given a sentence or paragraph:
# Count total words
# Build a frequency dictionary (word → count)
# Extract top 3 most common words
# sentence = "Our colleagues strive to have a positive impact and make a meaningful difference to our business performance, our customers’ lives and the communities where we live, work and play."
# count = 0
# cleaned_sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
# words = cleaned_sentence.split()

# # Count total words
# total_words = len(words)
# logger.info(f"{total_words}")  # Count total words

# # Build a frequency dictionary (word → count)
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# logger.info(f"{word_count}")  # Build a frequency dictionary (word → count)

# # Extract top 3 most common words
# top_3_common_words = []
# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
# for word, count in sorted_words[:3]:
#     top_3_common_words.append(word)
# logger.info(f"Top 3 common words are: {top_3_common_words}")

# 3: From your previous CSV transformer:
# Keep only rows where age > 30.
# Add a new field "status" = "senior" if age ≥ 35 else "mid".

# data = ["name,age,city", "Alice,25,Toronto", "Bob,30,New York", "Charlie,35,London"]
# headers = data[0].split(",")
# rows = data[1:]
# results = []
# for row in rows:
#     row_values = row.split(",")  # split row string into a list of values
#     row_dict = dict(zip(headers, row_values))  # create dictionary for the current row
#     age = int(row_dict["age"])  # Convert the 'age' string to an integer for comparision
#     # if age > 30:
#     if age >= 35:
#         print("Status = senior")
#     else:
#         print("Status = mid")

# 4: Using the CSV data, group people by city and show how many live in each city.
# data = ["name,age,city", "Alice,25,Toronto", "Bob,30,New York", "Charlie,35,London"]
# city = {}
# rows = data[1:]
# for row in rows:
#     level, message, place = row.split(",", 2)
#     city[place] = city.get(place, 0) + 1
# logger.info(f"{city}")

# 5: Given a 2D list (matrix):Transpose it, Flatten it, Keep only even numbers.
# [[1,2,3],[4,5,6]] → [2,4,6]
# matrix = [[1, 2, 3], [4, 5, 6]]
# transpose_matrix = [list(row) for row in zip(*matrix)]
# logger.info(f"{transpose_matrix}")  # transpose

# flatten_matrix = [num for row in matrix for num in row]
# logger.info(f"{flatten_matrix}") # flatten

# even_matrix = [num for row in matrix for num in row if num % 2 == 0]
# logger.info(f"{even_matrix}") # even numbers from matrix

# 6: Remove entries with None scores and normalize all names to lowercase
# data = [
#     {"user": "Alice", "score": 50},
#     {"user": "Bob", "score": None},
#     {"user": "Charlie", "score": 70},
# ]
# scores = {}
# for row in data:
#     if row["score"] is not None:
#         user_name_lower = row["user"].lower()
#         scores[user_name_lower] = row["score"]
# logger.info(f"{scores}")

# 7: Convert the data into a list of dictionaries (like a CSV parser).

# Calculate:
# Average salary per department.

# Youngest and oldest employee.

# Count of employees per city.

# Filter employees earning more than 65 000.

# Group by department and list employee names.

# Find top 3 highest-paid employees overall.
# data = [
#     "id,name,age,city,salary,department",
#     "1,Alice,25,Toronto,55000,Engineering",
#     "2,Bob,30,New York,62000,Marketing",
#     "3,Charlie,35,London,72000,Engineering",
#     "4,David,28,Toronto,58000,Sales",
#     "5,Eva,32,London,69000,Engineering",
#     "6,Frank,40,New York,80000,Marketing",
#     "7,Grace,29,London,60000,Sales",
# ]
# avg salary
# total_salary = 0
# count = 0
# rows = data[1:]
# for row in rows:
#     fields = row.split(",")
#     salary = int(fields[4])
#     total_salary += salary
#     count += 1
#     avg_salary = total_salary / count
# logger.info(f"{avg_salary:.2f}")

# youngest and oldest employees:
# first_row_field = rows[0].split(",")
# initial_age = int(first_row_field[2])
# youngest_employee_age = initial_age
# oldest_employee_age = initial_age
# for row in rows:
#     fields = row.split(",")
#     age = int(fields[2])
#     if age < youngest_employee_age:
#         youngest_employee_age = age
#     if age > oldest_employee_age:
#         oldest_employee_age = age
# logger.info(f"Age of youngest employee: {youngest_employee_age}")
# logger.info(f"Age of oldest employee: {oldest_employee_age}")

# count of employees per city
# employees_per_city = {}
# for row in rows:
#     fields = row.split(",")
#     city = fields[3]
#     if city in employees_per_city:
#         employees_per_city[city] += 1
#     else:
#         employees_per_city[city] = 1
# logger.info(f"{employees_per_city}")

# 3 Filter employees earning more than 65000
# employees_earning_more_than_65000 = []
# for row in rows:
#     fields = row.split(",")
#     salary = int(fields[4])
#     name = fields[1]
#     if salary > 65000:
#         employees_earning_more_than_65000.append(name)
# logger.info(f"{employees_earning_more_than_65000}")

# 4 Group By department and list employees names
# employee_counts_by_department = {}
# for row in rows:
#     fields = row.split(",")
#     department = fields[5]
#     if department in employee_counts_by_department:
#         employee_counts_by_department[department] += 1
#     else:
#         employee_counts_by_department[department] = 1
# logger.info(f"{employee_counts_by_department}")

# 5: find top 3 highest paid employees overall
# highest_paid_employees = []
# for row in rows:
#     fields = row.split(",")
#     employee_dict = {"name": fields[1], "salary": int(fields[4])}
#     highest_paid_employees.append(employee_dict)
#     highest_paid_employees.sort(
#         key=lambda highest_paid_employees: highest_paid_employees["salary"],
#         reverse=True,
#     )
#     top_3_highest_paid = highest_paid_employees[:3]
# logger.info(f"{top_3_highest_paid}")

# data = [
#     "id,name,age,city,salary,department",
#     "1,Alice,25,Toronto,55000,Engineering",
#     "2,Bob,30,New York,62000,Marketing",
#     "3,Charlie,35,London,72000,Engineering",
#     "4,David,28,Toronto,58000,Sales",
#     "5,Eva,32,London,69000,Engineering",
#     "6,Frank,40,New York,80000,Marketing",
#     "7,Grace,29,London,60000,Sales",
# ]

# # 1: Parse the data into list of dicts
# headers = data[0].split(",")
# rows = data[1:]
# records = []
# for row in rows:
#     employee_dict = dict(zip(headers, row.split(",")))
#     records.append(employee_dict)
# logger.info(f"{records}")
# records = [dict(zip(headers, row.split(","))) for row in rows]
# logger.info(f"{records}")

# # 2: Convert numeric fields
# for row in records:
#     row["age"] = int(row["age"])
#     row["salary"] = int(row["salary"])

# # 3: Average salary per department
# avg_salary = {}
# total_salaries_by_department = {}
# employee_count_by_department = {}
# for row in rows:
#     fields = row.split(",")
#     salary = int(fields[4])
#     department = fields[5]
#     if department not in total_salaries_by_department:
#         total_salaries_by_department[department] = 0
#         employee_count_by_department[department] = 0
#     total_salaries_by_department[department] += salary
#     employee_count_by_department[department] += 1

# average_salary_by_department = {}
# for department in total_salaries_by_department:
#     total_salary = total_salaries_by_department[department]
#     count = employee_count_by_department[department]
#     avg_salary = total_salary / count
#     average_salary_by_department[department] = (
#         f"{avg_salary:.2f}"  # or = round(avg_salary, 2)
#     )
# logger.info(f"{average_salary_by_department}")


# # 4: Employees with salary > 65000
# high_earners = []
# for row in records:
#     if row["salary"] > 65000:
#         high_earners.append(row["name"])
# logger.info(f"{high_earners}")

# # 5: Count employees per city
# employees_per_city = {}
# for row in records:
#     if row["city"] in employees_per_city:
#         employees_per_city[row["city"]] += 1
#     else:
#         employees_per_city[row["city"]] = 1
# logger.info(f"{employees_per_city}")


# logs = [
#     "INFO: Started job",
#     "INFO: Connected to DB",
#     "ERROR: Disk full",
#     "WARNING: Memory high",
#     "ERROR: Timeout",
#     "INFO: Finished job",
# ]
# # Count how many INFO, ERROR, and WARNING messages there are.
# count = {}
# for row in logs:
#     level, message = row.split(":", 1)
#     count[level] = count.get(level, 0) + 1
# logger.info(f"{count}")

# data = [
#     {"name": "Alice", "age": 25, "city": "Toronto", "salary": 55000},
#     {"name": "Bob", "age": 30, "city": "New York", "salary": 62000},
#     {"name": "Charlie", "age": 35, "city": "London", "salary": 72000},
#     {"name": "David", "age": 28, "city": "Toronto", "salary": 58000},
#     {"name": "Eva", "age": 32, "city": "London", "salary": 69000},
# {"name": "Frank", "age": 40, "city": "New York", "salary": 80000},
# ]

# 1: Filter employees with salary above 60 000.
# salary_above_60000 = []
# for row in data:
#     salary = int(row["salary"])
#     if salary > 60000:
#         salary_above_60000.append(row)
# logger.info(f"{salary_above_60000}")


# 2: Find the average salary per city.
# city_salaries = {}
# city_count = {}
# for row in data:
#     salary = int(row["salary"])
#     city = row["city"]
#     if city not in city_salaries:
#         city_salaries[city] = 0
#         city_count[city] = 0
#     city_salaries[city] += salary
#     city_count[city] += 1
# avg_salary = {}
# for city in city_salaries:
#     total_salary = city_salaries[city]
#     count = city_count[city]
#     avg_salary[city] = total_salary / count
# logger.info(f"{avg_salary}")

# 3: Find the name of the highest-paid person overall.
# highest_paid_person = ""
# highest_salary = 0
# for row in data:
#     name = row["name"]
#     salary = int(row["salary"])
#     if salary > highest_salary:
#         highest_salary = salary
#         highest_paid_person = name
# logger.info(f"Highest paid person: {highest_paid_person}, salary: {highest_salary}")

# 4: (Bonus) Create a list of formatted strings like:["Alice from Toronto earns $55000", ...]
# formatted_string_list = []
# for row in data:
#     name = row["name"]
#     city = row["city"]
#     salary = int(row["salary"])
#     formatted_string = f"{name} from {city} earns ${salary}"
#     formatted_string_list.append(formatted_string)
# logger.info(f"{formatted_string_list}")

# transactions = [
#     {"id": 1, "user": "Alice", "amount": 120, "type": "deposit"},
#     {"id": 2, "user": "Bob", "amount": 50, "type": "withdrawal"},
#     {"id": 3, "user": "Alice", "amount": 200, "type": "deposit"},
#     {"id": 4, "user": "Charlie", "amount": 70, "type": "deposit"},
#     {"id": 5, "user": "Bob", "amount": 130, "type": "deposit"},
#     {"id": 6, "user": "Charlie", "amount": 50, "type": "withdrawal"},
# ]

# 1: Total balance per user, Assume: deposit = +amount, withdrawal = -amount
# total_balance = {}
# for amt in transactions:
#     name = amt["user"]
#     amount = amt["amount"]
#     transactions_type = amt["type"]
#     if name not in total_balance:
#         total_balance[name] = 0
#     if transactions_type == "deposit":
#         total_balance[name] += amount
#     else:
#         total_balance[name] -= amount
# logger.info(f"{total_balance}")

# 2: Count transactions per type
# transaction_count = {}
# for t in transactions:
#     transactions_type = t["type"]
#     if transactions_type in transaction_count:
#         transaction_count[transactions_type] += 1
#     else:
#         transaction_count[transactions_type] = 1
# logger.info(f"{transaction_count}")

# 3: Find user with highest total balance
# total_balance = {}
# for t in transactions:
#     name = t["user"]
#     amount = t["amount"]
#     transactions_type = t["type"]
#     if name not in total_balance:
#         total_balance[name] = 0
#     if transactions_type == "deposits":
#         total_balance[name] += amount
#     else:
#         total_balance[name] = amount
# logger.info(f"{total_balance}")

# highest_total_balance = max(total_balance.items(), key=lambda x: x[1])
# logger.info(f"{highest_total_balance}")

# 4: Build a summary sentence:
# formatted_string_list = []
# for t in transactions:
#     name = t["user"]
#     current_user_balance = total_balance[name]
#     transactions_type = t["type"]
#     formatted_string = (
#         f"{name} has the ${current_user_balance} across {transactions_type}"
#     )
#     formatted_string_list.append(formatted_string)
# logger.info(f"{formatted_string_list}")

# Day-28
matrix = [[5, 12, 17], [3, 6, 9], [14, 8, 11]]
# Flatten the matrix into a single list:
flatten_matrix = [num for row in matrix for num in row]
logger.info(f"{flatten_matrix}")

# Filter only even numbers from the flattened list.
even_num = [num for num in flatten_matrix if num % 2 == 0]
logger.info(f"{even_num}")

# Create a list of squares of numbers > 10.
squares = [num**2 for num in flatten_matrix if num > 10]
logger.info(f"{squares}")

# Build a dictionary with key=original number and value=square for numbers > 10.
number_list = {}
# {number_list[num] for num in flatten_matrix}
for num in flatten_matrix:
    if num > 10:
        number_list[num] = num**2
logger.info(f"{number_list}")
