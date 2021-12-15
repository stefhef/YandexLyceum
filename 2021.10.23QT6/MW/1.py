import csv
import pandas as pd
import numpy as np


def refactor_number(number: float):
    try:
        n = str(number).split('.')

        if set(n[1]) == {'0'}:
            return n[0]
        return number
    except BaseException:
        return number


with open('output.csv', 'w') as outp:

    count = 0

    data = pd.read_excel('data.xlsx', na_values='', na_filter=False)
    data: pd.DataFrame
    count_ln, ln = data.shape
    wrt = csv.writer(outp, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar='"')

    for i in range(ln):
        try:
            data.drop(f'Unnamed: {i}', axis=0)
        except BaseException:
            pass
    wrt.writerow(data.keys())
    for line in data.values:
        out_l = list()
        line: list
        for elem in line:

            if isinstance(elem, float):
                elem = refactor_number(elem)

            if elem is None or 'Unnamed: ' in elem:
                elem = ''
            out_l.append(elem)
        wrt.writerow(out_l)
        count += 1
