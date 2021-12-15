import sys


def check_number(number):
    number = ''.join(number)
    number_normal = number.replace(' ', '').replace('\t', '').strip()
    if not number_normal.startswith('+7') and not number_normal.startswith('8') or \
            number.startswith('-') or number.endswith('-'):
        return 'неверный формат'

    number_new = ''
    scob = []
    for letter in number_normal:
        if letter not in '0123456789+-()':
            return 'неверный формат'
        if letter == '(':
            if scob:
                return 'неверный формат'
            scob.append(letter)
        elif letter == ')':
            try:
                scob.remove('(')
            except BaseException:
                return 'неверный формат'
        elif letter == '-':
            if number_new[-1] == '-':
                return 'неверный формат'
            number_new += '-'
        else:
            number_new += letter
    if scob:
        return 'неверный формат'
    number_new = number_new.replace('-', '')
    if number_new.startswith('8'):
        number_new = '+7' + number_new[1:]
    if len(number_new[2:]) < 10:
        return 'неверное количество цифр'
    return number_new[:12]


text = sys.stdin.readlines()
print(check_number(text))
