def is_correct_mobile_phone_ru(number: str):
    number = number.replace(' ', '').replace('-', '')
    
    if number.startswith('+7'):
        number = number[2:]
    elif number.startswith('8'):
        number = number[1:]
    else:
        return False

    if '(' in number:
        if ")" not in number or not number.startswith('(') or number.count(')') > 1 or number.count(
                '(') > 1 or number.index(')') != 4:
            return False
    elif ')' in number:
        return False

    number = number.replace(')', '').replace('(', '')

    if not number.isdigit():
        return False

    if len(number) != 10:
        return False

    return True


print("YES" if is_correct_mobile_phone_ru(input()) else "NO")
