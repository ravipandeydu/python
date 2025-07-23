square = lambda x: x * x
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
reverse = lambda s: s[::-1]
uppercase = lambda s: s.upper()
filter_even = lambda list: [x for x in list if x % 2 == 0]
sum_of_list = lambda list: sum(list)