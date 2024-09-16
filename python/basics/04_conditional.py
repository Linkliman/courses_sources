# 1. What are Conditionals?
# Conditionals allow your program to make decisions based on certain conditions.
# In Python, the main conditional keywords are `if`, `elif`, and `else`.

# Example: Basic `if` statement
x = 10
if x > 5:
    print(f"{x} is greater than 5")  # This will be printed

# Example: `if-else` statement
if x < 5:
    print(f"{x} is less than 5")
else:
    print(f"{x} is greater than or equal to 5")  # This will be printed

# Example: `if-elif-else` statement
if x < 5:
    print(f"{x} is less than 5")
elif x == 10:
    print(f"{x} is exactly 10")  # This will be printed
else:
    print(f"{x} is greater than 5 but not 10")

# 2. Logical Operators in Conditionals
# You can combine multiple conditions using logical operators: `and`, `or`, `not`.

# `and`: Both conditions must be true
age = 20
if age > 18 and age < 30:
    print("You are a young adult.")  # This will be printed

# `or`: At least one condition must be true
if age < 18 or age > 60:
    print("You are either underage or a senior.")
else:
    print("You are in the working age group.")  # This will be printed

# `not`: Negates a condition
if not (age < 18):
    print("You are not a minor.")  # This will be printed

# 3. Nested Conditionals
# You can also nest conditionals inside one another, but be careful to avoid deep nesting.

# Example: Nested conditionals
score = 85
if score >= 50:
    if score >= 80:
        print("Great job!")  # This will be printed
    else:
        print("You passed!")
else:
    print("You failed.")

# 4. Ternary Conditional Operator
# Python supports a shorthand way of writing conditionals using the ternary conditional operator.

# Syntax: `value_if_true if condition else value_if_false`
is_adult = True if age >= 18 else False
print(is_adult)  # Output: True

# 5. Checking Membership in Conditionals
# You can check if a value exists in a list, dictionary, set, or string using the `in` keyword.

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list!")  # This will be printed

# Checking in a string
if "a" in "apple":
    print("'a' is in the word apple.")  # This will be printed

# Checking in a dictionary (checks keys)
person = {"name": "John", "age": 30}
if "name" in person:
    print("The key 'name' exists in the dictionary.")  # This will be printed

# 8. Using `match` Statements (Python 3.10+)
# Python 3.10 introduced the `match` statement for pattern matching, which can simplify complex conditionals.

# Example: Simple `match` statement
status_code = 200

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status code")

# Output: OK

# 9. Best Practices for Conditionals
# - Avoid deep nesting of conditionals by using `return` or `break` early in loops or functions.
# - Prefer `elif` over multiple `if` statements if the conditions are mutually exclusive.
# - Use descriptive variable names for clarity, especially when dealing with complex conditionals.
# - Use the ternary operator (`value_if_true if condition else value_if_false`) for simple conditions.
