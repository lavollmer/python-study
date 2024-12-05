# Python Data Types

Variables can store data of different types and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

One is able to get the data type of any object by using type ().

Example:
x = 5
print(type(x))

In Python, the data type is set when you assign a value to a variable

## Python Numbers

There are three numeric types: int, float, complex

Example:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

### Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

### Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.Float can also be scientific numbers with an "e" to indicate the power of 10.

Example of scientific float:
x = 35e3
y = 12E4
z = -87.7e100

### Complex
Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

## Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods.

Example:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

SPECIAL CASE:
You cannot convert complex numbers into another number type.

## Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))

## Python Casting
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is done using constructor functions.
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

Example:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

Int casting always rounds down with decimals.