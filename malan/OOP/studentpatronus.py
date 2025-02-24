# anytime you are using a class - you are creating Objects
# classes are mutable but can make them immutable
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    # calling a function Student
    # creating an object of a class (object is when you use the blueprint to create an object)
    # object equals instances
    student = Student()
    # putting inside of Class name attribute and house attribute
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__=="__main__":
    main()
    
# classes = a blueprint for pieces of data
# class is a mold that gives you type of data that what you want
# create your own objects primary function