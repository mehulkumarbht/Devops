from loguru import logger

number_list: [1,2,3,4,5,6,7,8,9,10]
# new_list = []
# for number in range(1,11):
#     if number%2 ==0:
#         new_list.append(number)
        
# logger.info(f"Give me new list:  {new_list}")

# new_list = [number for number in range(1,11) if number%2 ==0]
# logger.info(f"Give me new list:  {new_list}")

new_list= []
for number in range(1,11):
    if number % 2 == 0:
        new_list.append("Even")
    else:
        new_list.append("Odd")

logger.info(f"Give me new list:  {new_list}")

new_list = ["Even" if number % 2 == 0 else "Odd" for number in range(1,11)]
logger.info(f"Give me new list:  {new_list}")