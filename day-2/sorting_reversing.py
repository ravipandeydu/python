# Given list of employees from the image
employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales"),
    ("Eve", 70000, "Marketing") # Added an extra employee for better demonstration
]

print("--- Original Employees List ---")
for emp in employees:
    print(emp)

# Task 1: Sort by Salary (Ascending and Descending)
print("\n--- Task 1: Sort by Salary (Ascending) using sorted() ---")
# sorted() creates a new list, original 'employees' remains unchanged
employees_by_salary_asc = sorted(employees, key=lambda emp: emp[1])
for emp in employees_by_salary_asc:
    print(emp)

print("\n--- Task 1: Sort by Salary (Descending) using sorted() ---")
employees_by_salary_desc = sorted(employees, key=lambda emp: emp[1], reverse=True)
for emp in employees_by_salary_desc:
    print(emp)

# Task 2: Sort by Department, Then by Salary
print("\n--- Task 2: Sort by Department, Then by Salary using sorted() ---")
# Sorts by department (index 2) first, then by salary (index 1)
employees_by_dept_salary = sorted(employees, key=lambda emp: (emp[2], emp[1]))
for emp in employees_by_dept_salary:
    print(emp)

# Task 3: Create a Reversed List (without modifying the original)
print("\n--- Task 3: Create a Reversed List using reversed() and list() ---")
# reversed() returns an iterator, list() converts it to a new list
reversed_employees = list(reversed(employees))
for emp in reversed_employees:
    print(emp)
print("\nOriginal employees list after reversed() (should be unchanged):")
for emp in employees:
    print(emp)

# Task 4: Sort by Name Length
print("\n--- Task 4: Sort by Name Length using sorted() ---")
employees_by_name_length = sorted(employees, key=lambda emp: len(emp[0]))
for emp in employees_by_name_length:
    print(emp)

# Task 5: Use sorted() vs .sort() Appropriately
print("\n--- Task 5: Demonstrating .sort() (modifies original list) ---")
# Create a copy to show modification, as original 'employees' was used for sorted() examples
employees_for_sort = [
    ("Charlie", 60000, "HR"),
    ("Diana", 50000, "Finance"),
    ("Frank", 75000, "IT")
]
print("List before .sort():")
for emp in employees_for_sort:
    print(emp)

employees_for_sort.sort(key=lambda emp: emp[1]) # .sort() modifies the list in place
print("\nList after .sort() (sorted by salary ascending):")
for emp in employees_for_sort:
    print(emp)

print("\n--- Summary of sorted() vs .sort() ---")
print("`sorted(iterable, key=..., reverse=...)`:")
print("- Returns a new sorted list.")
print("- Does NOT modify the original iterable.")
print("- Useful when you need to preserve the original order or chain operations.")

print("\n`list.sort(key=..., reverse=...)`:")
print("- Sorts the list IN PLACE.")
print("- Returns `None`.")
print("- Modifies the original list directly.")
print("- Useful when you no longer need the unsorted version of the list and want to save memory.")
