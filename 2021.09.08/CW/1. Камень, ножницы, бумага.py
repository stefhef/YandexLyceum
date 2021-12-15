a1, a2 = input().lower().strip(), input().lower().strip()

if a1 == a2:
    print('ничья')
elif a1 == 'камень':
    if a2 == 'бумага':
        print('второй')
    else:
        print('первый')
elif a1 == 'ножницы':
    if a2 == 'бумага':
        print('первый')
    else:
        print('второй')
else:
    if a2 == 'ножницы':
        print('второй')
    else:
        print('первый')
        