import json

with open('./json_example.json', 'r', encoding = 'utf8') as f :
    # contents = f.read()
    json_data = json.load(f)

print('json_data')
print(json_data)
print()

print('employees')
for employee in json_data['employees'] :
    print(employee)
print()

print('employees firstname')
for employee in json_data['employees'] :
    print(employee['firstName'])
print()

print('employees lastname')
for employee in json_data['employees'] :
    print(employee['lastName'])
