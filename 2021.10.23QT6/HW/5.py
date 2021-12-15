import csv


subject = input()
year1, year2 = input().split()
out = []
with open('salary.csv', encoding='utf-8') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in table:
        if row['Федеральный округ'] == subject:
            price1, price2 = int(row[year1]), int(row[year2])
            if price2 < price1 * 1.04:
                out.append((row['Субъект'], price1, price2))

with open('out_file.csv', 'w') as outfile:
    if out:
        print(f'Субъект;{year1};{year2}', file=outfile)
        for row in out:
            print(f'{row[0]};{row[1]};{row[2]}', file=outfile)
    else:
        print('', file=outfile)