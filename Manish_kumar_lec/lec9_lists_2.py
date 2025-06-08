from loguru import logger

labour_name = ["Mahesh", "Suresh", "Mithilesh", "Sumesh", 500, 400, 400, 300]

# new_labour = ["Ram", "Mohan"]

# full_labour_name = labour_name + new_labour

# logger.info(f"Full list of labours {full_labour_name}")

# Accessing the list
# logger.info(f"Give me firt two element from the list: {labour_name[0:2]}")

# To get list in reverse order,
# logger.info(f"Give me the list in reverse order: {labour_name[::-1]}")

# length (len) will give number of elements in the list
# logger.info(f"How many elements are there in the list: {len(labour_name)}")

# Insert will add an element in the list where you want, if you do not specify

# labour_name.insert(4,"Ram")
# logger.info(f"Give me updated list: {labour_name}")

# labour_name.insert(8,600)
# logger.info(f"Give me updated list: {labour_name}")

# pop mentod: used to delete the element from the list

# labour_name.pop()
# logger.info(f"Give me updated list: {labour_name}")

# labour_name.pop(4)
# logger.info(f"Give me updated list: {labour_name}")

#'remove' will remove an element from the list
# labour_name.remove(400)
# logger.info(f"Give me updated labour list: {labour_name}")

# Delete will be used to delete the entire list
# del labour_name
# logger.info(f"Give me updated labour list: {labour_name}")
# It will give you NameError: labour_name not defined because it is deleted by using del

# change the list value
# labour_name[0] = "Maheshji"
# logger.info(f"Give me updated labour list: {labour_name}")
# labour_name[0:4] = ["Maheshji, Sureshji", "Mithileshji", "Sumeshji"]
# logger.info(f"Give me updated labour list: {labour_name}")

# # split method
# api_endpoint = "https://github.com/darshilparmar/kafka-in-10min-video-code/blob/main/commands"

# new_api_endpoint = api_endpoint.split('/')

# logger.info(f"Give me breakdown of api_endpoint: {new_api_endpoint}")
# logger.info(f"Give me blob from api_endpoint: {new_api_endpoint[-3]}")

# Sorting
# labour_name_new = [500,600,400,400,300]
# labour_name_new.sort()
# logger.info(f"Give me sorted labour list:{labour_name_new} ")
# labour_name.sort()

# logger.info(f"Give me updated labour list: sorted{labour_name}")