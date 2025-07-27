# Given nested dictionary representing school data
school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    },
    "History": {
        "teacher": "Dr. Lee",
        "students": [("Grace", 90), ("Henry", 85), ("Ivy", 91)]
    }
}

print("--- Initial School Data ---")
import json
print(json.dumps(school, indent=2))

# Task 1: Print Teacher Names
print("\n--- Task 1: Teacher Names ---")
for class_name, class_data in school.items():
    teacher_name = class_data["teacher"]
    print(f"Class: {class_name}, Teacher: {teacher_name}")

# Task 2: Calculate Class Average Grades
print("\n--- Task 2: Class Average Grades ---")
for class_name, class_data in school.items():
    grades = []
    for student_name, grade in class_data["students"]: # Unpacking student tuple
        grades.append(grade)

    if grades:
        average_grade = sum(grades) / len(grades)
        print(f"Class: {class_name}, Average Grade: {average_grade:.2f}")
    else:
        print(f"Class: {class_name}, No students to calculate average.")

# Task 3: Find Top Student Across All Classes
print("\n--- Task 3: Top Student Across All Classes ---")
top_student_name = None
highest_grade_overall = -1

for class_name, class_data in school.items():
    for student_name, grade in class_data["students"]: # Unpacking student tuple
        if grade > highest_grade_overall:
            highest_grade_overall = grade
            top_student_name = student_name

if top_student_name:
    print(f"Student with the highest grade across all classes: {top_student_name} (Grade: {highest_grade_overall})")
else:
    print("No students found in the school data.")

# Task 4: Use Unpacking (demonstrated throughout the tasks)
print("\n--- Task 4: Demonstration of Unpacking ---")
print("Tuple unpacking has been used in Task 2 and Task 3 when iterating through student lists:")
print("Example: `for student_name, grade in class_data[\"students\"]:`")
print("This allows direct access to `student_name` and `grade` without needing to use `student[0]` or `student[1]`.")
