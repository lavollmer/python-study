# Want to check valid phone number
# Want to show what country they are calling from

import re

locations = {"+1":"United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    # \+ escaped with backsplash \ (expecting LITERAL character +)
    # \d any kind of number between 0-9
    # \d {1,3} between 1,3 numbers
    # a space after
    # exactly 3 numbers followed by a dash
    # exactly 4 numbers at the end
    # make a capture group by using parentheses () inside a regular expression group
    # ?P<variable> this NAMES the group 
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number= input("Number: ")
    
    # stored number user's phone number
    # searching for match in pattern
    match = re.search(pattern, number)
    if match:
        # use country_code as the KEY for the locations dictionary
        country_code = match.group("country_code")
        # user the key for the value
        print(locations[country_code])
    else:
        print("Invalid")

main()