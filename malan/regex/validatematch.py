import re

# := walrus operator new to python and ask a boolean question about it
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
