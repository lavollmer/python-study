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