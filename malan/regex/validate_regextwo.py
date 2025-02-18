import re

email = input("What's your email? ").strip()

# re.search(pattern,string), can take a bunch of special symbols
# . any character except a newline
# * 0 or more reptitions
# + 1 or more reptitions
# ? 0 or 1 repetition
# {m} m reptitions
# {m,n} m-n reptitions

# start state from left to right, stay in first state or transition to next state
# did it end up in a final state
# if we get stuck in the invalid state then invalid
# escape character for a newline = backsplash to match on a dot 
# r means to treat raw string (similiar to f string)
# ^ match the start of string
# $ matches the end of the string just before the newline at the end
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("invalid")
    

# [] inside of pattern and include set of characters
# [^] complementing the set - you CANNOT match any of these characters