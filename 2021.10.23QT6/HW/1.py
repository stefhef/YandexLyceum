import csv


with open('wares.csv', 'r', encoding='utf-8') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in table:
        if int(row['Old price']) > int(row['New price']):
            print(row['Name'])
