import re

url = input("URL: ").strip()

# searching the user's input url
# extracting/capturing the user's username with the (.+)
# if a match then print out username
# (www\.) is the first group
# (?:...) non-capturing version, yes using parenthese to group but DO NOT NEED TO CAPTURE
if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
    
# re.split use multiple characters
# re.findall 