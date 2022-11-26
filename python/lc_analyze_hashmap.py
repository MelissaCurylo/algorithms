"""
Hash Notes:
    - Basic Operations:
        - Hash table: creates a new hash table.
        - Delete: deletes key:value pair from table.
        - Get: searches for key and returns key's value from table.
        - Put: inserts new key:value pair in table. 
        - Delete Hash Table: removes hash table. 


    - Hash Table:
        - Also known as Hash Map or Hash Tree. 
        - Implements an associative array (dictionary) via mapping key:value pairs through hash functions.
        - Array of stored pointers that point to records part of a collection of data. 
        - The data is stored in a way that makes searching and retrieving data efficient.


    - Hash Function:
        - Also known as hash code.
        - Used by hash table to compute an index into an array of buckets to store values. 
        - Function that converts a number or string to a integer value.
        - The converted value is mapped as an index in the hash table.
        - Good hash functions should have:
            - Quick and effective computablility.
            - Uniform distribution of keys.
                - The hash table positions should be equal for each key. 
        - At lookup, a key is hashed and the results from being hashed determine where value is stored.
            - This is why hashing is resourceful, only one hashed key uniquely to that particular index containing the buckets storing the values.
            - Each key has an indexed unique array of buckets. 
        - Space-Time Tradeoff:
            - If memory is infinite then entire key can be used as an index in order to locate the index value with single memory access.
        - Avoid Collisions


    - Hash Map:
        - Hash Map = {Key : Value} 
        - Hash Maps use Hash Function
        - Syntax: hash_map = {}
        - Data types: any
        - KeyError is returned when there isn't a key available after call. 
    
    - Hash Function Methods: 
        - mod method:
            - Takes the remainder of key divided by table size and maps the key into the slots of the table. 
            - key % table_size
    
    - Collisions:
        - Occurs when different keys convert to the same integer.
            - Data store at the key will be lost via being overwritten with new key being converted. 
        - Avoiding collision methods:
            - Prime numbers:
                - Design hash map by taking the size of hash table's array modulo 
            - Chaining: 
                - Stores linked lists inside the hash map array instead of the elements.
                - LL nodes store key:value pair. 
                - If collision occurs, the collided key:value pairs become linked together in a linked list. 
                    - Access to key:value pair is done by traversing linked list for key match.

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



# print(f"-----Block # 4-------------------------------------------")
# print(f"Using Classes to instantiate and create a hash table.\n")

# class hash_table:
#     def __init__(self, size):
#         self.size = size
#         self.hash_table = self.create_buckets()

#     def create_buckets(self):
#         return[[] for _ in range(self.size)]