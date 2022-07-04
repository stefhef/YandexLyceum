def strip_punctuation_ru(data: str):
    data = data.replace(',',
                        ' ').replace('.',
                                     ' ').replace('!', ' ')
    data = data.replace('"', ' ').replace("'", ' ').replace('?', ' ').replace('_', ' ')
    data = data.replace("–", ' ').replace('—', ' ').replace(':', ' ').replace(';', ' ')
    for ind, elem in enumerate(data):
        if elem == '-' and ind > 0:
            if data[ind - 1] == ' ' and data[ind + 1] == ' ':
                data = data[:ind] + ' ' + data[ind + 1:]
    data = data.replace('(', ' ').replace(')', ' ').replace('  ', ' ')

    return data
