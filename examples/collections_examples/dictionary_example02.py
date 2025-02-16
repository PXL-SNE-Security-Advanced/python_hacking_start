# dictionary_example02.py
# Creating a dictionary with a record for John
people_dict = {
    'John': {'age': 30, 'city': 'New York', 'occupation': 'Engineer'},
    'Dominique': {'age': 40, 'city': 'Kortessem', 'occupation': 'Lector'},
    
}

# Adding a record for Eva
people_dict['Eva'] = {'age': 26, 'city': 'London', 'occupation': 'Doctor'}

# Accessing information of Eva
print("\nInformation of Eva:")
print("Age:", people_dict['Eva']['age'])
print("City:", people_dict['Eva']['city'])
print("Occupation:", people_dict['Eva']['occupation'])

print()
print("people_dict all:", people_dict)

# Removing the entry for Dominique
del people_dict['Dominique']

print()
print("people_dict after removing Dominique:", people_dict)

'''
Information for Eva:
Age: 26
City: London
Occupation: Doctor

people_dict all: {'John': {'age': 30, 'city': 'New York', 'occupation': 'Engineer'}, 'Dominique': {'age': 40, 'city': 'Kortessem', 'occupation': 'Lector'}, 'Eva': {'age': 26, 'city': 'London', 'occupation': 'Doctor'}}

people_dict after removing Dominique: {'John': {'age': 30, 'city': 'New York', 'occupation': 'Engineer'}, 'Eva': {'age': 26, 'city': 'London', 'occupation': 'Doctor'}}
'''