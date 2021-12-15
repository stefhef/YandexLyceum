import csv
from collections import defaultdict


def search_path(start, end, fin_path='', weight=0, c=0):
    global paths
    for path in d[start]:
        if path[0] == end:
            weight += path[1]
            if start in fin_path:
                fin_path += f' {end}'
            else:
                fin_path += f'{start} {end}'
            paths.append((fin_path, weight))
        elif c == 0:
            search_path(path[0], end, f'{start} {path[0]}', weight=int(path[1]), c=1)


with open('input.csv', encoding='utf-8') as inputcsvfile:
    table = csv.reader(inputcsvfile, delimiter=';', quotechar='"')
    count = 0
    d = defaultdict(list)
    for row in table:
        if row[2]:
            d[row[0]].append((row[1], int(row[2])))
        else:
            start, end = row[0], row[1]
    # print(d)
    # print(start, end, sep='\t')
    paths = []
    search_path(start, end)

# print(paths)
print(sorted(paths, key=lambda x: x[1])[0][0])
