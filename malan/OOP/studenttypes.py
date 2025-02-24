class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

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
    return Student(name, house)


if __name__ == "__main__":
    main()


# examples of classes
# int => int is a class int(x, base = 10), will return an object of type int
# str => str are classes, class str(object='')
# str.lower() => object type str
# str.strip([chars]) => came with the authors of python
