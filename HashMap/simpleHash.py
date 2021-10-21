headers_array = ['Id', 'Name']
data = ['0001']

for x, y in zip(headers_array, data):
    if not y:
        y = ''
        x = ''
        print(x, y)
    else:
        print(x, y)