user_info = {
    "Name" : "Rushikesh",
    "Age" : 18,
    "Fav_movie" : ["Robot", "Social Networks", "Twitter"],
    "Fav_tunes" : ["Tokyo Ghoul", "Weathering with you"]
}
# Find key present or not
'''
if "Fav_tunes" in user_info:
    print("True")
else:
   print("False")
'''

# Find value  present or not
'''
if "Rushikesh" in user_info.values():
    print("True")
else:
    print("False")
'''

for i in user_info.values():
    print(i)

# print("\n")

# print(user_info.values())
# print(type(user_info.values()))
# print("\n")

print(user_info.keys())

# print(user_info.keys())
 #print(type(user_info.keys()))


# print("\n")
# for i in user_info:
#     print(user_info[i])


for key1, value1 in user_info.items():
    print(f"{key1} is {value1}")


'''
user1 = dict(name = "e", age = 19, email="xyz@gmail.com")
print(user1)
print(type(user1))
'''
