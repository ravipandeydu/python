# Initial student records from the image
students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]

print("--- Initial Student Records ---")
for student in students:
    print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Age: {student[3]}")

# Task 1: Find the Student with the Highest Grade
print("\n--- Task 1: Find the Student with the Highest Grade ---")
highest_grade = -1
highest_grade_student = None

for student in students:
    if student[2] > highest_grade:
        highest_grade = student[2]
        highest_grade_student = student

if highest_grade_student:
    print(f"Student with the highest grade:")
    print(f"ID: {highest_grade_student[0]}, Name: {highest_grade_student[1]}, Grade: {highest_grade_student[2]}, Age: {highest_grade_student[3]}")
else:
    print("No students found in the list.")

# Task 2: Create a Name-Grade List
print("\n--- Task 2: Create a Name-Grade List ---")
name_grade_list = []
for student in students:
    name_grade_list.append((student[1], student[2]))

print("Name-Grade List:")
print(name_grade_list)

# Task 3: Demonstrate Tuple Immutability
print("\n--- Task 3: Demonstrate Tuple Immutability ---")
print("Attempting to change the grade of a student in the original list...")
try:
    # Attempt to change Alice's grade (index 0, grade is at index 2 within the tuple)
    students[0][2] = 90
except TypeError as e:
    print(f"Error: {e}")
    print("Explanation: Tuples are immutable, which means once they are created, their elements cannot be changed, added, or removed. The error 'tuple object does not support item assignment' confirms this.")

print("\nWhy tuples are preferred for immutable records like student data:")
print("- Data Integrity: Once a record is created, you can be sure that its values (like student ID, name, or birth date) won't be accidentally changed later in the program.")
print("- Performance: Tuples are generally faster than lists for iteration and access, as their size is fixed.")
print("- Use as Dictionary Keys: Because tuples are immutable, they can be used as keys in dictionaries, which is not possible with lists.")
print("- Security and Reliability: For data that should not be altered, tuples provide a level of data integrity and make your code more robust by preventing unintended modifications.")