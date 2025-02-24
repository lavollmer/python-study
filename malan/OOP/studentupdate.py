# anytime you are using a class - you are creating Objects
# classes are mutable but can make them immutable
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # passing arguments to the classes, will provide the ability to error check
    student = Student(name, house)
    return student

if __name__=="__main__":
    main()
    
# classes = a blueprint for pieces of data
# class is a mold that gives you type of data that what you want
# create your own objects primary function