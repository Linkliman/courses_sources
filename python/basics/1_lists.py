# 1. What are Lists?
# A list in Python is a collection of items that are ordered, mutable, and can contain duplicates.
# Lists are one of the most commonly used data structures in Python.

# Example:
fruits = ["apple", "banana", "cherry"]

# Lists can hold different data types, including strings, numbers, booleans, or even other lists.
mixed_list = [1, "hello", True, [2, 3, 4]]

# 2. Accessing Elements in a List
# Lists are zero-indexed, meaning the first element is at index 0.
# You can access elements in a list using square brackets.

# Example:
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# You can also access elements using negative indexing (counting from the end).
print(fruits[-1])  # Output: cherry (last element)

# 3. Modifying Lists
# Lists are mutable, so you can change the elements after the list is created.

# Change the second element
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# 4. Adding and Removing Elements

# Add an element to the end of the list using `append()`
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Insert an element at a specific index using `insert()`
fruits.insert(1, "banana")  # Insert "banana" at index 1
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'orange']

# Remove an element using `remove()`
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Remove the last element using `pop()`
last_fruit = fruits.pop()
print(last_fruit)  # Output: orange (the popped element)
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 5. List Slicing
# You can extract a subset of a list using slicing, which uses the syntax list[start:end].
# The `start` index is inclusive, and the `end` index is exclusive.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract elements from index 2 to 5 (5 is not included)
print(numbers[2:5])  # Output: [2, 3, 4]

# Extract elements from the beginning up to index 4
print(numbers[:5])  # Output: [0, 1, 2, 3, 4]

# Extract elements from index 5 to the end
print(numbers[5:])  # Output: [5, 6, 7, 8, 9]

# You can also use a step in slicing:
print(numbers[::2])  # Output: [0, 2, 4, 6, 8] (every second element)

# Reverse the list using slicing
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 6. List Comprehensions
# List comprehensions provide a concise way to create lists. 
# It consists of brackets containing an expression followed by a for loop.

# Example: Create a list of squares of numbers from 0 to 9
squares = [n**2 for n in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehensions can also have conditions:
even_squares = [n**2 for n in range(10) if n % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# 7. Common List Methods

# Length of the list
print(len(fruits))  # Output: 3

# Check if an element exists in the list using `in`
print("apple" in fruits)  # Output: True

# Sorting a list
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Reversing a list
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# Count occurrences of an element
print(fruits.count("apple"))  # Output: 1

# 8. Nested Lists
# Lists can contain other lists, making them two-dimensional (or multi-dimensional) arrays.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list:
print(matrix[0][0])  # Output: 1 (first element of the first row)
print(matrix[1][2])  # Output: 6 (third element of the second row)

# List comprehension with nested lists:
flattened = [item for row in matrix for item in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
