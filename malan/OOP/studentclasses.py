# keep all the related code togethed
# raise exceptions - creating your own exceptions to alert the programmer there is an error
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        # instance variable
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Student has been created
    return Student(name, house)


if __name__=="__main__":
    main()
