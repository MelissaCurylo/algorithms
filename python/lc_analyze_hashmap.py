"""
Python Dictionary Notes:
    - Dictionary Syntax: dic = {}
    - Deleting:
        - del my_dict # deletes dictionary
        - del my_dict['yourkey'] # deletes key
    - Clearing:
        - my_dict.clear()
"""
print("\n")
print(f"-------------------------------------------")
print(f"| *Analyzing Dictionary Functions*        |")   
print(f"-------------------------------------------\n")

print(f"-----Block # 1-------------------------------------------")
my_dict = {"username": "MelissaLynn", "email": "Melissa.Curylo@outlook.com", "favorite meal": "Vegetarian Pad Thai"}
print("username : ", my_dict['username'])
print(f"{my_dict}\n")



print(f"-----Block # 2-------------------------------------------")
# print("Dictionary Position #2: ", my_dict[2]) #  returns KeyError, cannot pull like hash map as these are strings.
print("Position # 2 holds: ", my_dict['email']) # in order to pull position 2 then need to know key name versus index.

my_dict[4] = 2
print("Position # 4 holds: ", my_dict[4])

my_dict[5] = "Cats are awesome!"
print(f"Position # 5 holds: {my_dict[5]}\n")



print(f"-----Block # 3-------------------------------------------")
del my_dict[4]
# print(my_dict[4]) # prints KeyError becauase [4] is deleted
my_dict["username"] = 'Melissa'
print(f"{my_dict['username']}\n")



print(f"-----Block # 4-------------------------------------------")
del my_dict
# print(my_dict)
print(f"This space should be empty as delete function deletes my_dict.\n")


print(f"-----Block # 5-------------------------------------------")
my_dict = {"username": "Melissa Curylo", "email": "Melissa.Curylo@outlook.com", "favorite_meal": "Vegetarian Pad Thai"}
my_dict.clear()
print(f"Dictionary cleared: {my_dict}\n")

my_dict = {"username": "GirlCoder", "email": "Melissa.Curylo@outlook.com", "favorite_meal": "Vegetarian Pad Thai"}
my_dict_add_on = {"first_name": "Melissa", "last_name": "Curylo"}
my_dict["full_name"] = my_dict_add_on
print(f"Dictionary updated with combined dictionaries: \n{my_dict}\n")


"""
Hash Map Notes:
    - Hash Map = {Key : Value} 
    - Syntax: hash_map = {}
    - Data types: any
    - KeyError is returned when there isn't a key available after call. 
"""
print("\n")
print(f"-------------------------------------------")
print(f"| *Analyzing Hash Map Functions*          |")   
print(f"-------------------------------------------\n")

print(f"-----Block # 1-------------------------------------------")
my_hash_map = {}
my_hash_map[2] = 91
my_hash_map[3] = "Hello World"
my_hash_map[4]= 55
print(f"Content of Hash Map: {my_hash_map[2]}, {my_hash_map[3]}, {my_hash_map[4]}\n")

print(f"-----Block # 2-------------------------------------------")
print(4 in my_hash_map) # prints True
print(854 in my_hash_map) # prints Fasle because it doesn't exist.
print(f"Content of Hash Map: {my_hash_map}\n")


print(f"-----Block # 3-------------------------------------------")
for key, val in my_hash_map.items():
    print(f"These are the paired key:value ->  {key} : {val}\n")