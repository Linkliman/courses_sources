# 1. What are Dunder (Magic) Methods?
# Dunder (short for "double underscore") or magic methods in Python allow us to define how objects of a class should behave with
# built-in functions, operators, and type conversion. These methods begin and end with double underscores, such as `__init__`, `__add__`, etc.

# 2. Initialization and Representation Methods

# __init__(self, ...)
# Called when a new object is created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# __str__(self)
# Defines the "informal" or user-friendly string representation, used by `print()` and `str()`.
# If this is not defined, `print()` falls back to `__repr__`.

# __repr__(self)
# Defines the "official" string representation, used by `repr()` or when printing in the interactive console.
# It should ideally be a string that can recreate the object when passed to `eval()`.

class Person:
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

# __del__(self)
# Called when an object is about to be destroyed (garbage collection).
class Person:
    def __del__(self):
        print(f"{self.name} is being destroyed.")

# 3. Arithmetic and In-Place Operators

# Arithmetic operators:
# - __add__(self, other) for `+`
# - __sub__(self, other) for `-`
# - __mul__(self, other) for `*`
# - __truediv__(self, other) for `/`
# - __floordiv__(self, other) for `//`
# - __mod__(self, other) for `%`
# - __pow__(self, other) for `**`

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# In-place arithmetic operators:
# - __iadd__(self, other) for `+=`
# - __isub__(self, other) for `-=`
# - __imul__(self, other) for `*=`
# - __itruediv__(self, other) for `/=`
# - __ifloordiv__(self, other) for `//=`
# - __imod__(self, other) for `%=`
# - __ipow__(self, other) for `**=`

# Unary operators:
# - __neg__(self) for unary `-`
# - __pos__(self) for unary `+`
# - __abs__(self) for `abs()`
# - __invert__(self) for bitwise `~`

class Vector:
    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))

v1 = Vector(2, -3)
print(abs(v1))  # Output: Vector(2, 3)

# 4. Comparison Operators

# Comparison operators:
# - __eq__(self, other) for `==`
# - __ne__(self, other) for `!=`
# - __lt__(self, other) for `<`
# - __le__(self, other) for `<=`
# - __gt__(self, other) for `>`
# - __ge__(self, other) for `>=`

class Person:
    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# Example:
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(person1 == person2)  # Output: False
print(person1 < person2)   # Output: False

# 5. Bitwise Operators

# Bitwise operators:
# - __and__(self, other) for `&`
# - __or__(self, other) for `|`
# - __xor__(self, other) for `^`
# - __lshift__(self, other) for `<<`
# - __rshift__(self, other) for `>>`

class BitwiseExample:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return BitwiseExample(self.value & other.value)

    def __or__(self, other):
        return BitwiseExample(self.value | other.value)

    def __str__(self):
        return f"Value: {self.value}"

b1 = BitwiseExample(12)  # 12 in binary: 1100
b2 = BitwiseExample(6)   # 6 in binary: 0110

b3 = b1 & b2
print(b3)  # Output: Value: 4 (binary: 0100)

# 6. Type Conversion Dunder Methods

# These methods allow objects to be converted to other types:
# - __int__(self) for `int()`
# - __float__(self) for `float()`
# - __bool__(self) for `bool()`
# - __str__(self) for `str()`

class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    def __bool__(self):
        return self.temperature > 0

temp = Celsius(37.5)
print(int(temp))    # Output: 37
print(float(temp))  # Output: 37.5
print(bool(temp))   # Output: True

# 7. Attribute Access Dunder Methods

# These methods control how attributes are accessed, set, and deleted:
# - __getattr__(self, name): Called when trying to access a non-existent attribute.
# - __getattribute__(self, name): Called for every attribute access.
# - __setattr__(self, name, value): Called when setting an attribute.
# - __delattr__(self, name): Called when deleting an attribute.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, attr):
        return f"{attr} not found."

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"Deleting {name}")
        super().__delattr__(name)

# Example:
person = Person("Alice", 30)
print(person.height)  # Output: height not found.
person.age = 31  # Output: Setting age to 31
del person.name  # Output: Deleting name

# 8. Callable Objects

# The `__call__(self)` method allows an object to be called as if it were a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
print(double(5))  # Output: 10

# 9. Context Management Dunder Methods

# Context managers are used to manage resources, such as files, with the `with` statement.
# - __enter__(self): Executed at the start of the `with` block.
# - __exit__(self, exc_type, exc_value, traceback): Executed at the end of the `with` block.

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Example:
with ManagedFile('hello.txt') as f:
    f.write('Hello, world!')

# The file will automatically close after the `with` block is exited, even if an exception occurs.

# 10. Length, Indexing, and Slicing

# These methods allow objects to behave like containers (e.g., lists):
# - __len__(self): For `len()`
# - __getitem__(self, index): For indexing (e.g., `obj[index]`)
# - __setitem__(self, index, value): For setting an item
# - __delitem__(self, index): For deleting an item

class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

# Example:
my_list = CustomList([10, 20, 30, 40])
print(len(my_list))  # Output: 4
print(my_list[2])    # Output: 30
my_list[1] = 99
print(my_list[1])    # Output: 99
del my_list[0]
print(my_list[0])    # Output: 99

# 11. Object Copying

# To control object copying behavior, implement these methods:
# - __copy__(self) for `copy.copy()`
# - __deepcopy__(self, memo) for `copy.deepcopy()`

import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __copy__(self):
        return Person(self.name, self.age)

    def __deepcopy__(self, memo):
        return Person(copy.deepcopy(self.name, memo), copy.deepcopy(self.age, memo))

p1 = Person("Alice", 30)
p2 = copy.copy(p1)
p3 = copy.deepcopy(p1)

# 12. Iterator Dunder Methods
# These methods allow an object to be iterable, meaning it can be used in loops.

# __iter__(self): Initializes the iterator and returns the object itself.
# __next__(self): Returns the next item in the iterator, raises StopIteration when finished.

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

counter = Counter(1, 5)
for num in counter:
    print(num)

# 13. Reversed Dunder Method
# __reversed__(self): Defines how the object should behave with the reversed() function.

class Countdown:
    def __init__(self, start):
        self.start = start

    def __reversed__(self):
        return range(self.start, 0, -1)

countdown = Countdown(5)
print(list(reversed(countdown)))

# 14. Hashing and Immutability
# __hash__(self): Returns an integer representing the hash value of the object, used in sets and as dict keys.
# __eq__(self, other): Defines equality comparison, often used with __hash__.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(hash(p1) == hash(p2))  # True

# 15. Async and Await Dunder Methods (Python 3.5+)
# __aiter__(self): Defines asynchronous iteration.
# __anext__(self): Defines the next item in an asynchronous iteration, returns an awaitable.

import asyncio

class AsyncCounter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __aiter__(self):
        self.current = self.low
        return self

    async def __anext__(self):
        if self.current > self.high:
            raise StopAsyncIteration
        self.current += 1
        await asyncio.sleep(0.1)  # Simulate async work
        return self.current - 1

async def main():
    async for number in AsyncCounter(1, 5):
        print(number)

asyncio.run(main())

# 16. Pattern Matching Dunder Methods (Python 3.10+)
# __match_args__: A tuple of field names used in pattern matching.

class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)

match point:
    case Point(1, y):
        print(f"Point with x=1 and y={y}")

# 17. Slot Management
# __slots__: Defines a fixed set of attributes, reducing memory usage.

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)
