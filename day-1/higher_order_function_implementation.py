def custom_map(func, iterable):
    return [func(item) for item in iterable]

def custom_filter(func, iterable):
    return [item for item in iterable if func(item)]

def custom_reduce(func, iterable):
    result = iterable[0]
    for x in iterable[1:]:
        result = func(result, x)
    return result

