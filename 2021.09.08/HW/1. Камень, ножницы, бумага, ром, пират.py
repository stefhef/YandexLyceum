a1, a2 = input().lower().strip(), input().lower().strip()

if a1 == a2:
    print('ничья')

elif a1 == 'камень':
    if a2 in ['бумага', 'пират']:
        print('второй')
    else:
        print('первый')

elif a1 == 'ножницы':
    if a2 in ['камень', 'пират']:
        print('второй')
    else:
        print('первый')

elif a1 == 'ром':
    if a2 in ['ножницы', 'камень']:
        print('второй')
    else:
        print('первый')

elif a1 == 'пират':
    if a2 in ['бумага', 'ром']:
        print('второй')
    else:
        print('первый')

else:
    if a2 in ['ножницы', 'ром']:
        print('второй')
    else:
        print('первый')
