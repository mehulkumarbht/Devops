from loguru import logger

# def final_cart_amount(*args, discount=0.10):
#     try:
#         result = 0
#         for amount in args:
#             result += amounts
        
#         amount_after_discount = result - (result*discount)

#         return amount_after_discount
#     except NameError:
#         logger.info("Variable not found")
#         raise Exception("Please check the variable name")
#     except TypeError:
#         logger.info("Please provide the amount in integer")
#         raise Exception("Value provided is not an integer coming from TypeError")
#     except Exception as e:
#         logger.info("Can not process the cart amount")
#         raise e
# try:
#     final_cart_amount_to_be_paid = final_cart_amount(100, 500, 120, 300, '500', discount=0.5)

#     logger.info(final_cart_amount_to_be_paid)
# except Exception as e:
#     logger.info(e)
#     raise e
# logger.info("Entry in Database done. Job ran successfully")

# Write a program to open a log.txt. If file is empty then raise an exception.
# If it's not empty then find out all of the unique names in the file. 

file = open("C:/Users/mehul/Downloads/logs.txt", "r")
content = file.read()
print(content)
try:
    If file is null:
    except Exception as e:
    logger.info("File is empty")
    raise e 


