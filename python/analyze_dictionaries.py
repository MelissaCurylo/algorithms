"""
Python Dictionary Notes:
    - Dictionary Syntax: dic = {}
    - Deleting:
        - del my_dict # deletes dictionary
        - del my_dict['yourkey'] # deletes key
    - Clear :
        - my_dict.clear()
    - Append an element:
        - my_dict["current_value_here"] = "new_value_here"
        - my_dict["current_value_here"].append("new_value_here") 
            - append() will not work on dictionaries with values as they do not have an append method use the option above, bracket notation.
            - Empty dictionaries will allow the use of append().

    - Remove Element:
        - my_dict.pop()
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

my_dict.pop("username")
print(f"This is the dictionary with the pop function: {my_dict}\n")



print(f"-----Block # 4-------------------------------------------")
del my_dict
# print(my_dict)
print(f"This space should be empty as delete function deletes my_dict.\n")


print(f"-----Block # 5-------------------------------------------")
my_dict = {"username": "Melissa Curylo", "email": "Melissa.Curylo@outlook.com", "favorite_meal": "Vegetarian Pad Thai"}
my_dict.clear()
print(f"Dictionary cleared: {my_dict}\n")

my_dict = {"username": "Melissa", "email": "Melissa.Curylo@outlook.com", "favorite_meal": "Vegetarian Pad Thai"}
my_dict_add_on = {"first_name": "Melissa", "last_name": "Curylo"}

# my_dict["username"].append("GirlCoder") # dictionaries don't have append() method use below instead:
my_dict["username"] = "GirlCoder"
print(f"Dictionary with the appeneded key:value pair:\n {my_dict}\n")
my_dict["full_name"] = my_dict_add_on
print(f"Dictionary updated with combined dictionaries: \n{my_dict}\n")


print(f"-----Block # 6-------------------------------------------")
new_dict = {"name": []}
new_dict["name"].append("GirlCoder")
print(f"Using append() on an empty dictionary: {new_dict}\n")

