import csv

result = []
present = float(input())
with open('vps.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)
    for i, row in enumerate(reader):
        if float(row[-2]) >= present:
            result.append(row[0])

print(*result, sep='\n')
