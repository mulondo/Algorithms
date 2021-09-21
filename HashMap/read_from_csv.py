import csv

requirements = []
with open('requirements.csv', 'r') as new_file:
    print(type(new_file))
    for line in new_file:
        token = line.split(',')
        print(token[0])
        items = token[0]
        price = token[1]
        requirements.append([items, price])

print(requirements)