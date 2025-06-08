from loguru import logger

# def final_cart_amount(*args,discount=0.1):
#     result = 0
#     for amount in args:
#         result+=amount
#     print(result)
        
#     amount_after_discount = result - (result*discount)

#     return amount_after_discount
    
# final_amount_to_paid = final_cart_amount(100, 500, 100, 200, 600)

# logger.info(f"{final_amount_to_paid}")

# Write a program where you need to take n number of inputs from user and
# return total sum of it.

# def total_amount (*args):
#     result = 0
#     for amount in args:
#         result+=amount
#     print(result)
#     return result
    
# total_amount_paid = total_amount(100,200,300,400,500)

# logger.info(f"{total_amount_paid}")



# def generic_logging(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# generic_logging(status = "Success", status_code = 200, messgage = "Run successfully")
# generic_logging(status = "Failed", status_code = 500, error = "Table not found")
    

# Write a program in which function take logs input
# from the user and write this into a file. How to write
# into file has not been taught yet so google and try to complete it.

def generic_logging(**kwargs):
    with open("C:/Users/mehul/Downloads/logs.txt","a")as file1:
        for key,value in kwargs.items():
            file1.write(f"{key}:{value}\n")
        
generic_logging(status = "Failed", status_code = 404, message = "Failed to make connection")
generic_logging(status = "Success", status_code = 400, message = "Try again")


# import logging
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged')