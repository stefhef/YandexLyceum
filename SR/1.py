file1, file2 = input(), input()
events = {}
with open(file1, 'r', encoding='utf8') as f:
    text = f.readlines()
    for line in text:
        line = line.strip().split()
        events[line[0]] = line[1:]

with open(file2, encoding='utf8') as f:
    text = f.readlines()
    out = set()
    items = tuple(map(str.strip, text))
    for item in items:
        for key, value in events.items():
            if item in value:
                out.add(key)

with open('events.txt', 'w', encoding='utf8') as f:
    print('\n'.join(sorted(out)), file=f)
