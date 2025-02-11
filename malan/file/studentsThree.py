students = []

# open file to read
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lambda function python that is anonymous
# function has no name, don't need name if you have only in one place
# lambda is a anony function then parameter is student, don't use return keyword just code what you want
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
