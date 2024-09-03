import utiles


def run():
    keys, values = utiles.get_population()

    print(keys, values)

    var = [
        {
            'Country': 'Colombia',
            'population': 30_456_235
        },
        {
            'Country': 'United States',
            'population': 328_239_523
        }
    ]
    country = input('Type Country => ')
    result = utiles.population_by_country(var, country)

    print(result)


if __name__ == '__main__':
    run()
