# 1. What are Variables?
# A variable in Python is a name that is used to refer to a value stored in memory.
# Variables can store different types of data, and their values can change during execution.

# Example:
x = 10  # `x` is a variable holding an integer value
y = "Hello, Python!"  # `y` is a variable holding a string value

# 2. Naming Conventions
# Variable names must start with a letter or an underscore (_) and can be followed by letters, numbers, or underscores.
# Variable names are case-sensitive. Lowercase letters are commonly used.

# Examples of valid variable names:
age = 25
user_name = "John"
_country = "USA"

# Examples of invalid variable names:
# 1user = "Jane"   # Variable name cannot start with a number
# @score = 90      # Variable name cannot contain special characters like @, $, etc.

# 3. Basic Variable Types

# Integer (int) - Whole numbers without decimals
age = 30

# Float (float) - Numbers with decimals
temperature = 36.6

# String (str) - Sequence of characters enclosed in quotes
greeting = "Hello, World!"

# Boolean (bool) - Logical values, True or False
is_raining = False

# You can check the type of a variable using the `type()` function:
print(type(age))  # Output: <class 'int'>
print(type(temperature))  # Output: <class 'float'>
print(type(greeting))  # Output: <class 'str'>
print(type(is_raining))  # Output: <class 'bool'>

# 4. Type Casting
# You can convert between types using casting functions like `int()`, `float()`, `str()`, and `bool()`.

# Convert a float to an integer
pi = 3.14159
pi_int = int(pi)  # Result: 3 (decimal part is truncated)

# Convert a string to an integer
num_str = "100"
num_int = int(num_str)  # Result: 100

# Convert an integer to a string
age_str = str(age)  # Result: "30"

# Convert a value to boolean
zero_bool = bool(0)  # Result: False
one_bool = bool(1)  # Result: True

# 5. Multiple Assignments
# You can assign multiple variables in a single line using tuple unpacking.

# Assigning different values to different variables
a, b, c = 5, "apple", 3.14

# Swapping values between variables
x, y = 10, 20
x, y = y, x  # After swapping: x is 20, y is 10

# 6. Dynamic Typing in Python
# Python is dynamically typed, which means you don't need to declare the type of a variable.
# You can assign a value of any type to a variable and even reassign it to a different type later.

# Example:
var = 42  # Initially an integer
var = "Now I'm a string!"  # Now it's a string

# 7. Global vs Local Variables
# Variables defined inside a function are local and accessible only within that function.
# Global variables are accessible throughout the program.

global_var = "I'm global!"

def my_function():
    local_var = "I'm local!"
    print(local_var)  # This works
    print(global_var)  # Global variables are accessible inside the function

my_function()

# print(local_var)  # This will raise an error because local_var is not accessible outside the function

# You can modify a global variable inside a function using the `global` keyword:
def modify_global():
    global global_var
    global_var = "I've been modified!"

modify_global()
print(global_var)  # Output: "I've been modified!"

# 8. Mutable vs Immutable Variables
# Mutable variables can be changed after creation, while immutable variables cannot.

# Immutable types: int, float, str, tuple
x = 10
x = 20  # This creates a new integer object rather than modifying the original

# Mutable types: list, dict, set
my_list = [1, 2, 3]
my_list[0] = 10  # The original list is modified

# 9. Constants in Python
# Python does not have built-in support for constants, but you can follow naming conventions to indicate that
# a variable should not change. Typically, constants are written in uppercase.

PI = 3.14159  # Use uppercase letters to indicate constants

# You can use third-party libraries like `const` or create custom solutions to implement strict constants.

# 10. Advanced Concepts: Variable Scope

# Python has 4 types of variable scope:
# - Local: Variables defined inside a function
# - Enclosing: Variables in the local scope of enclosing functions (used in nested functions)
# - Global: Variables defined at the top level of the script or program
# - Built-in: Variables that are preassigned in Python (e.g., keywords like True, False)

def outer_function():
    outer_var = "I'm in the outer function!"

    def inner_function():
        inner_var = "I'm in the inner function!"
        print(outer_var)  # The inner function can access variables from the outer function

    inner_function()

outer_function()

# In nested functions, you can use the `nonlocal` keyword to modify variables in the enclosing scope:
def outer():
    outer_var = "Outer"

    def inner():
        nonlocal outer_var
        outer_var = "Modified by inner"

    inner()
    print(outer_var)  # Output: "Modified by inner"

outer()

# 11. The Walrus Operator (Python 3.8+)

# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can make your code shorter and sometimes more readable.

# Example 1: Using the walrus operator in a while loop
# Normally, you'd assign a value and then check the condition in separate steps:
n = 0
while n < 5:
    n += 1
    print(n)

# With the walrus operator, you can combine assignment and the condition check into one step:
n = 0
while (n := n + 1) < 5:  # n is incremented and checked in the same line
    print(n)  # Output: 1, 2, 3, 4

# Example 2: Using the walrus operator in an if statement
# Let's say we want to check the length of a list and use that length in the same if statement.

my_list = [1, 2, 3, 4, 5]

# Without the walrus operator, we'd do it like this:
length = len(my_list)
if length > 3:
    print(f"List is long enough, it has {length} elements.")

# With the walrus operator, we can shorten this:
if (length := len(my_list)) > 3:
    print(f"List is long enough, it has {length} elements.")

# Example 3: Combining walrus operator with list comprehensions
# The walrus operator is also useful in list comprehensions where you might want to reuse a computed value.

# Let's say we want to filter a list of numbers, but we want to use each number's squared value in the condition:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Without walrus operator, you'd have to call the squaring operation twice:
squares = [n**2 for n in numbers if n**2 > 20]

# With the walrus operator, you can compute the square once and reuse it:
squares = [square for n in numbers if (square := n**2) > 20]
print(squares)  # Output: [25, 36, 49, 64]

# Example 4: Using walrus operator in a for loop
# In some cases, the walrus operator helps reduce redundancy in loops.

# Without walrus operator:
data = ["apple", "banana", "cherry", "date"]
for fruit in data:
    if len(fruit) > 5:
        print(f"The fruit '{fruit}' has {len(fruit)} letters.")

# With walrus operator:
for fruit in data:
    if (length := len(fruit)) > 5:
        print(f"The fruit '{fruit}' has {length} letters.")
