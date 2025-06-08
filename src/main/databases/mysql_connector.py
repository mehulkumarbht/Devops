from loguru import logger
import mysql.connector
from src.main.encrypt_decrypt.lec_25_encryption_decryption import decrypt

import configparser
config = configparser.ConfigParser()
class MySqlConnection:
    def __init__(self,config):
        self.config = config
        self.connection  = None
        
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host = self.config["mysql_database"]["host"],
                                                      user = self.config["mysql_database"]["user"],
                                                      password = self.config["mysql_database"]["password"],
                                                      database = self.config["mysql_database"]['database'])
            logger.info("MySQL Connection Successful")

        except Exception as e:
            logger.error(f"Error occured: {e}")
            raise e
    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info("MySQL Connection closed")
class MySQLCRUDOperation:
    def __init__(self,mysql_connection):
        self.connection = mysql_connection

    def read_from_mysql(self, query):
        logger.info(f"Query sent to read {query}")
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            logger.info(f"Error occured in mysql query run {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
                logger.info('Cursor Closed')

    def insert_into_mysql(self,query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit() # this is very important, without commit database entry will not happen 
            logger.info("Insert committed to Database.")
        except Exception as e:
            logger.info(f"Error occured in mysql query run {e}")
            raise e
        finally:
                cursor.close()
                logger.info("Cursor closed")

        


    

# config.read(r"C:\Users\mehul\Documents\Programming\src\resources\config_file.ini")

# def read_from_mysql(config,query):
#     try:
#         connection = mysql.connector.connect(host = config["mysql_database"]["host"],
#                                             user = config["mysql_database"]["user"],
#                                             password = decrypt(config["mysql_database"]["password"]),
#                                             database = config["mysql_database"]["database"])
        

#         cursor = connection.cursor()
#         cursor.execute(query)
#         result = cursor.fetchall()
#         # logger.info(f"{result}")
#         return result
#     except Exception as e:
#         logger.info(f"Error occured in mysql DB {e}")
#         raise e
#     finally:
#         connection.close()
#         cursor.close()

