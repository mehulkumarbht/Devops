from loguru import logger
from src.main.databases.mysql_connector import MySqlConnection, MySQLCRUDOperation
from src.main.encrypt_decrypt.lec_25_encryption_decryption import decrypt
from datetime import datetime
import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\mehul\Documents\Programming\src\resources\config_file.ini")
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

class Labour:
    # count = 0 # class variable
    def __init__(self, first_name, last_name, wage, role, crud):
        self.first_name = first_name #instance variable
        self.last_name = last_name # instance variable
        self.wage = wage # instance variable, if you put self.__wage, then it will become private variable  
        self.role = role
        self.crud = crud
        self.save_to_database(self.crud)
    # _<class_name>__<private_variable>

    def save_to_database(self, crud):
        query = f"SELECT id FROM labours WHERE lower(first_name) = '{self.first_name}' AND lower(last_name) = '{self.last_name}'"
        logger.info(f"{query}")
        result = crud.read_from_mysql(query)

        if result: # if labour alraedy exists, return existing ID
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]
        email = self.first_name +"."+ self.last_name + "@gmail.com"
        insert_query = f"""
        INSERT INTO labours (first_name, last_name, wage, role, email)
        VALUES ('{self.first_name}','{self.last_name}',{self.wage},'{self.role}','{email}')
        """
        logger.info(f"{insert_query}")

        crud.insert_into_mysql(insert_query)

        result = crud.read_from_mysql(query)
        logger.info(f"New labour added with ID: {result[0][0]}")
        return result[0][0] 

#check if our user is already present in table?
# IF yes then skip saving and Insert into query and write

    @staticmethod
    def login_and_logout(crud, id=None, first_name=None, last_name=None):
        if id is None:
            if first_name is None or last_name is None:
                logger.error("Please provide either id or first name and last_name")
                return
            
            query = f"""
                    SELECT id from labours
                    WHERE lower(first_name) = '{first_name.lower()}'
                    AND lower(last_name)= '{last_name.lower()}'
                    """
            try:
                result = crud.read_from_mysql(query)
                id = result[0][0]
                logger.info(f"Id from labours table row #: {result[0][0]}")
            except IndexError:
                logger.error("Please register yourself. No entry found")
            except Exception as e:
                logger.error(f"Got error{e}")
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')

        check_query = f"""
            SELECT id, start_time, end_time FROM attendance
            WHERE labour_id = {id} AND DATE(start_time) = '{current_date}'
            """
        
        result = crud.read_from_mysql(check_query)
        logger.info(f"Data from labours table {result}")
        
        if len(result)== 0:
            insert_query = f"""
            INSERT INTO attendance (labour_id, start_time)
            VALUES ({id}, '{current_time}')
            """
            crud.insert_into_mysql(insert_query)
            logger.info(f"Labour {id} logged in at {current_time}")
        else:
            id = result[0][0]
            update_query = f"""
                    UPDATE attendance
                    SET end_time = '{current_time}'
                    WHERE id = {id}
                """
            crud.insert_into_mysql(update_query)
            logger.info(f"Labour {id} logged out at {current_time}")


