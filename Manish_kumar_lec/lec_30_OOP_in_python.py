from loguru import logger

class User:
    name = "manish"
    def __init__(self, ip, phone_details, location = None):
        self.ip = ip
        self.phone_details = phone_details
        self.location = location
    
    def signup(self):
        pass

    def login(self):
        pass

    def profile_update(self):
        pass



user1 = User("10.123.1.10", "Samsung/Android")
logger.info(f"{user1}")
logger.info(f"{user1.__dict__}")
print(f"{dir(user1)}")
user2 = User("10.123.1.12", "Iphone 16/iOS","Bangalore")
logger.info(f"{user2.__dict__}")