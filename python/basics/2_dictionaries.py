# 1. What are Dictionaries?
# A dictionary in Python is an unordered, mutable, and indexed collection of key-value pairs.
# Each key is associated with a value, and keys must be unique and immutable (e.g., strings, numbers, tuples).

# Example:
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 2. Accessing Dictionary Elements
# You can access values in a dictionary by referring to their keys.

# Access value using key
print(person["name"])  # Output: John
print(person["age"])   # Output: 30

# You can also use the `get()` method to access values safely (returns `None` if the key is not found).
print(person.get("name"))  # Output: John
print(person.get("job", "Not specified"))  # Output: Not specified (because 'job' key doesn't exist)

# 3. Adding and Modifying Elements in a Dictionary

# Adding a new key-value pair:
person["job"] = "Engineer"
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Modifying an existing value:
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# 4. Removing Elements from a Dictionary

# Remove a key-value pair using `pop()`
age = person.pop("age")
print(age)  # Output: 31
print(person)  # Output: {'name': 'John', 'city': 'New York', 'job': 'Engineer'}

# Remove the last inserted key-value pair using `popitem()`
last_item = person.popitem()
print(last_item)  # Output: ('job', 'Engineer')
print(person)  # Output: {'name': 'John', 'city': 'New York'}

# Remove a key-value pair using `del`
del person["city"]
print(person)  # Output: {'name': 'John'}

# Clear the entire dictionary
person.clear()
print(person)  # Output: {}

# 5. Dictionary Length
# You can use the `len()` function to get the number of key-value pairs in a dictionary.

person = {"name": "John", "age": 30, "city": "New York"}
print(len(person))  # Output: 3

# 6. Checking if a Key Exists
# You can check if a specific key exists in a dictionary using the `in` operator.

print("name" in person)  # Output: True
print("job" in person)   # Output: False

# 7. Iterating Through a Dictionary

# Loop through keys:
for key in person:
    print(key, person[key])

# Output:
# name John
# age 30
# city New York

# Loop through values:
for value in person.values():
    print(value)

# Output:
# John
# 30
# New York

# Loop through key-value pairs:
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: John
# age: 30
# city: New York

# 8. Dictionary Methods

# `keys()`: Returns a list-like object containing all the keys in the dictionary
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# `values()`: Returns a list-like object containing all the values in the dictionary
values = person.values()
print(values)  # Output: dict_values(['John', 30, 'New York'])

# `items()`: Returns a list-like object containing key-value pairs (as tuples)
items = person.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# `update()`: Merges another dictionary into the current dictionary
person.update({"job": "Engineer", "age": 31})  # Updates age and adds job
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# `copy()`: Creates a shallow copy of the dictionary
person_copy = person.copy()
print(person_copy)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# 9. Nested Dictionaries
# Dictionaries can contain other dictionaries (or other data structures), creating a nested dictionary.

company = {
    "employee_1": {
        "name": "Alice",
        "age": 28,
        "job": "Developer"
    },
    "employee_2": {
        "name": "Bob",
        "age": 35,
        "job": "Manager"
    }
}

# Accessing nested dictionary elements:
print(company["employee_1"]["name"])  # Output: Alice
print(company["employee_2"]["job"])   # Output: Manager

# Modifying values in nested dictionaries:
company["employee_1"]["age"] = 29
print(company["employee_1"]["age"])  # Output: 29

# Adding a new employee:
company["employee_3"] = {
    "name": "Charlie",
    "age": 22,
    "job": "Intern"
}
print(company)

# 10. Dictionary Comprehensions
# Just like list comprehensions, you can create dictionaries using dictionary comprehensions.

# Example: Create a dictionary where keys are numbers and values are their squares.
squares = {n: n**2 for n in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example: Create a dictionary from two lists (using zip to pair keys and values)
keys = ["name", "age", "job"]
values = ["John", 30, "Engineer"]
person_dict = {k: v for k, v in zip(keys, values)}
print(person_dict)  # Output: {'name': 'John', 'age': 30, 'job': 'Engineer'}

# 11. Merging Dictionaries
# Python 3.9+ introduced the `|` (pipe) operator to merge dictionaries.

dict_a = {"name": "Alice", "age": 28}
dict_b = {"job": "Developer", "city": "San Francisco"}

merged_dict = dict_a | dict_b
print(merged_dict)  # Output: {'name': 'Alice', 'age': 28, 'job': 'Developer', 'city': 'San Francisco'}

# You can also use the `update()` method (as seen earlier):
dict_a.update(dict_b)
print(dict_a)  # Output: {'name': 'Alice', 'age': 28, 'job': 'Developer', 'city': 'San Francisco'}

# 12. Dictionary Performance Notes
# - Dictionaries in Python use hash tables, making them extremely efficient for lookups, insertions, and deletions.
# - The average time complexity for these operations is O(1).

# Conclusion:
# Dictionaries are a powerful and flexible data structure in Python. They allow for fast lookups, storing key-value pairs, 
# and can be nested for more complex data storage. Mastering dictionaries is essential for Python programming.
