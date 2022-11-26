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