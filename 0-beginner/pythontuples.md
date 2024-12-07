# Python Tuples

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Creating a tuple with one item - To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.Tuples are unchangeable, or immutable as it also is called.

## Tuple Data Type

From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>

## Tuple Constructor

The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

## Accessing an item in a tuple
Use the index number inside square brackets

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

## Add Items to Tuples

Tuples are immutable. Do not have builtin append().

Ways to work around it.

1. Convert it into a list - convert to a list, add items then convert back to a tuple

2.Add tuple to a tuple - allowed to add tuples to tuples

## Removing items in a tuple

You cannot remove items in a tuple. They are unchangeable.

Workarounds include:
1. Convert to a list, remove item and convert back to list
2. Delete the tuple completely
SPECIAL CASE with error
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

