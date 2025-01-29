def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

# function with argument number - return boolean values
# if number is even, return True
# if number is odd, return False
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()