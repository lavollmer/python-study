# goal extract username only

url = input("URL: ").strip()

# if url is a string comes with method replace - pass two arguments
username = url.replace("https://twitter.com/","")
print(f"{username}")


# what if user said http
# what if had slash at end of username
# what is no https
# what if user uses www