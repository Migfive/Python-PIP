import csv


def read_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        vale = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            vale.append(country_dict)
        return vale


if __name__ == '__main__':
    data = read_csv('data.csv')
    print(data[0])
