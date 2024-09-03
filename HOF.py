def increment(x):
    return x + 1


def hig_ord_func(x, func):
    return x + func(x)


result = hig_ord_func(2, increment)

print(result)

# Example for Lambda

increment_V2 = lambda x: x + 1

hig_order_func_V2 = lambda x, funct: x + funct(x)

result2 = hig_order_func_V2(2, increment_V2)

print(result2)

# Using a named function instead of a lambda in the higher-order function
#
result3 = hig_order_func_V2(2, lambda x: x + 1)

print(result3)
