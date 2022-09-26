import csv
import json

DATA_ADS = 'ads.csv'
JSON_ADS = 'ads.json'
DATA_CATEGORIES = 'categories.csv'
JSON_CATEGORIES = 'categories.json'


def convert_file(csv_file, json_file, model_name):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model_name, 'pk': int(row['ID'] if 'Id' in row else row['id'])}
            to_add['fields'] = row
            result.append(to_add)
        with open(json_file, 'w', encoding='utf-8') as json_f:
            json_f.write(json.dumps(result, ensure_ascii=False))


convert_file(DATA_CATEGORIES, JSON_CATEGORIES, 'ads.category')
