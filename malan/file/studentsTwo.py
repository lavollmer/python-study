students = []

# open file to read
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

# already using double quotes in f string - need to use single quotes to differentiate
# python allows to pass functions inside other arguments
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
