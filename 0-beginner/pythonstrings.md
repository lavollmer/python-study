# Python Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

print("Hello")
print('Hello')

You can use quotes inside a string, as long as they don't match the quotes surrounding the string.

## Multiline Strings

You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

Note: in the result, the line breaks are inserted at the same position as in the code.

## Strings are Arrays

strings in Python are arrays of bytes representing unicode characters

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Get the character at position 1. The first character has a position of 0.
a = "Hello, World!"
print(a[1])

Since strings are arrays, we can loop through the characters in a string, with a for loop.

## String Length

To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

## Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

In an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


## Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

## Slicing Strings

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

What is happening here " b = "Hello, World!"  print(b[2:5])"→Slicing strings, Get the characters from position 2 to position 5 (not included)

Note: The first character has index 0.

### Slice from the Start

By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

### Slice to the End

