# goal extract username only
import re

url = input("URL: ").strip()

# if url is a string comes with method removeprefix
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")


# what if user said http
# what if had slash at end of username
# what is no https
# what if user uses www (subdomain)
# user experience - tolerant of all users input that are valid

# re.sub is substituting
# pattern
# repl what do you want to replace it with
# string what you want to replace
# find and replace with regular expressions(regex)
# need backsplash before . to escape it
# ? means 0 or 1 the character before
# need parentheses to group
# take these incremental steps - make sure it works, add it together
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)

print(f"Username: {username}")