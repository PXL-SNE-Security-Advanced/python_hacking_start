# dictionary_example01.py
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values using keys
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 30

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'

# Modifying a value
my_dict['age'] = 32

# Removing a key-value pair
del my_dict['city']

# Accessing keys, values, and items
print("Keys:", my_dict.keys())     # Output: dict_keys(['name', 'age', 'occupation'])
print("Values:", my_dict.values()) # Output: dict_values(['John', 32, 'Engineer'])
print("Items:", my_dict.items())   # Output: dict_items([('name', 'John'), ('age', 32), ('occupation', 'Engineer')])

print()
print("my_dict:", my_dict)

'''
John
30
Keys: dict_keys(['name', 'age', 'occupation'])
Values: dict_values(['John', 32, 'Engineer'])
Items: dict_items([('name', 'John'), ('age', 32), ('occupation', 'Engineer')])

my_dict: {'name': 'John', 'age': 32, 'occupation': 'Engineer'}
'''


