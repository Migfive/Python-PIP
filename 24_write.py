with open('text', 'r+', encoding='utf-8') as file:
    for line in file:
        print(line)

    # your write
    file.write('\nNew line added')
