from loguru import logger

# name = "Mehul kumar"
# lst = [19,34,52,59,49]
# counter = 0
# for char in name:
#     print(counter,char)
#     counter += 1

# print(name[ :4])

# for number in lst:
#     print(counter, number)
#     counter += 1

# name = "Mehul kumar "
# print(name.capitalize())
# print(name.count("m"))
# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))
# print(chr(97))

# print(name.endswith("r"))
# print(name.islower())
# print(name.upper())
# print(name.lower())
# new_names = name.replace("Mehul", "Manish")
# print(new_names)

# print(len(name))
# print(name.strip())
# print(len(name.strip()))

# print(name.swapcase())

# counter = 0
# for char in name:
#     if char.islower():
#         print(counter,char.upper())
#     else:
#         print(counter,char.lower())
#     counter += 1


# # Assignment =1
# name = "Programming Aasan Hai"
# lst = ""
# for char in name:
#     if char.isupper():
#          lst = lst+char.lower()
#     if char.islower():
#         lst = lst+char.upper()
# print(lst)
    
    
# name = "Manish ram mohan sohan ramesh"
# names = name.split(" ")
# print(names)

# lst = []
# for name in names:
#     if name.endswith("h"):
#         lst.append(name)
#     else:
#         print(f"{name} does not end with h")

# Assignment = 2: Convert these email ids in *** except first last character/number
lst = "shikhar_dhavan1997@yahoo.com"
for i in lst:
    name,domain = lst.split("@")
    if len(name)>2:
        mask = name[0]+'*'*(len(name)-2)+name[-1]
    else:
        mask = name
    mask_with_domain = mask + '@' + domain
print(mask_with_domain)

#Assignment =3:
# input = ["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
# "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
# "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
# "/region//japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
# "/region//india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
# "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
# "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
# "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"]

# # Output:- ["10.168.155.2","10.168.156.2","10.168.151.2"
# #            "10.168.155.22","10.168.167.2",
# #            "10.168.179.28","10.168.155.31" ]
# ip = []
# for number in input:
#     ip.append(number.split("/")[10])
# print(list(ip))