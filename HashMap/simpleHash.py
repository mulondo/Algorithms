headers_array = ['Id', 'Name']
data = ['0001']

header_array = ['Book', 'Pen']
employees = [{'Book': 'picfure', 'Pen': 'bic', 'Pencils': 'zin'}]
new_header = []
emps = {}


for employee in employees:
    emps = employee

for header in header_array:
    # if header == emps.get(header):
    print(header, employee)
    if header in emps.keys():
        new_header.append(header)
        # print(header, emps.get(header))
print(new_header)

for x, y in zip(headers_array, data):
    if not y:
        y = ''
        x = ''
        print(x, y)
    else:
        print(x, y)