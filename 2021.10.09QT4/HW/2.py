formats = {}
space = {'B': (1024, 'KB'), 'KB': (1024, 'MB'), 'MB': (1024, 'GB'), 'GB': (1024, 'TB'), 'TB': 1024}
space_reverse = {'GB': (1024, 'MB'), 'MB': (1024, 'KB'), 'KB': (1024, 'B')}


def wt_to_bytes(wt, unit):
    global space_reverse
    if unit == 'B':
        return wt
    weight, unit = space_reverse[unit]
    wt *= weight
    return wt_to_bytes(wt, unit)


def convert_bytes(wt, unit):
    global space
    if wt < 1024:
        return f'Summary: {wt} {unit}'
    weight, unit = space[unit]
    wt = round(wt / weight)
    return convert_bytes(wt, unit)


with open('input.txt', 'r') as f:
    text = f.read().split('\n')
    print(text)

    for st in text:
        st = st.split()
        name_form, wt = st[0].split('.'), wt_to_bytes(int(st[-2]), st[-1])
        name, form = name_form

        if form not in formats:
            formats[form] = []
        
        formats[form].append((name, wt))

weight = 0
with open('output.txt', 'w') as f:
    for key, value in sorted(formats.items()):
        for name, wt in sorted(value):
            weight += wt
            print(f'{name}.{key}', file=f)
        print('----------', file=f)
        print(convert_bytes(weight, 'B'), end='\n\n', file=f)
        weight = 0

