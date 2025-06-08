from loguru import logger

# labour_name = ["Mahesh", "Suresh", "Mithilesh", "Sumesh"]

# itr_number = 0
# while(itr_number < len(labour_name)):
#     logger.info(f"{labour_name[itr_number]}")
#     itr_number = itr_number + 1

# itr_number = len(labour_name)-1 
# while(itr_number >= 0):
#     logger.info(f"{labour_name[itr_number]}")
#     itr_number = itr_number - 1

operator = ['+','-','*','/']
user_input = float(input("please enter the number: "))
while True:
    operator_input = input("Please enter +,-,*,/: ")
    while True:
        user_next_input = float(input("Please enter next number: "))
        if operator_input == '+':
            user_input += user_next_input
        elif operator_input == '-':
            user_input -= user_next_input
        elif operator_input == '*':
            user_input *= user_next_input
        elif operator_input == '/':
            user_input /= user_next_input
        else:
            operator_input == "=":
            logger.info(f" Final result: ")







# operator_input = input.operator("please enter the operator: ")
# user_next_input = input("please enter next number: ")


