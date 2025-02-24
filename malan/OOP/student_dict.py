def main():
    student = get_student()
    if student["name"] == "Padma":
        student["student"] = "Ravenclaw"
    # f string can't use double quotes inside double quotes
    print(f"{student['name']} from {student['house']}")
    
def get_student():
    # returning two key value pairs - returning a dictionary
    # name is name and house is house in a dictionary
    # name is a key
    name = input("Name: ")
    # house is the key
    house = input("House: ")
    return {"name": name, "house": house}

if __name__=="__main__":
    main()