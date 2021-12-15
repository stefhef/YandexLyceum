import csv

summ = 1000

with open('wares.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    rows = [(row[0], int(row[1])) for row in reader]
    rows.sort(key=lambda x: x[1])

result = []

if rows[0][1] > summ:
    print('error')
else:
    while rows and summ >= rows[0][1]:
        count = summ // rows[0][1]
        if count > 10:
            count = 10
        summ -= count * rows[0][1]
        result.extend([rows[0][0]] * count)
        rows.pop(0)

    print(', '.join(result))