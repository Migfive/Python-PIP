import functools

numbers = [1, 2, 3, 4]


def accum(counter, items):
    print('counter =>', counter)
    print('items =>', items)
    return counter + items


# Using functools.reduce() to calculate sum of numbers in the list
result = functools.reduce(accum, numbers)

print(result)
