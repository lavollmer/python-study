score = int(input("Enter score: "))

# if score >= 90 and score <= 100:
#     print("A")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 70 and score < 80:
#     print("C")
# elif score >=60 and score < 70:
#     print("D")
# else:
#     print("F")

# minor optimization => else if statements
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")