students = []

# open file to read
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# create a function to be used in a sort function
def get_house(student):
    return student["house"]

# Only passing in the key NOT get_name() - so sorted function can call that get_name fxn
# already using double quotes in f string - need to use single quotes to differentiate
# python allows to pass functions inside other arguments
for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")
