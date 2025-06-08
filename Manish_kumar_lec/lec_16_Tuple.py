# 1. Write a program to return entire element as a tuple
# which can have a list in the tuple input 
# 
# test_tuple = ([5,6], [6,7,8,9], [3])
# result = ()
# for lst in test_tuple:
#     new_var = tuple(lst)
#     result = result + new_var
# print(tuple(result))

# 2. Write a program to return a tuple which is
# exponential (power like square/cube) of given two tuples as an input

tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)
result = ()
for i in range(len(tuple1)):
    new_var = tuple1[i] ** tuple2[i]
    result = (result) + (new_var,)
print (tuple(result))


