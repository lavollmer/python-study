def main():
    # can return a tuple as a one variable
    # can index into a tuple and is immutable
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # tuple - when using commma returning one value of a tuple with two values
    return (name, house)

if __name__=="__main__":
    main()