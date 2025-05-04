marks = []
count = 1
while count <= 10:
    mark = int(input(f"Enter marks of student No. {count}: "))
    count += 1
    marks.append(mark)
print(marks)

maximum = max(marks)
minimum = min(marks)
average = sum(marks)/10

print("The Maximum mark is:", maximum)
print("The Minimum marks is:", minimum)
print("The Average number of marks", average)
