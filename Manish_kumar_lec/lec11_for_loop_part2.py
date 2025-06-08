# from loguru import logger

# # count = 0
# # paragraph =""" Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
# # data warehouse and business intelligence industry’s thought leader on the dimen
# # sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
# # books written by Ralph and his colleagues have been the industry’s best sellers 
# # since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
# # coinvented the Star workstation, the fi rst commercial product with windows, icons, 
# # and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
# # electrical engineering from Stanford University """

# # lst = paragraph.lower().split(" ")
# # logger.info(f"{lst}")

# # for letter in lst:
# #     if letter == "the":
# #         count = count+1
# #     else:
# #         continue
# # logger.info(f"Give me count of the: {count}")


# # Insert 100 in the list [5,18,77,108,930] in sorted order

# # number_list =[5, 18, 77, 108, 930]
# # number_to_insert = 100

# # index = 0
# # for number in number_list:
# #     if number>number_to_insert:
# #         index = index
# #         break
# #     else: 
# #         index = index+1
# # logger.info(f"{index}")

# # number_list.append('None')
# # for i in range(len(number_list)-1, index, -1):
# #     number_list[i]=number_list[i-1] 

# # number_list[index] = number_to_insert
# # logger.info(f"{number_list}")

# # lst = [202,165,89,76,12]
# # number_to_insert = 15
# # Insert the number in a way the list is sorted in descending order

# lst = [202,165,89,76,12]
# number_to_insert = 15
# index = 0

# for number in lst:
#     if number<number_to_insert:
#         index = index
#         break
#     else:
#         index = index+1

# logger.info(f"index = {index}")

# lst.append('None')
# logger.info(f"{lst}")

# for i in range(len(lst)-1,index,-1):
#     lst[i]=lst[i-1]

# lst[index]=number_to_insert
# logger.info(f"{lst}")