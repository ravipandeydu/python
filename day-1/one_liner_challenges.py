from functools import reduce

squares = [i*i for i in range(1, 11) if i % 2 == 0]

odd_numbers = [i for i in range(1, 11) if i % 2 != 0]

multiply_by_two = [i*2 for i in range(1, 11) if i % 2 == 0]

cubes = [i**3 for i in range(1, 11)]

sum_using_reduce = reduce(lambda x, y: x + y, [i for i in range(1, 11)])

print(sum_using_reduce)