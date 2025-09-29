import periodictable
from loguru import logger

Atomic_table = int(input("Enter periodic table no: "))

element = periodictable.elements[Atomic_table]
logger.info(f"{'Name:', element.name}")
logger.info(f"{'Symbol', element.symbol}")
logger.info(f"{'Mass:', element.mass}")
logger.info(f"{'density:', element.density}")
logger.info(f"{'isotopes:', element.isotopes}")
