email = input("What's your email?").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")