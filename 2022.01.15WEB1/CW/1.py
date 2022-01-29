space = {'Б': (1024, 'КБ'), 'КБ': (1024, 'МБ'), 'МБ': (1024, 'ГБ'), 'ГБ': (1024, 'ТБ'), 'ТБ': 1024}


def human_read_format(size):
    global space
    return convert_bytes(size, 'Б')


def convert_bytes(wt, unit='Б'):
    global space
    if wt < 1024:
        return f'{wt}{unit}'
    weight, unit = space[unit]
    wt = round(wt / weight)
    return convert_bytes(wt, unit)

print(convert_bytes(15000))