# All my student specific functionality
# Cleaning up all the code to be better designed
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # call this method without making a student first
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    # get Student class get function
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

