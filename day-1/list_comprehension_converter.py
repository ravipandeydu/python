# Traditional for loop to list comprehension converter
cubes = []

for i in range(1, 11):
    cubes.append(i**3)

# List Comprehension
cubes_1 = [i**3 for i in range(1,11)]

#  With Filtering
cubes_even = [i**3 for i in range(1, 11) if i % 2 == 0]

# Nested Loop
nested_list = [[i, j] for i in range(1, 4) for j in range(1, 4)]

print(cubes_1, cubes_even, nested_list)