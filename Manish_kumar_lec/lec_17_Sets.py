from loguru import logger

list1 = {1,2,3,4,5,6}
list2 = {4,5,6,7,8}
# Missing values in list1 = [8,7]
# Additional values in list1 = [1,2,3]
# Missing values in list2 = [1,2,3]
# Additional values in list2 = [7,8]
# logger.info(f"Missing values in list1 = {list2.difference(list1)}")
# logger.info(f"Missing values in list2 = {list1.difference(list2)}")
# logger.info(f"Additional values in list1 = {list1.difference(list2)}")
# logger.info(f"Missing values in list2 = {list2.difference(list1)}")


ar1 = {1,5,10,20,40,80}
ar2 = {6,7,20,80,100}
ar3 = {3,4,15,20,30,70,80,120}

# output = [80,20]

# print(ar1.intersection(ar2))

final_output = []
for number in ar1:
    if number in ar2 and number in ar3:
        final_output.append(number)
    else:
        continue
print(final_output)