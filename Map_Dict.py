item = [
    {
        'product': 'shirt',
        'Price': 100,

    },
    {
        'product': 'pants',
        'Price': 150
    },
    {
        'product': 'zhoes',
        'Price': 200
    }
]

prices = list(map(lambda element: element['Price'], item))

print(prices)


def add_taxes(x):
    x_copy = x.copy()
    x_copy['taxes'] = x_copy['Price'] * .19
    return x_copy


new_items = list(map(add_taxes, item))
print(new_items)
print(item)
