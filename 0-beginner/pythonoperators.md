# Python Operators

Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:
print(10 + 5)

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators


Operator, Example, Same As
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)

PYTHON OPERATORS
Operator	Name	Example
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y

PYTHON LOGICAL OPERATORS
Operator	Description	
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true

Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first: print((6 + 3) - (6 + 3))

Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions: print(100 + 5 * 3)

## Precedence of Operators

() Parentheses
** Exponentiation
* / // % Multiplication, division, floor division, modulus
+ - Addition and subtraction
== != > >= < <= Comparisons, identity and membership operators

NOTE: Addition + and subtraction - has the same precedence

## Python Lists
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

### List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

Lists are used to store multiple items in a single variable.

Ordered lists means that items have a defined order and the order will not change.

Changeable list means that we can change, add and remove items in a list after it has been created.

Since lists are indexed, they can have items with the same value.

Determine list length use len().

List items can be any data type.

List items are indexed and you can access by referring to the index number.

Negative indexing 
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

### List Constructor

Example
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

### Change List Items

To change the value of a specific item refer to the index number.

Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

Note:  The length of the list will change when the number of items inserted does not match the number of items replaced.

Example
Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

### Insert Python
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

### Add List Items
Add an item to the end of list, use the append()

Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

### Add one list to another list

To append elements from another list to current list, use the extend()

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

### Remove Specified Items

The remove() method removes the specified item.

Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

If you do not specify the index, the pop() method removes the last item.

The del keyword also removes the specified index:
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

## Loop Lists

You can loop through the list items by using a for loop:
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

Loop through list items by referring to their index number - use range() and len() functions

Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

## While Loop

Loop through the list items by using a while loop.

Use the len() function to determine the length of the list. Start a 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.

Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


List Comprehension
A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

## List Comprehension

