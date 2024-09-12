# 1. What are Loops?
# Loops allow you to repeat a block of code multiple times.
# Python has two types of loops: `for` loops and `while` loops.

# 2. `for` Loops
# A `for` loop is used to iterate over a sequence (like a list, tuple, string, or range).

# Example: Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# Example: Looping through a string (character by character)
word = "Python"
for letter in word:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

# Example: Using `range()` to loop a specific number of times
# The `range(start, stop, step)` function generates a sequence of numbers.

for i in range(5):  # Loops from 0 to 4 (stop is exclusive)
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# You can also specify a start and step in `range()`.
for i in range(1, 10, 2):  # Loops from 1 to 9, with a step of 2
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

# 3. `while` Loops
# A `while` loop runs as long as the condition remains True.

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Don't forget to update the condition, otherwise you'll get an infinite loop!

# Output:
# Count is: 0
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4

# 4. Loop Control Statements: `break`, `continue`, and `pass`

# `break`: Terminates the loop entirely.

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# `continue`: Skips the current iteration and moves to the next one.

for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)

# Output:
# 0
# 1
# 3
# 4

# `pass`: Does nothing. It acts as a placeholder when a loop must have a statement but you want to do nothing.
for i in range(3):
    if i == 1:
        pass  # Do nothing when i is 1
    print(i)

# Output:
# 0
# 1
# 2

# 5. Nested Loops
# A loop inside another loop is called a nested loop.

# Example: Nested `for` loop
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1

# Example: Nested `while` loop
i = 1
while i < 4:
    j = 1
    while j < 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2

# 6. Looping with Conditionals (Combining Loops and Conditionals)

# Example: Printing only even numbers using a loop and condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")

# Output:
# 2 is even
# 4 is even
# 6 is even
# 8 is even
# 10 is even

# Example: Breaking out of a loop when a condition is met
for number in numbers:
    if number == 7:
        print("Number 7 found, stopping the loop.")
        break
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# Number 7 found, stopping the loop.

# Example: Skipping numbers using `continue`
for number in numbers:
    if number % 2 != 0:
        continue  # Skip odd numbers
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10

# 7. Iterating Through Complex Structures (Lists, Dictionaries, and Sets)

# List Iteration
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Output:
# red
# green
# blue

# Dictionary Iteration (keys, values, and items)
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over keys
for key in person:
    print(key)

# Output:
# name
# age
# city

# Iterate over values
for value in person.values():
    print(value)

# Output:
# John
# 30
# New York

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: John
# age: 30
# city: New York

# Set Iteration
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5

# 8. Looping with `enumerate()` and `zip()`

# `enumerate()`: Loop with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# `zip()`: Loop through two or more sequences at the same time
names = ["John", "Jane", "Alice"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Output:
# John scored 85
# Jane scored 90
# Alice scored 78

# 9. Comprehensions with Loops (List, Set, and Dictionary Comprehensions)

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Set Comprehension
unique_squares = {x**2 for x in range(5)}
print(unique_squares)  # Output: {0, 1, 4, 9, 16}

# Dictionary Comprehension
names = ["John", "Jane", "Alice"]
scores = [85, 90, 78]
name_score_dict = {name: score for name, score in zip(names, scores)}
print(name_score_dict)  # Output: {'John': 85, 'Jane': 90, 'Alice': 78}

# 10. Using the `else` Keyword with Loops
# The `else` block in loops is executed when the loop completes all iterations normally,
# meaning it does not hit a `break` statement. This is particularly useful when you need
# to check if a loop finished without interruptions or breaks.

# Example: `else` with `for` loop

# Search for a number in a list, if found, break the loop. If not found, execute the `else` block.
numbers = [1, 2, 3, 4, 5]
target = 7

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break
else:
    print(f"{target} is not in the list.")  # This will be printed

# Output:
# 7 is not in the list.

# In this example, the loop completes without finding the number 7, so the `else` block is executed.
# If the target was found, the loop would break, and the `else` block would not run.

# Example: `else` with `while` loop

# Using a `while` loop to search for a number in a sequence
i = 0
while i < len(numbers):
    if numbers[i] == target:
        print(f"{target} found in the list!")
        break
    i += 1
else:
    print(f"{target} is not in the list.")  # This will be printed

# Output:
# 7 is not in the list.

# Example: Using `else` with a `for` loop that does not `break`
for i in range(3):
    print(i)
else:
    print("Loop completed without a break.")  # This will be printed after all iterations

# Output:
# 0
# 1
# 2
# Loop completed without a break.

# Example: Using `else` with a `for` loop that has a `break`
for i in range(3):
    print(i)
    if i == 1:
        break  # Loop will break when i is 1
else:
    print("This will not be printed because the loop broke.")

# Output:
# 0
# 1

# Summary of `else` with Loops:
# - The `else` block in loops executes when the loop finishes its iterations without being interrupted by a `break`.
# - If the loop hits a `break`, the `else` block will be skipped.
# - `else` is useful in scenarios like searching or validation, where you want to confirm if a condition was met
#   during the loop or not.
