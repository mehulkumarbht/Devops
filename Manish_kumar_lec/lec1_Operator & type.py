from loguru import logger

length_of_land = 100
bredth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
is_home = True

# Calculate the total area of the land

# total_area_of_land = length_of_land * bredth_of_land
# logger.info(f"Total are of my land is {total_area_of_land} sq ft")

# BODMAS (Bracket, Division, Multiplication, Addition,Substraction)
# perimeter_of_land = 2 * (length_of_land + bredth_of_land)

# logger.info(f"perimeter of land is {perimeter_of_land} sq ft")

# Modulo opertor
# print(15/8) #Armstong number code

# Floor & Ceiling division
# import math
# print(15/8)
# print(math.ceil(15/8))
# print(math.floor(15/8))

# Concatenation
# a = "mehul"
# b = 25
# print(a+str(b))

# a = '25'
# b = 20
# print(int(a)+b)

# User input
length_of_land = int(input("Please enter your length of land: "))
breadth_of_land = input("Please enter your breadth of land: ")

# logger.info(f'{type(lenght_of_land)}')
total_are_of_your_land = (length_of_land) * float(breadth_of_land)
logger.info(f"Total area of your land is {total_are_of_your_land} sq ft")