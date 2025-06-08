from loguru import logger
import mysql.connector

connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "Rar19bg29#",
                                     database = "home_builder")
logger.info(f"{connection}")

cursor = connection.cursor()

#cursor.execute("select name,wages from labours_table")

#result = cursor.fetchall()

#logger.info(f"{result}")

# insert_query = "INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)"
# cursor.execute(insert_query, ('Rahul', 'labour', 700))
# connection.commit()

logger.info('Entry done in the databases')

insert_query = "DELETE from labours_table WHERE id = 12"
cursor.execute(insert_query)

connection.commit()

logger.info("Entry deleted in the database")
connection.close()
cursor.close()