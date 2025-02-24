# keep all the related code togethed
# raise exceptions - creating your own exceptions to alert the programmer there is an error
# __str__ method in class by python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        # instance variable
        self.name = name
        self.house = house
    # only takes self
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Student has been created
    return Student(name, house)


if __name__=="__main__":
    main()

# https://docs.python.org/3/tutorial/classes.html