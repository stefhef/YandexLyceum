import sys

flag = True
d = {}


for line in sys.stdin:
    line = line.strip()
    if flag:
        flag = False
    elif line == '':
        flag = True
    else:
        line = line.split()
        cab, subject = int(line[-1]), ' '.join(line[:-1])
        if cab in d:
            if subject not in d[cab]:
                d[cab].append(subject)
        else:
            d[cab] = [subject]

for cab, subjects in sorted(d.items()):
    print(f'{cab}: {", ".join(subjects)}')
