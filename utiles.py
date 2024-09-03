def get_population():
    keys = ['col', 'bol']
    value = [300, 400]
    return keys, value


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result


