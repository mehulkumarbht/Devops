from loguru import logger
from src.main.databases.mysql_connector import MySqlConnection, MySQLCRUDOperation
from src.main.encrypt_decrypt.lec_25_encryption_decryption import decrypt
import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\mehul\Documents\Programming\src\resources\config_file.ini")
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

class Labour:
    # count = 0 # class variable
    def __init__(self, first_name, last_name, wage, role,crud):
        self.first_name = first_name #instance variable
        self.last_name = last_name # instance variable
        self.wage = wage # instance variable, if you put self.__wage, then it will become private variable  
        self.role = role
        self.crud = crud
        # Labour.count += 1 If you want to count total number workers
        self.save_to_database(crud)

# _<class_name>__<private_variable>

    def save_to_database(self, crud):
        query = f"SELECT id FROM labours WHERE lower(first_name) = '{self.first_name}' AND lower(last_name) = '{self.last_name}'"
        logger.info(f"{query}")
        result = crud.read_from_mysql(query)

        if result: # if labour alraedy exists, return existing ID
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]
        email = self.first_name +'.'+ self.last_name + '@gmail.com'
        insert_query = f"""
        INSERT INTO labours (first_name, last_name, wage, role, email)
        VALUES ('{self.first_name}','{self.last_name}',{self.wage},'{self.role}','{email}')
        """

        
        crud.insert_into_mysql(insert_query)

        result = crud.read_from_mysql(query)
        logger.info(f"New labour added with ID: {result[0][0]}")
        return result[0][0] 

#check if our user is already present in table?
# IF yes then skip saving and Insert into query and write
    def login(self):
        pass

config = configparser.ConfigParser()
config.read(r"C:\Users\mehul\Documents\Programming\src\resources\config_file.ini")
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

mysql_db_conn_obj = MySqlConnection(config)
mysql_db_conn_obj.connect()
crud = MySQLCRUDOperation(mysql_db_conn_obj.connection)

manish_obj = Labour("Manish", "Kumar", 500,"labour", crud)
manish_obj.save_to_database(crud)
# print(manish_obj._Labour__wage)
# print(manish_obj._last)
ramesh_obj = Labour("Ramesh", "Singh", 400, "Mistri", crud)
ramesh_obj.save_to_database(crud)
# logger.info(f"{ramesh_obj}")
# print(Labour.total_count)
# logger.info(f"{Labour.count}")

    #(first_name, last_name, wage)