import re

email = input("What's your email?").strip()

# re.search(pattern,string), can take a bunch of special symbols
# . any character except a newline
# * 0 or more reptitions
# + 1 or more reptitions
# ? 0 or 1 repetition
# {m} m reptitions
# {m,n} m-n reptitions
if re.search("@", email):
    print("valid")
else:
    print("invalid")