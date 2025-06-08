from loguru import logger

# length_of_land = 100
# bredth_of_land = 100
# bricks_cost_per_piece = 10.5
# labour_mistri1 = "Jagmohan"
# is_home = True

# length_of_land = int(input("what is the length of your land? : "))
# if length_of_land < 100:
#     logger.info(f"Your land are is not sufficient for 4 BHK House")
#     if length_of_land < 50:
#         logger.info(f"Your land area is too small to build house")
#     else:
#         logger.info(f"You can build 3 BHK house")
# elif length_of_land >= 500:
#     logger.info(f"Your land are is too big to build 4 bhk house")

# else: 
#     logger.info(f"Your land area is perfect to build 4 bhk house")

# Given number is odd or even
result = int(input("What is your number?: "))
if result%2 == 0:
    logger.info(f"It's even number")

else:
    logger.info(f"It's odd number")