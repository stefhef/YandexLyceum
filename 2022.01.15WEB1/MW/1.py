# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os

space = {'Б': (1024, 'КБ'), 'КБ': (1024, 'МБ'), 'МБ': (1024, 'ГБ'), 'ГБ': (1024, 'ТБ'), 'ТБ': 1024}


def convert_bytes(wt, unit):
    global space
    if wt < 1024:
        return f'{wt}{unit}'
    weight, unit = space[unit]
    wt = round(wt / weight)
    return convert_bytes(wt, unit)


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    if not total_size:
        total_size = os.path.getsize(start_path)
    return total_size


path = input()
files = list()
for file in os.listdir(path):
    size = get_size(path + rf'\{file}')
    files.append((file, size))
files = map(lambda x: (x[0], convert_bytes(x[1], "Б")), sorted(files,
                                                               key=lambda x: x[1],
                                                               reverse=True)[:10])
print("\n".join(map(lambda x: f"{x[0]}\t-\t{x[1]}", files)))
