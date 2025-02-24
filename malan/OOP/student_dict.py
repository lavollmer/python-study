def main():
    # can return a tuple as a one variable
    # can index into a tuple and is immutable
    # no constraints on types of things in tuples
    # immutable index into it numerically
    # dictionary of keys and values
    student = get_student()
    if student["name"] == "Padma":
        student["student"] = "Ravenclaw"
    # f string can't use double quotes inside double quotes
    print(f"{student['name']} from {student['house']}")
    
def get_student():
    # returning two key value pairs - returning a dictionary
    # name is name and house is house in a dictionary
    # empty dictionis two curly brackets
    student = {}
    # name is a key
    name = input("Name: ")
    # house is the key
    house = input("House: ")
    return {"name": name, "house": house}

if __name__=="__main__":
    main()