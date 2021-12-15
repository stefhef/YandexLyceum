d = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
     "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
     "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
     "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
     "б": "b", "ю": "ju", "ё": "jo"}

for key, value in tuple(d.items()):
    d[key.upper()] = value.capitalize()


with open('cyrillic.txt', encoding='UTF-8') as cyr_file:
    text = ''.join([d.get(sym, sym) for sym in cyr_file.read()])

with open('transliteration.txt', 'w', encoding='utf-8') as tr:
    tr.write(text)
