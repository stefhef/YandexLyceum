from yandex_testing_lesson import strip_punctuation_ru


def test():
    test_data = ({"input": 'Кое-где', 'output': "Кое-где"},
                 {"input": 'ААААА    Б', 'output': "ААААА Б"},
                 {"input": 'З.З,З!?З:;)(З', 'output': "З З З З З"},
                 {"input": 'Какое-то          странное       чувство',
                  'output': "Какое-то странное чувство"},
                 {"input": 'Кое-где_____о', 'output': "Кое-где о"},
                 {"input": 'Кое___кто', 'output': "Кое кто"},
                 {"input": "Кое '' кто", 'output': "Кое кто"},
                 {"input": "Кое  кто .......", 'output': "Кое кто"},
                 {"input": 'Z---Z', 'output': 'Z---Z'},
                 {"input": "    .......", 'output': " "},
                 {"input": "    .......", 'output': " "},
                 {"input": "здесь - уже не дефис", 'output': "здесь уже не дефис"},)

    for case in test_data:
        if strip_punctuation_ru(case['input']) != case['output']:
            return False

    return True


print("YES" if test() else "NO")
