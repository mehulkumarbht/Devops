from loguru import logger
# # Calculate cost of fencing from following:
# length = 100
# breadth = 100
# cost_per_feet = 17

# def calculate_fencing_cost(length, breadth, cost_per_feet):
#     circumference = 2 * (length + breadth)
#     cost_per_fencing = circumference * cost_per_feet
#     return cost_per_fencing

# cost_of_fencing = calculate_fencing_cost (20,20,17)
# logger.info(f"Cost of fencing is {cost_of_fencing}")

# Calculate cost of grass

length = 100
breadth = 20
cost_of_grass = 10

def calculate_grass_cost(length, bredth, cost_of_grass):
    circumference = 2 * (length + breadth)
    cost_of_grass_work = circumference * cost_of_grass
    return cost_of_grass_work

cost_per_grass = calculate_grass_cost(100,20,10)

logger.info(f"Cost of grass is {cost_per_grass}")