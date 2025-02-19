# hexidecimal color code #0076BA

# Rules for pattern with hexidecimal color codes
# Begins with a #
# Composed of 6 characters - 0-9 and A-F

import re

def main():
    code = input("Hexadecimal color code: ")

    # r means create a raw string - i.e. backsplash chara won't be interpreted as backsplash with raw
    # [] is called a character set, A-Z is considered a RANGE
    # after finding hash symbol then should find the characters
    # quantifiers - access with curly braces (ensures exactly of 6 characters)
    # anchor - using a carrot at beginning and $ at the end
    # $ last character should be the six characters
    pattern = r"^#[0-9A-Fa-f]{6}$"
    # search the pattern in the code string which returns a match object
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print(f"Invalid.")
    
main()