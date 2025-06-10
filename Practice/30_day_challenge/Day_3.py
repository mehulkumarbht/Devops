from loguru import logger

furniture = {"table": 500, "desk": 120, "chairs": 180}
# inventory = furniture["table"]
# print(inventory)
# for key, value in furniture.items():
#     logger.info (f"{key} : {value}")

def display_furniture():
    logger.info("\nCurrent Inventory:")
    for key, value in furniture.items():
        logger.info(f"{key}: {value}")
    
def add_furniture(key, value):
    if key in furniture:
        furniture[key] += value
    else:
        furniture[key] = value
    logger.info(f"Purchased {value} in {key}")

def remove_furniture(key, value):
    if key in furniture:
        furniture[key] -= value
    else:
        furniture[key] = value
    logger.info(f"Sold {value} in {key}")

display_furniture()
add_furniture("table", 3)
remove_furniture("desk", 5)
remove_furniture("chair", 11)

display_furniture()