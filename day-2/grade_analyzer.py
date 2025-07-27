grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

print("--- Initial Grades ---")
print(grades)

# Task 1: Slice grades from index 2 to 7
print("\n--- Task 1: Sliced Grades (index 2 to 7) ---")
sliced_grades = grades[2:8] # Slice includes start index, excludes end index
print(sliced_grades)

# Task 2: Use list comprehension to find grades above 85
print("\n--- Task 2: Grades Above 85 (using list comprehension) ---")
grades_above_85 = [grade for grade in grades if grade > 85]
print(grades_above_85)

# Task 3: Replace the grade at index 3 with 95
print("\n--- Task 3: Replace grade at index 3 with 95 ---")
grades[3] = 95
print(grades)

# Task 4: Append three new grades (e.g., 93, 80, 70)
print("\n--- Task 4: Append three new grades (93, 80, 70) ---")
grades.append(93)
grades.append(80)
grades.append(70)
print(grades)

# Task 5: Sort in descending order and display the top 5 grades
print("\n--- Task 5: Top 5 Grades (sorted descending) ---")
grades.sort(reverse=True) # Sort in descending order
top_5_grades = grades[:5] # Get the first 5 elements after sorting
print(top_5_grades)