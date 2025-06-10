from loguru import logger

length = float(input("Please input length: "))
width = float(input("Please input width: "))

rectangular = length * width
logger.info(f"Area of of a rectangular is {rectangular}")