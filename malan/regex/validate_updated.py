email = input("What's your email?").strip()

username, domain = email.split("@")

# truthy value for one character for username
# if username AND . in domain = TWO boolean expressions
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")