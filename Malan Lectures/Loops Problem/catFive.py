def main():
    number = get_number()
    meow(number)

#break out the loop then return the value
def get_number():
    while True:
        n = int (input("Whats n? "))
        if n > 0:
            break
        return n
    
def meow(n):
    for _ in range (n):
        print("meow")


main()