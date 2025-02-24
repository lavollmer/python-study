# anytime you are using a class - you are creating Objects
# classes are mutable but can make them immutable
class Student:
    # instance methods
    # designed the authors of python
    # we are adding instance variables to objects
    # blueprint always going to have a name and house but we can determine what it looks like
    # init takes self gives to the current object that is created
    def __init__(self, name, house):
        # instance variable
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # classes come with methods(certain functions to determine behavior in a standard way)
    # passing arguments to the classes, will provide the ability to error check
    # constructor call - instantiate a student object for me
    student = Student(name, house)
    return student

if __name__=="__main__":
    main()
    
# classes = a blueprint for pieces of data
# class is a mold that gives you type of data that what you want
# create your own objects primary function