import sys


def check_number(number: list):
    number = ''.join(number)
    number_normal = number.replace(' ', '').replace('\t', '').strip()
    if not number_normal.startswith('+7') and not number_normal.startswith('8') or\
            number.startswith('-') or number.endswith('-'):
        return 'error'

    number_new = ''
    scob = []
    for letter in number_normal:
        if letter not in '0123456789+-()':
            return 'error'
        if letter == '(':
            if scob:
                return 'error'
            scob.append(letter)
        elif letter == ')':
            try:
                scob.remove('(')
            except BaseException:
                return 'error'
        elif letter == '-':
            if number_new[-1] == '-':
                return 'error'
            number_new += '-'
        else:
            number_new += letter
    if scob:
        return 'error'
    if number_new.startswith('8'):
        number_new = '+7' + number_new[1:]
    if len(number_new[2:]) < 10:
        return 'error'
    return number_new.replace('-', '')[:12]


text = sys.stdin.readlines()
print(check_number(text))
