import sys

count = False
num = False
sort = False
for arg in sys.argv:
    if '--count' == arg:
        count = True
    elif '--num' == arg:
        num = True
    elif '--sort' == arg:
        sort = True
    else:
        filename = arg

try:
    with open(filename, "r") as file:
        data = list(map(str.strip, file.readlines()))
except FileExistsError:
    print("ERROR")
    exit("ERROR")
except FileNotFoundError:
    print("ERROR")
    exit("ERROR")

if sort:
    data = sorted(data)

for i, line in enumerate(data):
    if num:
        print(f'{i} {line}')
    else:
        print(line)
if count:
    print(f"rows count: {len(data)}")
