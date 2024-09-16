# Warning, this file will not run as it is, it is just a collection of code snippets.

# 1. What is a Module?
# A module in Python is simply a file containing Python code. It may include functions, classes, or variables,
# and you can import it into other Python programs.

# Example: Let's say we have a file called `math_tools.py` with the following content:
# ----------------
# # math_tools.py
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero.")
#     return a / b
# ----------------

# You can import and use this module in another Python script.

# 2. Importing Modules

# There are several ways to import modules in Python.

# Example: Importing the whole module
import math_tools

print(math_tools.add(5, 3))       # Output: 8
print(math_tools.divide(10, 2))   # Output: 5.0

# Example: Importing specific functions from a module
from math_tools import add, multiply

print(add(5, 3))       # Output: 8
print(multiply(4, 2))  # Output: 8

# Example: Importing all functions using *
from math_tools import *

print(subtract(5, 2))  # Output: 3

# 3. Module Aliasing
# You can also assign a shorter alias when importing a module for convenience.

import math_tools as mt

print(mt.add(10, 5))  # Output: 15
print(mt.multiply(3, 3))  # Output: 9

# 4. Built-in Modules
# Python comes with a large number of built-in modules. Some common ones include `os`, `sys`, `math`, `random`, etc.

# Example: Using the `math` module
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

# Example: Using the `random` module
import random

print(random.randint(1, 10))  # Random number between 1 and 10

# 5. Working with Custom Modules
# To create your own module, you just need to create a Python file with the necessary functions and classes,
# and then you can import it into any other Python file.

# Let's say we have another file called `string_tools.py`:
# ----------------
# # string_tools.py
# def to_uppercase(s):
#     return s.upper()
#
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)
# ----------------

# Now, in another file, we can import this module and use its functions.

# Example usage of custom module:
import string_tools

print(string_tools.to_uppercase("hello"))  # Output: HELLO
print(string_tools.count_vowels("hello"))  # Output: 2

# 6. The `__name__` and `__main__` Special Variables

# Every Python module has a special built-in variable `__name__`. If the module is being run directly, `__name__` will be `"__main__"`.
# If the module is being imported into another module, `__name__` will be the name of the module.

# Let's modify `math_tools.py` to include a conditional check:
# ----------------
# # math_tools.py
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# if __name__ == "__main__":
#     print("This is math_tools.py being run directly!")
# ----------------

# If you run `math_tools.py` directly, the message "This is math_tools.py being run directly!" will be printed.
# However, if you import `math_tools` into another script, that message will NOT be printed.

# 7. Packages
# A package in Python is simply a directory containing multiple modules and an optional `__init__.py` file.
# A package allows you to structure your project in a hierarchical way.

# Example structure of a package:
# my_package/
#     __init__.py
#     math_tools.py
#     string_tools.py

# The `__init__.py` file can be empty or contain initialization code for the package.
# You can import specific modules from the package like this:
# import my_package.math_tools

# Or import everything in the package:
# from my_package import math_tools, string_tools

# 8. The `__init__.py` File
# The `__init__.py` file is executed when a package is imported. This file is often used to initialize the package or define
# what modules and symbols will be available when you import the package.

# Example of `__init__.py` content:
# ----------------
# # __init__.py
# from .math_tools import add, subtract
# from .string_tools import to_uppercase
# ----------------

# Now, if you import the package, those functions will be available directly:
# from my_package import add, to_uppercase

# 9. Relative Imports
# If you are working with packages, you can use relative imports to refer to modules within the same package.

# Example:
# In `string_tools.py` (inside a package), you could do:
# from .math_tools import add  # Relative import (from the same package)

# Relative imports use `.` for the current directory and `..` for the parent directory.

# 10. Reloading Modules
# Sometimes when developing, you want to reload a module after making changes without restarting the Python interpreter.
# You can do this using `importlib.reload()`.

import importlib
import math_tools

# Now modify `math_tools.py` and save it, then reload the module:
importlib.reload(math_tools)

# Now the new version of `math_tools` is available in your session.

# 11. Finding a Module’s Path
# If you're curious about where Python is loading a module from, you can check the module's `__file__` attribute.

import math
print(math.__file__)  # Output: Path to the math module on your system

# 12. `sys.path` and the Module Search Path
# Python uses the `sys.path` list to search for modules when you use `import`. This list includes directories like
# the current directory, standard library paths, and other directories specified in the PYTHONPATH environment variable.

import sys
print(sys.path)  # Output: List of directories where Python searches for modules

# You can modify `sys.path` at runtime to include new directories where Python will look for modules:
sys.path.append('/path/to/my/modules')