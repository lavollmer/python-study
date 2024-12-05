# Python Variable Names

A variable can have a short name or a more descriptive name. 

Rules for variables:
A variable name must start with a letter or the underscore character

A variable name cannot start with a number

A variable name can only contain alpha-numeric 
characters and underscores (A-z, 0-9, and _ )

Variable names are case-sensitive (age, Age and AGE are three different variables)

A variable name cannot be any of the Python keywords.

Legitimate names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Camel Case - each word except the first starts with capital letter

Pascal Case - Each word starts with a capital letter

Snake Case - Each word is separated by an underscore character

## Assign Multiple Values

Python allows you to assign values to multiple variables in one line.

 You can assign the same value to multiple variables.

 Example:
 x = y = z = "Orange"
print(x)
print(y)
print(z)

## Unpacking a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

## Output Variables

You can use the print() function to output variables. 

You can output multiple variables separated by a comma.

Example:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)