"""
Python Dictionary Notes:
- Dictionary Syntax: dic = {}
"""
my_dict = {"username": "MelissaLynn", "email": "Melissa.Curylo@outlook.com", "favorite meal": "Vegetarian Pad Thai"}
print("username : ", my_dict['username'])
print(my_dict)
print("-------------------------------------------")

# print("Dictionary Position #2: ", my_dict[2]) #  returns KeyError, cannot pull like hash map as these are strings.
print("Position # 2 holds: ", my_dict['email']) # in order to pull position 2 then need to know key name versus index.

my_dict[4] = 2
print("Position # 4 holds: ", my_dict[4])

my_dict[5] = "Cats are awesome!"
print("Position # 5 holds: ", my_dict[5])

print("-------------------------------------------")
print(my_dict)
print("-------------------------------------------")




"""
Hash Map Notes:
    - Hash Map = {Key : Value} 
    - Syntax: hash_map = {}
    - Data types: any
    - KeyError is returned when there isn't a key available after call. 
"""

my_hash_map = {}
my_hash_map[2] = 91
my_hash_map[3] = "Hello World"
my_hash_map[4]= 55
print("-------------------------------------------")

print(my_hash_map[2], my_hash_map[3], my_hash_map[4])
print(4 in my_hash_map) # prints True
print(854 in my_hash_map) # prints Fasle because it doesn't exist.
print(my_hash_map)
print("-------------------------------------------")


for key, val in my_hash_map.items():
    print(f"These are the paired key:value ->  {key} : {val}")