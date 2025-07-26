age = input("Please enter your age: ")
if not age.isdigit():
    print("Invalid input. Please enter a number")
else:
    age = int(age)
    if age < 0 or age > 120:
        print("Out of range. Please enter a valid age between 0 and 120.")
    else:
        print(f"You entered a valid age: {age}")