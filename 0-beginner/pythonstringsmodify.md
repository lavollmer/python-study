# Python String Modify

### Upper Case

The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

### Lower Case

The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

### Remove whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

### Replace String

The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

### Split String

The split() method returns a list where the text between the specified separator becomes the list items.

The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

## String Concatenation

To concatenate, or combine, two strings you can use the + operator.

Example, Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

Example, To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

## Format Strings
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

## F-Strings

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36
txt = f"My name is John, I am {age}"
print(txt)

## Placeholders and Modifiers

A placeholder can contain variables, operations, functions, and modifiers to format the value.

Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)