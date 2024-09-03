#file = open('text', encoding = 'utf-8')

#print(file.readline())
#print(file.readline())
#print(file.read())



#file.close()

with open('text', encoding = 'utf-8') as file:
    for line in file:
        print(line)