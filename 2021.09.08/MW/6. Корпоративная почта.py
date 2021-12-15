d_name = {}

for _ in range(int(input())):
    name = input().replace(
        '1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace(
        '6', '').replace('7', '').replace('8', '').replace('9', '').split('@')[0]
    if name not in d_name:
        d_name[name] = 1
    else:
        d_name[name] += 1


name_list = []
for _ in range(int(input())):
    name = input()
    name_list.append(name)

for name in name_list:
    if name in d_name:
        print(f'{name}{d_name[name]}@untitled.py')
        d_name[name] += 1
    else:
        print(f'{name}@untitled.py')
        d_name[name] = 1
