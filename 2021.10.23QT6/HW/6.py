import sys
sm, mn = map(int, input().split())
out = []
for line in sys.stdin:
    line = line.strip().split()
    res = tuple(map(int, line[2:]))
    if sum(res) >= sm and len(tuple(filter(lambda x: x >= mn, res))) == 3:
        line.append(sum(res))
        out.append(line)

with open('exam.csv', 'w') as outfile:
    print('Фамилия;имя;результат 1;результат 2;результат 3;сумма', file=outfile)
    for row in out:
        print(f'{row[0]};{row[1]};{row[2]};{row[3]};{row[4]};{row[5]}', file=outfile)
