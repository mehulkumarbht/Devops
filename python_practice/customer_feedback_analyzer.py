from loguru import logger
import re
import string

raw_feedback = [
    "id: 501, rating: 5, comment: Excellent service! , agent: Alice ",
    "id:502,rating:4,comment:Good support,agent:Bob",
    "invalid feedback line",
    "id: 503, rating: 2 , comment: Very slow response , agent: Charlie",
    "id:504 , rating: 1, comment: Terrible experience , agent: Alice",
    "id: 505, rating:5, comment: Amazing help!, agent:  Bob ",
    "id:506 rating 3 comment ok agent Dave",  # Missing colons → invalid
]
# 1: Clean & Parse Valid Feedback Only
# Must contain id, rating, comment, agent
# Must contain : separators
# Ignore invalid lines

cleaned_feedback = []
required_keys = {"id", "rating", "comment", "agent"}
for row in raw_feedback:
    record = {}
    parts = row.split(",")
    for part in parts:
        if (
            ":" not in part
        ):  # To avoid crashing it on "INVALID LINE HERE", guard it with
            continue
        try:
            key, value = part.split(":", 1)
            key = key.strip()
            value = value.strip()
            record[key] = value
        except ValueError:
            # skip if split failed unexpectedly
            continue
    # skip if record is incomplete
    if len(record) != 4:
        logger.info(
            f"Skipping incomplete or improperly formatted record: {row.strip()}"
        )
        continue
    # 2 Convert fields: #agent: is alreay striped with above loop .strip()
    try:
        record["id"] = int(record["id"])
        record["rating"] = int(record["rating"])
        cleaned_feedback.append(record)
    except ValueError as e:
        logger.error(f"Error converting types for now: {row.strip()} Error: {e}")
        continue
logger.info(f"Final cleaned feedback records: {cleaned_feedback}")

# 3: Calculate summary stats
# a: Average rating across all feedback:
total_rating_sum = 0
total_rating_count = 0
for record in cleaned_feedback:
    rating = record["rating"]
    total_rating_sum += rating
    total_rating_count += 1

if total_rating_count > 0:
    overall_average = total_rating_sum / total_rating_count
    logger.info(f"Overall average rating:{overall_average:.2f}")
else:
    logger.info("Cannot calculate average: No feedback records found")
    overall_average = 0

    # b: Feedback count per agent
feedback_count_per_agent = {}
for record in cleaned_feedback:
    agent = record["agent"]
    if agent in feedback_count_per_agent:
        feedback_count_per_agent[agent] += 1
    else:
        feedback_count_per_agent[agent] = 1
logger.info(f"{feedback_count_per_agent}")

# c: Top 2 agents with highest average rating
total_rating_per_agent = {}
rating_count_per_agent = {}
for record in cleaned_feedback:
    agent = record["agent"]
    rating = record["rating"]
    if agent in total_rating_per_agent:
        total_rating_per_agent[agent] += rating
    else:
        total_rating_per_agent[agent] = rating

    if agent in rating_count_per_agent:
        rating_count_per_agent[agent] += 1
    else:
        rating_count_per_agent[agent] = 1
avg_rating_per_agent = {}
for agent_name in total_rating_per_agent:
    total_sum = total_rating_per_agent[agent_name]
    total_count = rating_count_per_agent[agent_name]
    if total_count > 1:
        average = total_sum / total_count
        avg_rating_per_agent[agent_name] = round(average, 2)
logger.info(f"Avg rating per agent: {avg_rating_per_agent}")
top_2_agents = sorted(
    avg_rating_per_agent.items(), key=lambda item: item[1], reverse=True
)
logger.info(f"Agent sorted by rating {top_2_agents}")


# d: How many ratings are 4 or 5? (positive feedback)

positive_feedback = 0
for record in cleaned_feedback:
    rating = record["rating"]
    if rating in (4, 5):
        positive_feedback += 1
logger.info(f"Number of Positive feedback:{positive_feedback}")

# 4: Identify Negative Comments, Return all comments where rating ≤ 2.

# negative_comments = []
# for record in cleaned_feedback:
#     rating = record["rating"]
#     comment = record["comment"]
#     if rating <= 2:
#         negative_comments.append(comment)
# logger.info(f"{negative_comments}")
