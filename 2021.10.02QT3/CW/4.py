import re
rus_a = 'йцукенгшщзхъёфывапролджэячсмитьбю'
eng_a = 'qwertyuiopasdfghjklzxcvbnm'


def check_password(pas: str):

    if len(pas) <= 8:
        return 'error'

    if pas.islower() or pas.isupper() or pas.isdigit()\
            or pas.isalpha() or not re.match(r'.*[0-9].*', pas):
        return 'error'
    pass_check = pas.lower().strip()

    elem, pass_check = pass_check[:4], pass_check[4:]
    if check_third(elem):
        return 'error'
    for el in pass_check:
        elem = elem[1:] + el
        if check_third(elem):
            return 'error'
    return 'ok'


def check_third(elem: str):
    try:
        if rus_a.index(elem) or eng_a.index(elem):
            return True
    except BaseException:
        return False


print(check_password(input()))
