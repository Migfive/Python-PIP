people = [
    {
        'name': 'Pedro',
        'country': 'Colombia',
        'age': 18,
        'course': 'developer'
    },
    {
        'name': 'Juan',
        'country': 'Perú',
        'age': 17,
        'course': 'UX'
    },
    {
        'name': 'Carlos',
        'country': 'Chile',
        'age': 31,
        'course': 'Diseño'
    },
    {
        'name': 'Ana Maria',
        'country': 'Colombia',
        'age': 25,
        'course': 'Tester'
    }
]

operation = list(filter(lambda item: item["country"] == 'Colombia', people))
print(operation)
