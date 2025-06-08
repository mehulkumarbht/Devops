from loguru import logger
import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\mehul\Documents\Programming\config_file.ini")

brick_cost = config["raw_material"]["brick_cost"]

logger.info(f"{brick_cost}, data type of brick_cost{type(brick_cost)}")

def total_no_of_bricks(length,bredth,height):
    no_of_bricks_in_length_side = length * (height * 2)
    total_no_of_bricks_in_length_side = no_of_bricks_in_length_side * 2

    no_of_bricks_in_bredth_side = bredth * (height * 2)
    total_no_of_bricks_in_bredth_side = no_of_bricks_in_bredth_side * 2

    total_no_of_bricks = total_no_of_bricks_in_length_side + total_no_of_bricks_in_bredth_side

    return total_no_of_bricks

def total_cost_of_bricks(config):
    brick_cost = float(config["raw_material"]["brick_cost"])
    final_total_no_of_bricks = total_no_of_bricks(15,15,10)
    final_cost = brick_cost * final_total_no_of_bricks
    return final_cost

result = total_cost_of_bricks(config)

logger.info(f"Total bricks cost to make one room is: {result}")