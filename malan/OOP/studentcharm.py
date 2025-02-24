# property has a bunch of defense mechanisms
# to prevent programmers from messing up functions
# decorators functions that modify other functions
# need function and variable to haver different names - add a little underscore
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        # instance variable
        self.name = name
        # going to call setter method
        self._house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    # function for a class that gets a value
    @property
    def house(self):
        return self._house

    # Setter
    # function for a class that sets a value
    # name it the getter function plus .setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Student has been created
    return Student(name, house)


if __name__ == "__main__":
    main()

# https://docs.python.org/3/tutorial/classes.html
