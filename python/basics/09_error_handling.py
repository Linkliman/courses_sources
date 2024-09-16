# 1. What is Error Handling?
# Error handling in Python is the process of responding to runtime errors or exceptions that occur during program execution.
# Python provides a robust mechanism to handle exceptions using the `try`, `except`, `else`, and `finally` blocks.

# 2. The `try` and `except` Blocks
# The `try` block lets you test a block of code for exceptions, and the `except` block allows you to handle the error.

# Example:
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")

# Output: You cannot divide by zero!

# Example: Catching a general exception
try:
    num = int("invalid number")  # This will raise a ValueError
except Exception as e:
    print(f"An error occurred: {e}")

# Output: An error occurred: invalid literal for int() with base 10: 'invalid number'

# 3. Catching Specific Exceptions
# You can catch specific types of exceptions, such as `ValueError`, `TypeError`, `KeyError`, etc., by specifying them in the `except` block.

# Example:
try:
    num = int("text")  # This will raise a ValueError
except ValueError:
    print("A ValueError occurred! Please input a valid number.")

# Output: A ValueError occurred! Please input a valid number.

# 4. Multiple `except` Blocks
# You can handle different exceptions with separate `except` blocks.

# Example:
try:
    # Uncomment one of the following lines at a time to trigger different exceptions
    # result = 10 / 0  # ZeroDivisionError
    # num = int("text")  # ValueError
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid value!")
except IndexError:
    print("List index out of range!")

# Output: List index out of range!

# 5. The `else` Block
# The `else` block will run if no exceptions are raised in the `try` block. It's useful for code that should only run if the `try` block succeeds.

# Example:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful! The result is:", result)

# Output: Division successful! The result is: 5.0

# 6. The `finally` Block
# The `finally` block always executes, whether an exception occurs or not. It is typically used for cleaning up resources (e.g., closing files).

# Example:
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleaning up resources...")  # This will always run

# Output:
# File not found!
# Cleaning up resources...

# 7. Raising Exceptions
# You can raise exceptions in your code using the `raise` keyword.

# Example:
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")  # Manually raise an exception
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)

# Output: Cannot divide by zero!

# 8. Custom Exceptions
# You can define your own exception classes by subclassing Python's built-in `Exception` class.

# Example:
class NegativeNumberError(Exception):
    pass  # Custom exception doesn't need special code, just a class

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot take the square root of a negative number.")
    return number ** 0.5

try:
    result = square_root(-4)
except NegativeNumberError as e:
    print(e)

# Output: Cannot take the square root of a negative number.

# 9. Using `try`, `except`, `else`, and `finally` Together
# You can use all these blocks together to handle exceptions and ensure code is always cleaned up.

# Example:
def open_file(file_name):
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    else:
        print(f"File {file_name} opened successfully.")
        file.close()
    finally:
        print("Execution complete.")

open_file("example.txt")

# Output:
# File example.txt not found.
# Execution complete.

# 10. Best Practices for Error Handling
# 1. Be specific with your `except` blocks: Only catch the exceptions you expect, and avoid using a general `except Exception` unless necessary.
# 2. Use custom exceptions when needed: Create meaningful exceptions for your application logic.
# 3. Always clean up resources: Use the `finally` block for cleanup actions like closing files or releasing network connections.
# 4. Avoid bare `except` blocks: Always specify the exception type or include `except Exception` with care to avoid catching unrelated errors.
# 5. Log exceptions: When dealing with larger projects, logging errors (e.g., using the `logging` module) is better than printing to the console.
