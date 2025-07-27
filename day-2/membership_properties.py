# Given data structures from the image
fruits_list = ["apple", "banana", "orange", "apple", "grape"]
fruits_tuple = ("apple", "banana", "orange")
fruits_set = {"apple", "banana", "orange", "grape"}
fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}

print("--- Initial Data Structures ---")
print(f"List: {fruits_list}")
print(f"Tuple: {fruits_tuple}")
print(f"Set: {fruits_set}")
print(f"Dictionary: {fruits_dict}")

# Task 1: Check for Membership
print("\n--- Task 1: Check for Membership ('apple') ---")
item_to_check = "apple"

print(f"Is '{item_to_check}' in fruits_list? {'Yes' if item_to_check in fruits_list else 'No'}")
print(f"Is '{item_to_check}' in fruits_tuple? {'Yes' if item_to_check in fruits_tuple else 'No'}")
print(f"Is '{item_to_check}' in fruits_set? {'Yes' if item_to_check in fruits_set else 'No'}")
print(f"Is '{item_to_check}' in fruits_dict? {'Yes' if item_to_check in fruits_dict else 'No'} (checks keys)")

# Task 2: Find Length
print("\n--- Task 2: Find Length ---")
print(f"Length of fruits_list: {len(fruits_list)}")
print(f"Length of fruits_tuple: {len(fruits_tuple)}")
print(f"Length of fruits_set: {len(fruits_set)}")
print(f"Length of fruits_dict: {len(fruits_dict)}") # Returns number of key-value pairs

# Task 3: Iterate and Print Elements / Task 5: Demonstrate Different Iteration Patterns
print("\n--- Task 3 & 5: Iterate and Print Elements with Different Patterns ---")

print("\nIterating through fruits_list:")
for fruit in fruits_list:
    print(f"- {fruit}")

print("\nIterating through fruits_tuple:")
for fruit in fruits_tuple:
    print(f"- {fruit}")

print("\nIterating through fruits_set:")
for fruit in fruits_set: # Order is not guaranteed for sets
    print(f"- {fruit}")

print("\nIterating through fruits_dict (keys):")
for fruit_name in fruits_dict: # Iterates over keys by default
    print(f"- {fruit_name}")

print("\nIterating through fruits_dict (values):")
for count in fruits_dict.values():
    print(f"- Count: {count}")

print("\nIterating through fruits_dict (key-value pairs):")
for fruit_name, count in fruits_dict.items():
    print(f"- {fruit_name}: {count}")

# Task 4: Compare Membership Testing Performance
print("\n--- Task 4: Compare Membership Testing Performance ---")
print("Membership testing (using 'in' operator) performance:")
print("- **Sets and Dictionaries (keys):** These data structures are highly efficient for membership checks, typically performing in O(1) on average (constant time). This is because they are implemented using hash tables, which allow for very fast lookups.")
print("- **Lists and Tuples:** Membership checks in lists and tuples involve iterating through each element until a match is found or the end is reached. In the worst case, this means checking every element, leading to O(n) (linear time) complexity, where 'n' is the number of elements. For large lists/tuples, this can be significantly slower than sets or dictionaries.")
print("\nTherefore, for applications where frequent membership checks are critical, sets or dictionaries (checking keys) are the preferred data structures.")
