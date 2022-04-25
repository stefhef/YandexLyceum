from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def test():
    test_data = ({"input": '89194563603', 'output': True},
                 {"input": '+7919456(360)3', 'output': False},
                 {"input": '+7919 456360 3', 'output': True},
                 {"input": '+79194 5636 03', 'output': True},
                 {"input": '+7(919)4563603', 'output': True},
                 {"input": '+7(91 9)4563603', 'output': True},
                 {"input": '+78980(91 9)4563603', 'output': False},
                 {"input": '+1(91 9)4563603', 'output': False})

    for case in test_data:
        if is_correct_mobile_phone_number_ru(case['input']) != case['output']:
            return False

    return True


print("YES" if test() else "NO")
