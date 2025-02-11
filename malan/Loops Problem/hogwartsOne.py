students = ["Hermione", "Harry", "Ron"]

#print can take 2 arguments that are separated by a space
#len is length in python
# take the length of the list (which is a number), then return that integer value to range which will give be the range of numbers
# Way a for loop works - creates a variable and assigns the variable to the first item in the list, then automatically assigns i to the second thing in the list and does the code below
for i in range(len(students)):
    print(i + 1, students[i])