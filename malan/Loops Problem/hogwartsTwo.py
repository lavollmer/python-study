#dict is a associate one value with another - just like a human dictionary
#keys and values (something associated with something than else)
#list is a set of values vs dict is more dynamic

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }

#Hermione is the key and get the value which will print out Gryffindor
# print(students["Hermione"])

# Use a for loop to iterate over the dictionary in python it will show the keys
for student in students:
    print(student, students[student], sep=", ")