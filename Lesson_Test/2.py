from yandex_testing_lesson import is_prime


def test():
    test_data = ({"input": 2, 'output': True},
                 {"input": 3, 'output': True},
                 {"input": 1, 'output': False})

    for case in test_data:
        try:
            if is_prime(case['input']) != case['output']:
                return False
        except ValueError:
            return False

    for number in [0, -1]:
        try:
            a = is_prime(number)
            print('NO')
            return False
        except ValueError:
            pass

    return True


print("YES" if test() else "NO")
