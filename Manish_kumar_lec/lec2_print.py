# print ("Hello World!")
# variable
# length_of_land = 100
# bricks_cost_per_piece = 10.5
# labour_mistri1 = "Jagmohan"
# is_home = True

# print(length_of_land, bricks_cost_per_piece, labour_mistri1, is_home)

# print(type(length_of_land), type(bricks_cost_per_piece), type(labour_mistri1), type (is_home))

# print("Length of land is", length_of_land)
# print("Mistri's name is", labour_mistri1)
# Escape sequence
# print ("Length of land is \"100\" feet")
# print('''Length of land is "100" feet''')
# print ('Length of land is "100" feet')

# string formatting

# f string
# print(f"cost of bricks per unit is {bricks_cost_per_piece}")

# .format method
# print("cost of bricks per unit is {}".format (bricks_cost_per_piece))

# logging with basicConfig in python

# import logging
# # Configure logging 
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - Line %(lineno)d - %(message)s')

# # Example
# logger = logging.getLogger(__name__)

# from loguru import logger
# logger.info(f"cost of bricks per unit is {bricks_cost_per_piece}")

# Q1. Define a variable of all the labours and print the name of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
#     labour variable should be something like this 1st_labour, 2nd_labour and so on.
# first_labour = "Mahesh"
# second_labour = "Mithilesh"
# third_labour = "Ramesh"
# fourth_labour = "Sumesh"
# print(f"1st_labour is {first_labour}, 2nd_labour is {second_labour}, 3rd_labour is {third_labour}, 4th_labour is {fourth_labour}")
# Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
#     labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
#     2nd_labour_wage and so on.
#     You are bound to use string formatting
first_labour_name = "Mahesh"
second_labour_name = "Mithilesh"
third_labour_name = "Ramesh"
fourth_labour_name = "Sumesh"
first_labour_wage = 500
second_labour_wage = 400
third_labour_wage = 400
fourth_labour_wage = 300

# print(f"{first_labour_name}'s wage is {first_labour_wage}")
# print(f"{second_labour_name}'s wage is {second_labour_wage}")
# print(f"{third_labour_name}'s wage is {third_labour_wage}")
# print(f"{fourth_labour_name}'s wage is {fourth_labour_wage}")
# Q3. I want to print this paragraph and its line number from which this paragraph is printing
#     """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
#     we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
#     help of 'Python programming'. We have total land is of \"100 ft * 100ft\", to complete the house 
#     we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
#             I have to print this paragraph as it is given here."""

from loguru import logger
logger.info(f""" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the help of 'Python programming'. We have total land is of "100 ft * 100ft", to colmplete the house we have total 6 labours with 'different skill set like " building wall or building roof ". I have to print this paragraph as it is given here.""")
#     Condition:- 
#     You can't use triple quote.
#     Triple quote at starting is also a part of paragraph.

# Q4. When do we get NameError?
# When Variable name is not corrrectly defined
# Q5. Python is a high level language. What does that mean by high level?
# It is called high level because it is written in human readable way, do not need to go low level to use it
# Q6. What is compiled and Inetrpreted language, list a few?
# When language need compilation to understand and give results it is called complied while it is not required an interpreter to understand the language than it is called interpreted language.
# C,C++, C# are compiled languages while Python is interpreted language.
# Q7. Get all varibales address from RAM and you find if something is similar?
# print (id(first_labour_name))
# print (id (first_labour_wage))
# print (id (second_labour_name))
# print (id (second_labour_wage))
# print (id (third_labour_name))
# print (id (third_labour_wage))
# print (id (fourth_labour_name))
# print (id (fourth_labour_wage))
# second_labour_wage and third_labour_wage have same variable adderess from RAM