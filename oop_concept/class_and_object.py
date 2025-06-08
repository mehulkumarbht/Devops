from loguru import logger
# from src.main.databases.mysql_connector import MySqlConnection, MySQLCRUDOperation
# from src.main.encrypt_decrypt.lec_25_encryption_decryption import decrypt
import configparser
# config = configparser.ConfigParser()
# config.read(r"C:\Users\mehul\Documents\Programming\src\resources\config_file.ini")
# config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

class Labour:
    no_of_labours = 0 # count = 0 # class variable
    def __init__(self, first_name, last_name, wage, role):
        self.first_name = first_name #instance variable
        self.last_name = last_name # instance variable
        self.wage = wage # instance variable, if you put self.__wage, then it will become private variable  
        self.role = role
        Labour.no_of_labours +=1
        
# _<class_name>__<private_variable>

    def save_to_database(self):
        query = "SELECT id FROM labours WHERE lower(first_name) = %s AND lower(last_name) = %s"
        logger.info(f"{query}")
        result = self.crud.read_from_mysql(query, (self.first_name, self.last_name))

        if result: # if labour alraedy exists, return existing ID
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]
        # email = self.first_name +"."+ self.last_name + "@gmail.com"
        # insert_query = f"""
        # INSERT INTO labours (first_name, last_name, wage, role, email)
        # VALUES ('{self.first_name}','{self.last_name}',{self.wage},'{self.role}','{email}')
        # """
        # logger.info(f"{insert_query}")

        # crud.insert_into_mysql(insert_query)

        # result = crud.read_from_mysql(query)
        # logger.info(f"New labour added with ID: {result[0][0]}")
        # return result[0][0] 

#check if our user is already present in table?
# IF yes then skip saving and Insert into query and write
    def login(self):
        pass

    @classmethod # class method
    def total_no_of_labours(cls):
        return Labour.no_of_labours

    @staticmethod # static method
    def is_valid_wage(your_wage):
        if your_wage<=200:
            logger.info("Ask for a fair wages")
        else:
            logger.info("Your wage is more than minimum specified")



# logger.info(f"{Labour.no_of_labours}")
manish_obj = Labour("Manish", "Kumar", 500,"labour")
# logger.info(f"{Labour.no_of_labours}")
rajesh_obj = Labour("Rajesh", "Singh", 400, "Mistry")
# logger.info(f"{Labour.no_of_labours}")
print(Labour.total_no_of_labours())
print(Labour.is_valid_wage(200))
