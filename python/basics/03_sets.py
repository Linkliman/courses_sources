# 1. What are Sets?
# A set in Python is an unordered, mutable collection of unique elements. 
# Sets do not allow duplicates, and elements must be immutable (e.g., strings, numbers, tuples).

# Example of creating a set:
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Sets automatically remove duplicate elements:
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# You can also create a set using the `set()` function:
colors = set(["red", "green", "blue"])
print(colors)  # Output: {'green', 'blue', 'red'}

# 2. Adding and Removing Elements

# Add a single element using `add()`:
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Add multiple elements using `update()`:
fruits.update(["kiwi", "mango"])
print(fruits)  # Output: {'apple', 'banana', 'kiwi', 'orange', 'cherry', 'mango'}

# Remove an element using `remove()` (raises an error if the element doesn't exist):
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'kiwi', 'orange', 'cherry', 'mango'}

# Remove an element using `discard()` (no error if the element doesn't exist):
fruits.discard("banana")  # No error, even though 'banana' is not in the set
print(fruits)  # Output: {'apple', 'kiwi', 'orange', 'cherry', 'mango'}

# Remove and return an arbitrary element using `pop()`:
popped_fruit = fruits.pop()
print(popped_fruit)  # Output: 'apple' (or some other element, since sets are unordered)
print(fruits)        # Output: Set after an element is removed

# Clear the entire set using `clear()`:
fruits.clear()
print(fruits)  # Output: set()

# 3. Set Length
# You can use the `len()` function to get the number of elements in a set.

numbers = {1, 2, 3, 4, 5}
print(len(numbers))  # Output: 5

# 4. Checking for Membership
# You can check if an element exists in a set using the `in` operator.

print(3 in numbers)   # Output: True
print(6 in numbers)   # Output: False

# 5. Set Operations (Union, Intersection, Difference, Symmetric Difference)

# Union (| or union()): Combines all elements from both sets (removing duplicates)
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection (& or intersection()): Returns only elements that exist in both sets
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}

# Difference (- or difference()): Returns elements that are in the first set but not in the second
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}

# Symmetric Difference (^ or symmetric_difference()): Returns elements that are in one set or the other, but not both
sym_diff_set = set_a ^ set_b
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# 6. Set Methods

# `isdisjoint()`: Returns True if two sets have no elements in common
set_x = {1, 2, 3}
set_y = {4, 5, 6}
print(set_x.isdisjoint(set_y))  # Output: True

# `issubset()`: Returns True if all elements of one set are in another set
set_c = {1, 2}
set_d = {1, 2, 3, 4}
print(set_c.issubset(set_d))  # Output: True

# `issuperset()`: Returns True if one set contains all elements of another set
print(set_d.issuperset(set_c))  # Output: True

# `intersection_update()`: Modifies the set to keep only elements found in both sets
set_a.intersection_update(set_b)
print(set_a)  # Output: {3}

# `difference_update()`: Modifies the set to remove elements found in another set
set_d.difference_update({3, 4})
print(set_d)  # Output: {1, 2}

# `symmetric_difference_update()`: Modifies the set to keep only elements found in one set or the other, but not both
set_x.symmetric_difference_update({2, 3, 4})
print(set_x)  # Output: {1, 4}

# 7. Set Comprehensions
# Like list comprehensions, you can create sets using set comprehensions.

# Example: Create a set of squares of numbers from 1 to 5
squares_set = {n**2 for n in range(1, 6)}
print(squares_set)  # Output: {1, 4, 9, 16, 25}

# Example: Create a set of even numbers from a list
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_set = {n for n in numbers_list if n % 2 == 0}
print(evens_set)  # Output: {2, 4, 6, 8, 10}

# 8. Frozen Sets
# A frozenset is an immutable version of a set. Once created, elements cannot be added or removed from a frozenset.

# Creating a frozenset
frozen = frozenset([1, 2, 3, 4, 5])
print(frozen)  # Output: frozenset({1, 2, 3, 4, 5})

# Frozensets support the same set operations but cannot be modified.
print(frozen | {6, 7})  # Output: frozenset({1, 2, 3, 4, 5, 6, 7})
# frozen.add(6)  # This will raise an AttributeError since frozensets are immutable.

# 9. Performance Notes on Sets
# Sets are implemented using hash tables, making them very fast for membership checks, insertions, and deletions.
# Average time complexity:
# - Insertion: O(1)
# - Deletion: O(1)
# - Membership check: O(1)
# - Set operations (union, intersection, etc.): O(min(len(set1), len(set2)))
