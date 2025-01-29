name = input("What is your name? ")

# Check if the name is Harry, Ron, or Hermione
# _ is a wildcard that matches anything
# | is the OR operator
match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor!")
    case _:
        print("Hello, stranger!")