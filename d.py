# Initialize sum
total = 0

print("Enter numbers one by one. Enter -999 to stop.")

while True:
    try:
        num = int(input("Enter a number: "))
        if num == -999:
            break
        total += num
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"\nThe sum of the entered numbers is: {total}")
