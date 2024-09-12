# 1. What are Functions?
# Functions in Python are reusable blocks of code that perform a specific task.
# You define a function using the `def` keyword, followed by the function name, parentheses, and a colon.

# Example: Defining and calling a function
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# 2. Function Arguments
# Functions can take arguments, which allow them to work with different inputs.
# Arguments are defined in the parentheses of the function definition.

# Example: Function with a single argument
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!

# Example: Function with multiple arguments
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# 3. Default Arguments
# You can assign default values to function arguments. If an argument is not provided during the function call,
# the default value will be used.

# Example: Function with default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Output: Hello, Guest!
greet("Charlie")  # Output: Hello, Charlie!

# 4. Keyword Arguments
# When calling a function, you can use keyword arguments to specify the values for each argument by name.

# Example: Using keyword arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(name="Alice", age=30, city="New York")  
# Output: Alice is 30 years old and lives in New York.

# You can also mix positional and keyword arguments.
describe_person("Bob", city="Los Angeles", age=25)  
# Output: Bob is 25 years old and lives in Los Angeles.

# 5. *args and **kwargs
# `*args` allows you to pass a variable number of positional arguments to a function.
# `**kwargs` allows you to pass a variable number of keyword arguments.

# Example: Using *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5, 10))       # Output: 15

# Example: Using **kwargs
def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# 6. Return Statement
# Functions can return values using the `return` keyword.
# Once a `return` statement is reached, the function stops and returns the specified value.

# Example: Function with return statement
def square(x):
    return x ** 2

result = square(4)
print(result)  # Output: 16

# You can return multiple values from a function as a tuple:
def get_person():
    name = "Alice"
    age = 30
    return name, age

person_name, person_age = get_person()
print(person_name)  # Output: Alice
print(person_age)   # Output: 30

# 7. Function Scope
# Variables defined inside a function have local scope, meaning they are only accessible within that function.
# Global variables can be accessed anywhere in the code, but be careful when modifying global variables inside functions.

# Example: Local and global variables
x = 10  # Global variable

def modify_var():
    x = 5  # Local variable (does not modify the global x)
    print(f"Inside function: x = {x}")

modify_var()  # Output: Inside function: x = 5
print(f"Outside function: x = {x}")  # Output: Outside function: x = 10

# To modify a global variable inside a function, use the `global` keyword.
def modify_global_var():
    global x
    x = 20

modify_global_var()
print(f"After modifying: x = {x}")  # Output: After modifying: x = 20

# 8. Lambda Functions
# Lambda functions are small, anonymous functions defined using the `lambda` keyword.
# They are typically used for short, simple operations.

# Syntax: `lambda arguments: expression`
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Example: Lambda function with multiple arguments
multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12

# Lambda functions are often used with functions like `map()`, `filter()`, and `sorted()`.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 9. Recursive Functions
# A recursive function is a function that calls itself to solve smaller instances of the same problem.
# Be careful with recursion as it requires a base case to stop, otherwise it will result in infinite recursion.

# Example: Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Example: Recursive function for Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n  # Base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

# 10. Decorators (Advanced Topic)
# Decorators are a powerful feature that allows you to modify or extend the behavior of a function.
# A decorator is a function that takes another function as an argument, adds some functionality, and returns a new function.

# Example: Simple decorator that logs when a function is called
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator  # Applying the decorator to a function
def add(a, b):
    return a + b

add(3, 5)
# Output:
# Calling add
# add returned 8

# You can apply decorators to any function to add functionality such as logging, timing, authentication, etc.
# Decorators will be detailed in the advanced parts of the tutorial