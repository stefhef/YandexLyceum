import os


def convert_bytes(wt, unit='Б'):
    space = {'Б': (1024, 'КБ'), 'КБ': (1024, 'МБ'), 'МБ': (1024, 'ГБ'), 'ГБ': (1024, 'ТБ'), 'ТБ': 1024}
    if wt < 1024:
        return f'{wt}{unit}'
    weight, unit = space[unit]
    wt = round(wt / weight)
    return convert_bytes(wt, unit)


def get_files_sizes():
    files = map(lambda x: f'{x} {convert_bytes(os.path.getsize(x))}', filter(os.path.isfile, os.listdir('.')))
    return '\n'.join(files)


if __name__ == '__main__':
    print(get_files_sizes())