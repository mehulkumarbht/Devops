from loguru import logger
from src.main.databases.mysql_connector import *
from src.main.encrypt_decrypt.lec_25_encryption_decryption import decrypt
from src.main.labours.labours_class import Labour
import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\mehul\Documents\Programming\src\resources\config_file.ini")
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

def main():
    
    mysql_db_conn_obj = MySqlConnection(config)
    mysql_db_conn_obj.connect()
    crud = MySQLCRUDOperation(mysql_db_conn_obj.connection)
    Labour.login_and_logout(crud, first_name="Sohan", last_name="Singh")
    # manish_obj = Labour("Sohan","Singh", 600,"labour", crud)
    # rajesh_obj = Labour("Rajesh", "Singh", 400, "Mistry")
    # manish_obj.save_to_database(crud)
    # rajesh_obj.save_to_database(crud)


if __name__=="__main__":
    main()