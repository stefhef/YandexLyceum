items = []
with open('luggage.txt', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        line = line.strip().split()
        name, c, wt = line[:-2], int(line[-1]), float(line[-2])
        items.append((wt, c, ' '.join(name)))

weight = float(input())

with open('taken_items.txt', 'w', encoding='utf-8') as f:

    out = ''
    sum_c = 0
    count = 0

    for item in sorted(items):
        wt, c, name = item
        weight -= wt
        if weight >= 0:
            out = name
            count += 1
            sum_c += c

    print(count, file=f)
    print(sum_c, file=f)
    print(out, file=f)

