# Python Object-Oriented Programming (OOP) Tutorial

# 1. What is Object-Oriented Programming?
# OOP is a programming paradigm that organizes code into objects, which represent real-world things and concepts.
# Objects are instances of classes, which define their behavior and properties (attributes and methods).

# 2. Defining a Class
# A class is like a blueprint for creating objects. It defines the attributes (data) and methods (functions) that the object will have.

# Example: Defining a basic class
class Dog:
    # Constructor: The `__init__` method is called when an object is created (instantiated).
    def __init__(self, name, breed):
        # Attributes: These are the properties of the object.
        self.name = name  # `self` refers to the instance of the class.
        self.breed = breed

    # Method: A function that belongs to the class.
    def bark(self):
        print(f"{self.name} says woof!")

# Creating (instantiating) objects of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Accessing attributes and calling methods
print(dog1.name)  # Output: Buddy
print(dog2.breed)  # Output: Bulldog
dog1.bark()  # Output: Buddy says woof!
dog2.bark()  # Output: Max says woof!

# 3. Instance vs. Class Variables
# - Instance variables (like `self.name`) are unique to each object.
# - Class variables are shared across all instances of a class.

# Example: Class variable vs instance variable
class Dog:
    species = "Canis lupus familiaris"  # Class variable (shared by all dogs)

    def __init__(self, name, breed):
        self.name = name  # Instance variable (unique to each dog)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.species)  # Output: Canis lupus familiaris (shared)
print(dog2.species)  # Output: Canis lupus familiaris (shared)

# 4. Methods
# - Instance methods: Require a reference to the object instance (`self`).
# - Class methods: Use `@classmethod` decorator and take `cls` as the first parameter (refer to the class itself).
# - Static methods: Use `@staticmethod` decorator and do not take `self` or `cls`.

# Example: Instance, class, and static methods
class Dog:
    species = "Canis lupus familiaris"  # Class variable

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):  # Instance method
        print(f"{self.name} says woof!")

    @classmethod
    def change_species(cls, new_species):  # Class method
        cls.species = new_species

    @staticmethod
    def general_info():  # Static method
        print("Dogs are domestic animals.")

# Calling methods
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy says woof!

# Using class method
Dog.change_species("New Species")
print(dog1.species)  # Output: New Species

# Using static method
Dog.general_info()  # Output: Dogs are domestic animals.

# 5. Inheritance
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

# Example: Parent and child classes
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):  # Override the parent method
        print(f"{self.name} says woof!")

# Cat class inherits from Animal
class Cat(Animal):
    def speak(self):  # Override the parent method
        print(f"{self.name} says meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Output: Buddy says woof!
cat.speak()  # Output: Whiskers says meow!

# 6. Super() Function
# The `super()` function allows you to call a method from the parent class, typically inside the child class.

# Example: Using `super()` to extend functionality
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the parent class method
        print(f"{self.name} says woof!")

dog = Dog("Buddy", "Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.
# Buddy says woof!

# 7. Encapsulation
# Encapsulation is the concept of restricting direct access to some of an object's attributes and methods.
# In Python, "private" attributes are indicated by a single or double underscore, but they are still accessible.

# Example: Encapsulation using private attributes
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute (convention, not enforced)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

# Creating a bank account
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)  # Output: Insufficient funds!
account.withdraw(100)
print(account.get_balance())  # Output: 1400

# Note: You can still access the "protected" attribute (e.g., `account._balance`),
# but it's discouraged by convention to do so directly.

# 8. Polymorphism
# Polymorphism allows methods in different classes to have the same name but perform different tasks.

# Example: Polymorphism with a common method
class Bird:
    def speak(self):
        print("Bird makes a sound.")

class Parrot(Bird):
    def speak(self):
        print("Parrot says hello!")

class Crow(Bird):
    def speak(self):
        print("Crow caws!")

# Create objects of different classes
parrot = Parrot()
crow = Crow()

# Call the same method `speak()` on different objects
parrot.speak()  # Output: Parrot says hello!
crow.speak()    # Output: Crow caws!

# 9. Dunder (Magic) Methods
# Dunder methods (short for "double underscore") are special methods that allow you to define the behavior of
# operators like `+`, `-`, or comparison operators. They also include things like `__init__`, `__str__`, and `__repr__`.

# Example: Overloading the `__str__` method to make an object printable
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog)  # Output: Buddy is a Golden Retriever

# You can also overload arithmetic operators, comparison operators, and more using dunder methods.


# 10. Miscellaneous

# Some more advanced concepts of object-oriented programming will be covered in another part of the tutorial.