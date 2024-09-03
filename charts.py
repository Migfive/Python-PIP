import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_line_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 20, 30]
    #generate_bar_chart(labels, values)
    generate_line_chart(labels, values)


