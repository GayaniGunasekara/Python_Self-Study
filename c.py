count = 0
while count < 5:
    mark = int(input("Enter the Mark:"))
    if mark > 75:
        grade = "A"
    elif mark >= 65:
        grade = "B"
    elif mark >= 55:
        grade = "C"
    elif mark >= 45:
        grade = "S"
    else:
        grade = "F"
    print("The grade for the subject is:", grade)
    count += 1
