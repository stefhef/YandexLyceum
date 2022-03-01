from zipfile import ZipFile

space = {'Б': (1024, 'КБ'), 'КБ': (1024, 'МБ'), 'МБ': (1024, 'ГБ'), 'ГБ': (1024, 'ТБ'), 'ТБ': 1024}


def convert_bytes(wt, unit):
    global space
    if wt < 1024:
        return f'{wt}{unit}'
    weight, unit = space[unit]
    wt = round(wt / weight)
    return convert_bytes(wt, unit)


with ZipFile("input.zip") as myzip:
    for elem in myzip.infolist():
        filename = elem.filename
        filename: str
        if filename[-1] == '/':
            filename = filename[:-1]
            size = ''
        else:
            size = convert_bytes(elem.file_size, "Б")
        print('  ' * (filename.count("/")) + filename.split('/')[-1] + f' {size}')
