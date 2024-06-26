#0x08. Python - More Classes and Objects
## Learning Objectives
### General
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special `__str__` and `__repr__` methods and how to use them
- What is the difference between `__str__` and `__repr__`
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain `__dict__` of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3 (version 3.8.5)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks
**Task 0: Write an empty class `Rectangle` that defines a rectangle**
>`0-rectangle.py`
```
You are not allowed to import any module
```
**Task 1 : Write a class `Rectangle` that defines a rectangle based on `0-rectangle.py`**
```
1. Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
     - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
2. Private instance attribute: `height:`
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
     -`height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
3. Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
4. You are not allowed to import any module
```
