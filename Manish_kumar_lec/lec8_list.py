from loguru import logger

labour_name = ["Mahesh", "Suresh", "Mithilesh", "Sumesh"]

# logger.info(f"What is the name of the first labour? He's {labour_name[0]}")

# labour_name.append("Ram")

# logger.info(f"Give me names of labour {labour_name}")

# labour_name.append("Mohan")

# logger.info(f"Give me names of labour {labour_name}")

# Insert
# labour_name.insert(2,"Ram")

# logger.info(f"Give me names of labour {labour_name}")

# new_labour = ["Ram", "Mohan"]

# labour_name.extend(new_labour)

# logger.info(f"Give me names of labour {labour_name}")

# -ve indexing 

# labour_name = ["Mahesh", "Suresh", "Mithilesh", "Sumesh"]

# In negative indexing, numbering starts from end and goes in reverse order like in above list Sumesh's
# element value is -1, Mithilesh's element value is -2, suresh's -3 and Mahesh's -4

# It is highly important in real world when we need to call values from the big list from the end

# logger.info(f"What is the name of the first labour? He's {labour_name[-1]}")


# logger.info(f"What is the name of the third labour? He's {labour_name[-3]}")

# Multidimensional list
labour_with_cost = [["Mahesh", 500], ["Suresh", 400], ["Mithilesh", 400], ["Sumesh", 300]]

logger.info(f"What is the name of second labour,i.e. {labour_with_cost [1][0]} and how much he charge per day? i.e. {labour_with_cost[1][1]}")

logger.info(f"What is the name of fourth labour: {labour_with_cost [3][0]}, and how much he charge per day?: {labour_with_cost[3][1]}")