# Python Variables

Variables are created when you assign a value to it. Python has no command for declaring a variable.

Examples:
x = 5
y = "Hello world!"

Python commenting starts with a #.
Comments can be places at the end of a line and python will ignore the rest of the line. Python does not have syntax for multiline code.

Python has no command for declaring variables. A variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type, even change type if they have been set.

Strings can be declared either single or double quotes.

Variables are case-sensitive.

## Casting

If you want to specify the data type of a variable, this can be done with casting.

Example:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

## Get the Type

You can get the data type of a variable with the type() function.

# Global Variables

Variables the are created outside of a function are known as global variables.

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 

To create a global variable inside a function use the global keyword.Also, use the global keyword if you want to change a global variable inside a function.

Example:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)