food = ('Carne', 'Maiz', 'aguacate')
menu = ('molida', 'trillado', 'Maduro')

all_menu = list(map(lambda a, b: a + " " + b, food, menu))

print(all_menu)

# Example With Numbers
numbers = [1, 2, 3, 4]

increment = list(map(lambda a: a * 2, numbers))

print(increment)
