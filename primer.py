import csv
import json
import itertools

csv_file = open('books.csv', newline='')
reader = csv.DictReader(csv_file, delimiter=',')

with open('users.json') as f:
    json_file = json.load(f)

result_list = []

for i, elem in enumerate(json_file):
    dict_obj = {'name': elem['name'],
                'gender': elem['gender'],
                'address': elem['address'],
                'age': elem['age'],
                'books': []}
    if i == 27:
        dict_obj['books'] = list(itertools.islice(reader, 22))
    else:
        dict_obj['books'] = list(itertools.islice(reader, 7))
    result_list.append(dict_obj)

with open('result.json', 'w') as outfile:
    json.dump(result_list, outfile, indent=4)
