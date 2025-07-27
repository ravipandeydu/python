# Initial lists from the image
students = ["Alice", "Bob", "Carol", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

# Task 1: Create a Numbered List of Students
print("--- Task 1: Numbered List of Students ---")
for i, student in enumerate(students):
    print(f"{i + 1}. {student}")

# Task 2: Pair Students with Their Scores Using enumerate()
print("\n--- Task 2: Students with Their Scores ---")
for i, student in enumerate(students):
    print(f"{student}: {scores[i]}")

# Task 3: Find Positions of High Scorers
print("\n--- Task 3: Positions of High Scorers (above 90) ---")
high_scorer_positions = []
for i, score in enumerate(scores):
    if score > 90:
        high_scorer_positions.append(i)

if high_scorer_positions:
    print("Positions of students who scored above 90:")
    for pos in high_scorer_positions:
        print(f"- Index: {pos} (Student: {students[pos]})")
else:
    print("No students scored above 90.")

# Task 4: Map Positions to Student Names
print("\n--- Task 4: Map Positions to Student Names ---")
position_to_student = {}
for i, student in enumerate(students):
    position_to_student[i] = student

print("Dictionary of positions to student names:")
print(position_to_student)