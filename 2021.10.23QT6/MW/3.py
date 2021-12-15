import csv

with open('alpha_oriona.csv', encoding='utf-8') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    queue = []
    out = list()
    for row in table:
        lum = int(row['luminosity'])
        out.append((row['date'], row['time'], lum))
        if len(out) > 1:
            if out[-2][-1] < lum:
                if len(out) > len(queue) + 1:
                    queue.clear()
                    queue.extend(out[:-1])
                out = out[-1:]
    if len(out) > len(queue):
        queue.clear()
        queue.extend(out)
with open('result.txt', 'w', encoding='utf-8') as result:
    print(len(queue), file=result)
    print(queue[0][0], queue[0][1], file=result)
