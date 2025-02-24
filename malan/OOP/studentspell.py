class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return f"{self.name} from {self.house} with {self.patronus}"

    # It's own function in the class
    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse"
            case "Otter":
                return "otter"
            case "Dog":
                return "Dog"
            case _:
                return "Wand"
    
def main():
    student = get_student()
    print("Expector Patronum!")
    print(student.charm())
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__=="__main__":
    main()

# https://docs.python.org/3/tutorial/classes.html