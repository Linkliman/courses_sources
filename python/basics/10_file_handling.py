# 1. What is File Handling?
# File handling is the process of opening, reading, writing, and closing files in Python.
# Python provides built-in functions for file handling, such as `open()`, `read()`, `write()`, and `close()`.

# 2. Opening a File
# To open a file, use the `open()` function. It takes two main arguments: the file name and the mode.
# Modes:
# - 'r': Read (default)
# - 'w': Write (overwrites if file exists)
# - 'a': Append (writes at the end of the file)
# - 'x': Create (fails if file exists)

# Example: Opening a file in read mode
file = open("example.txt", "r")
print(file.name)  # Output: example.txt

# 3. Reading from a File
# Once a file is open, you can use the `read()` or `readline()` functions to read its contents.

# Example: Reading the entire file using `read()`
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Prints the entire content of the file

# Example: Reading line by line using `readline()`
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # Removes newline character
        line = file.readline()

# Example: Reading all lines as a list using `readlines()`
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Output: List of all lines in the file

# 4. Writing to a File
# You can write to a file using the `write()` or `writelines()` functions. The mode must be 'w' (write) or 'a' (append).

# Example: Writing to a file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling tutorial.\n")

# Example: Appending to a file (adds content to the end of the file)
with open("output.txt", "a") as file:
    file.write("Appending more text.\n")

# 5. File Modes
# - 'r': Read (file must exist)
# - 'w': Write (overwrites the file, creates a new file if it doesn’t exist)
# - 'a': Append (adds to the file, creates a new file if it doesn’t exist)
# - 'x': Create (creates a new file, fails if file exists)
# - 'b': Binary mode (for non-text files like images or executables)
# - 't': Text mode (default for reading and writing text files)

# Example: Reading a file in binary mode
with open("image.jpg", "rb") as file:
    data = file.read()
    print(f"Read {len(data)} bytes from the image.")

# Example: Writing a file in binary mode
with open("new_image.jpg", "wb") as file:
    file.write(data)

# 6. Closing a File
# It's important to close a file when you're done with it to free up system resources.
# Using `with` automatically closes the file after the block is executed.

# Example: Manually closing a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # Make sure to close the file

# 7. Context Managers (`with` Statement)
# The `with` statement is the preferred way to work with files, as it automatically closes the file when the block is done.

# Example: Using `with` to open a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File will be closed automatically after this block

# 8. Handling File Exceptions
# File operations may raise exceptions (e.g., `FileNotFoundError` if the file doesn't exist).
# You can handle these exceptions using `try`, `except`.

# Example: Handling file not found error
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Please check the file name.")

# Example: Handling permission errors
try:
    with open("readonly_file.txt", "w") as file:
        file.write("Trying to write to a read-only file.")
except PermissionError:
    print("Permission denied! Cannot write to this file.")

# 9. Working with File Paths
# Python’s `os` and `pathlib` modules are useful for working with file paths.

# Example: Checking if a file exists using `os.path`
import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# Example: Creating a new directory
os.mkdir("new_directory")

# Example: Deleting a file
if os.path.exists("output.txt"):
    os.remove("output.txt")

# Example: Using `pathlib` for file paths (introduced in Python 3.4)
from pathlib import Path

# Define a file path
file_path = Path("example.txt")

if file_path.exists():
    print(f"File {file_path} exists.")
else:
    print(f"File {file_path} does not exist.")

# Example: Creating a new directory using `pathlib`
new_dir = Path("new_folder")
new_dir.mkdir(exist_ok=True)  # Create the directory, avoid error if it exists

# 10. Best Practices for File Handling
# - Always use the `with` statement when working with files to ensure they are closed properly.
# - Handle exceptions, especially `FileNotFoundError` and `PermissionError`.
# - Use the appropriate file mode ('r', 'w', 'a', etc.) based on the operation you're performing.
# - Use `os` and `pathlib` to work with file paths and directories in a cross-platform way.
