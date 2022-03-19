from yandex_testing_lesson import is_palindrome


def test():
    if not is_palindrome('AA'):
        print('NO')
        return

    if is_palindrome('A<'):
        print('NO')
        return

    if is_palindrome('а роза упала на лапу Азора'):
        print('NO')
        return

    if not is_palindrome('FBF'):
        print('NO')
        return

    if is_palindrome('Fbf'):
        print('NO')
        return

    if not is_palindrome('101'):
        print('NO')
        return

    if not is_palindrome('saippuakivikauppias'):
        print('NO')
        return

    if not is_palindrome('ароза упаланалапу азора'):
        print('NO')
        return

    if not is_palindrome('Ароза упалАнАлапу азорА'):
        print('NO')
        return

    print('YES')


test()