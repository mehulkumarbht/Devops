from loguru import logger

# labour_name = ["Mahesh", "Suresh", "Mithilesh", "Sumesh"]

# for name in labour_name:
#     logger.info(f" Give me labour name:{name} ")

# for i in range(len(labour_name)):
#     # logger.info(f"Give me labour number:{i}")
#     logger.info(f"Give me labour {i+1}'s name: {labour_name[i]}")

# # Star pyramid
# for i in range(5):
#     logger.info(f"{(i+1) * "*"}")

# Reverse Star Pyramid
# for i in range(5):
#     logger.info(f"{(5-i)* "*"}")

# Getting odd numbers from 0 to 100
# for number in range(101):
#     if number%2 != 0:
#         logger.info(f"Give me odd numbers from 0 to 100: {number}") 

number_list = [1,2,3,4,5,6,7,8,9,10]

new_list = []
for number in number_list:
    if number % 2 == 0:
        new_list.append(number)
        logger.info(f"Give me new list: {new_list}")

